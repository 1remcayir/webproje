# Web Güvenlik Analizi – PCAP Tabanlı Tespitler

Bu çalışma, Python ile hazırlanmış bir analiz aracının `.pcap` dosyaları üzerinden XSS, SQLi ve insecure cookie gibi yaygın web güvenlik açıklarını tespit etmesini konu alır.

---

## 1. HTTP Paketlerinden XSS Açığı Tespiti

**Açıklama:**  
Kod, `.pcap` dosyasındaki HTTP isteklerini analiz ederek URI ve başlıklarda yaygın XSS kalıplarını (ör. `<script>`, `onerror`) arar.

**2025 Etkisi:**  
Otomatikleştirilmiş ağ güvenliği tarayıcılarında XSS kontrolü halen önemlidir; özellikle IoT ve mobil ağlar için kritik rol oynar.

**Kaynak:**  
[OWASP XSS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)

---

## 2. SQL Injection İzlerinin Algılanması

**Açıklama:**  
RegEx ile URI ve HTTP başlıklarında SQLi şüphelisi olabilecek karakter dizileri (`'`, `--`, `OR 1=1`) aranır.

**2025 Etkisi:**  
Web trafiğinde arka kapı girişleri ve sızma testlerinde hızlı SQLi tespiti sunar; özellikle API güvenliğinde kullanılabilir.

**Kaynak:**  
[OWASP SQLi Prevention](https://owasp.org/www-community/attacks/SQL_Injection)

---

## 3. Güvensiz (Secure Olmayan) Çerezlerin Belirlenmesi

**Açıklama:**  
HTTP başlıklarında yer alan çerezlerin `Secure` bayrağı içerip içermediği kontrol edilerek güvenlik açığı belirlenir.

**2025 Etkisi:**  
GDPR ve KVKK uyumluluğu açısından büyük veri sistemlerinde cookie güvenliği daha sıkı izlenecek; bu tür tespit araçları kritik olacak.

**Kaynak:**  
[Mozilla Web Security Guidelines – Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)

---

## 4. RegEx Tabanlı Anomali Tespiti

**Açıklama:**  
Belirli kötü niyetli desenleri saptamak için düzenli ifadeler (regex) kullanılır, bu da statik içeriklerde hızlı tarama imkanı verir.

**2025 Etkisi:**  
RegEx, makine öğrenmesi öncesi filtreleme katmanı olarak kullanılabilir; SIEM sistemleriyle entegre edilmesi mümkündür.

**Kaynak:**  
[Regular Expressions in Security Research (Blog by Palo Alto)](https://unit42.paloaltonetworks.com/tag/regex/)

---

## 5. PCAP Dosyalarından Otomatik Raporlama

**Açıklama:**  
Kod, analiz sonuçlarını kullanıcı dostu bir metin dosyasına (`result_report.txt`) yazarak görsel ve yazılı çıktı üretir.

**2025 Etkisi:**  
Güvenlik analistlerinin olaylara hızlı müdahale etmesini sağlar; gelecekte otomatik SIEM dashboard’larına entegre edilebilir.

**Kaynak:**  
[GitHub – dpkt: Fast, simple packet creation / parsing](https://github.com/kbandla/dpkt)

---
# PCAP Analiz Scripti - Ana Çalışma Kısmı

```python
import os

if __name__ == "__main__":
    # Analiz edilecek PCAP dosyasının tam yolu
    pcap_path = r"C:\Users\efekan\Desktop\Yeni klasör (2)\test_capture.pcap.pcapng"
    # Oluşturulacak rapor dosyasının adı
    report_path = "result_report.txt"

    # Dosyanın var olup olmadığını kontrol et
    if not os.path.isfile(pcap_path):
        print(f"Hata: Dosya bulunamadı -> {pcap_path}")
        exit(1)

    # PCAP dosyasını yükle
    packets = load_pcap(pcap_path)
    # Paketleri analiz et
    results = analyze_packets(packets)
    # Analiz sonuçlarını rapor olarak kaydet
    generate_report(results, report_path)

```

**load_pcap(pcap_path)**
Belirttiğin pcap dosyasını açar ve içindeki tüm paketleri okur.
Dönen sonuç, paketlerin zaman damgası ve ham verilerini içeren bir liste.

**analyze_packets(packets)**
Okunan paketleri analiz eder.
XSS, SQL Injection ve güvensiz cookie gibi güvenlik açıklarını arar.
Bulduğu şüpheli içerikleri bir sözlük (dict) içinde döner.

**generate_report(results, report_path)**
Analiz sonuçlarını bir metin dosyasına yazar (rapor oluşturur).
Dosya adı ve yolu report_path ile belirlenir.
Bu satırlar birlikte çalışınca:
1.PCAP dosyasını okur,
2.İçerik güvenlik analizi yapar,
3.Bulunan sonuçları rapor dosyasına yazar.

![image](https://github.com/user-attachments/assets/70d21c50-9348-4887-aaa2-e7d107796cac)
