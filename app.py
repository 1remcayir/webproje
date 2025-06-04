import dpkt
import scapy.all as scapy
import re

def load_pcap(file_path):
    with open(file_path, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        return list(pcap)

def analyze_packets(packets):
    xss_patterns = [r"<script.*?>.*?</script>", r"onerror\s*=", r"javascript:"]
    sqli_patterns = [r"(\%27)|(\')|(\-\-)|(\%23)|(#)", r"or\s+1=1", r"union\s+select"]

    insecure_cookies = []
    xss_found = []
    sqli_found = []

    for ts, buf in packets:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if not isinstance(ip.data, dpkt.tcp.TCP):
                continue
            tcp = ip.data
            if tcp.dport == 80 or tcp.sport == 80:
                try:
                    http = dpkt.http.Request(tcp.data)
                    # XSS kontrolü: URI ve header
                    for pattern in xss_patterns:
                        if re.search(pattern, http.uri, re.IGNORECASE):
                            xss_found.append(http.uri)
                        for h,v in http.headers.items():
                            if re.search(pattern, v, re.IGNORECASE):
                                xss_found.append(v)

                    # SQLi kontrolü: URI ve header
                    for pattern in sqli_patterns:
                        if re.search(pattern, http.uri, re.IGNORECASE):
                            sqli_found.append(http.uri)
                        for h,v in http.headers.items():
                            if re.search(pattern, v, re.IGNORECASE):
                                sqli_found.append(v)

                    # İnsecure Cookie kontrolü
                    if 'cookie' in http.headers:
                        cookie = http.headers['cookie']
                        if 'secure' not in cookie.lower():
                            insecure_cookies.append(cookie)

                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                    continue
        except Exception as e:
            continue

    return {
        'xss': list(set(xss_found)),
        'sqli': list(set(sqli_found)),
        'insecure_cookies': list(set(insecure_cookies))
    }

def generate_report(results, output_file):
    with open(output_file, 'w') as f:
        f.write("Web Security Analyzer Raporu\n")
        f.write("============================\n\n")

        if results['xss']:
            f.write("🚨 XSS Tespit Edildi:\n")
            for item in results['xss']:
                f.write(f"- {item}\n")
            f.write("\n")
        else:
            f.write("✅ XSS açığı bulunamadı.\n\n")

        if results['sqli']:
            f.write("🚨 SQL Injection Şüphesi:\n")
            for item in results['sqli']:
                f.write(f"- {item}\n")
            f.write("\n")
        else:
            f.write("✅ SQL Injection şüphesi bulunamadı.\n\n")

        if results['insecure_cookies']:
            f.write("⚠️ Güvensiz Cookie Tespit Edildi:\n")
            for item in results['insecure_cookies']:
                f.write(f"- {item}\n")
            f.write("\n")
        else:
            f.write("✅ Güvensiz cookie bulunamadı.\n\n")

    print(f"Rapor {output_file} dosyasına kaydedildi.")

if __name__ == "__main__":
    pcap_path = "test_capture.pcap"   # Analiz edilecek pcap dosyası
    report_path = "result_report.txt"  # Oluşturulacak rapor dosyası

    packets = load_pcap(pcap_path)
    results = analyze_packets(packets)
    generate_report(results, report_path)
