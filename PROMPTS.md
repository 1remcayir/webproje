## 💬 prompts.md

### Web Security Analyzer – Kullanıcı Promtları ve Test Komutları

Bu belge, `Web Security Analyzer` aracıyla birlikte kullanılabilecek örnek prompt ve test komutlarını içerir. Amaç, kullanıcıların analizleri kolaylaştırması ve test senaryolarını daha etkili yürütebilmesidir.

---

### 📁 Girdi Dosyası Hazırlama Promtları

```text
Lütfen analiz etmek istediğiniz ağ trafiğini bir `.pcap` dosyası olarak sağlayınız.
Örnek komut:  
> tcpdump -i wlan0 -w test_capture.pcap
```

```text
Test senaryosu için XSS payload'ıları içeren bir HTTP isteği üretin.  
Önerilen Payload:  
> <script>alert('XSS')</script>
```

```text
SQL Injection testi için aşağıdaki gibi bir sorgu gönderimi yapabilirsiniz:  
> ' OR '1'='1'; --
```

---

### 🧪 Analiz Başlatma Promtları

```text
Analiz başlatılıyor. Lütfen bekleyiniz...

> python main.py --input test_capture.pcap --output result.txt
```

```text
Analiz tamamlandı. Rapor dosyası: `result.txt`  
Devam etmek için bir seçim yapın:
[1] Raporu görüntüle  
[2] Yeni bir dosya analiz et  
[3] Çıkış
```

---

### 🔍 Güvenlik Açığı Tespiti Sonrası Promtlar

```text
⚠️ Uyarı: Analiz sonucunda yüksek riskli bir XSS açığı tespit edildi.  
Dosya: test_capture.pcap  
Risk Seviyesi: HIGH  
İlgili Satır: 184  
Payload: <script>alert("xss")</script>
```

```text
⚠️ SQL Enjeksiyonu şüpesi tespit edildi.  
Lütfen ilgili web uygulamasının giriş filtrelerini kontrol ediniz.
```

---

### 🌐 Web Arayüzü (Geliştirilecek Özellikler İçin)

```text
[Beta] Web arayüzüne hoş geldiniz.  
Lütfen analiz etmek istediğiniz `.pcap` dosyasını yükleyin ve "Analiz Et" butonuna tıklayın.
```

```text
📊 Analiz tamamlandı. Aşağıda sonuçları grafiksel olarak inceleyebilirsiniz:  
[XSS] [SQLi] [CSRF] [Cookies]  
(Bar grafiği/renkli uyarılar için UI mockup eklenecek)
```

---

