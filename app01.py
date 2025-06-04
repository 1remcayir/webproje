import os

pcap_path = "test_capture.pcap"
if not os.path.exists(pcap_path):
    print(f"Hata: {pcap_path} dosyası bulunamadı!")
    exit()

packets = load_pcap(pcap_path)
