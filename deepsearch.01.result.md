
# Web Geliştirme ve Güvenlik: DNS Spoofing Üzerine Bir İnceleme

## 🎯 Proje Amacı

Bu araştırmanın amacı, **web geliştirme sürecinde güvenlik** perspektifiyle DNS spoofing saldırılarını, kullanılan araçları ve alınabilecek önlemleri incelemektir. Web geliştiricilerin, uygulamalarını daha güvenli hale getirmesi için potansiyel saldırı senaryoları hakkında farkındalık kazanması hedeflenmiştir.

---

## 🌐 DNS Spoofing Nedir?

DNS spoofing (DNS sahteciliği), bir kullanıcının DNS sorgularına sahte yanıtlar verilerek onu saldırganın kontrolündeki bir siteye yönlendirme yöntemidir. Bu saldırılar, web uygulamalarının güvenliğini tehdit eder ve kullanıcıların verilerinin çalınmasına neden olabilir.

---

## 🛠 İncelenen Araçlar

### 🐍 Ettercap
- **Kullanım Amacı:** MITM (Man-in-the-Middle) saldırıları ve DNS sahteciliği
- **Geliştirici Etkisi:** ARP poisoning yoluyla kullanıcıyı sahte web sayfasına yönlendirerek veri çalma
- **Önlem:** HTTPS, DNSSEC ve ağ izolasyonu

### 📄 Dnsspoof
- **Kullanım Amacı:** Statik yönlendirme ile DNS sahteciliği
- **Geliştirici Etkisi:** Saldırganın hazırladığı sahte sayfaya yönlendirme
- **Önlem:** DNSSEC, domain whitelisting

### 🧠 DNSChef
- **Kullanım Amacı:** Detaylı DNS spoofing yapılandırması
- **Web Güvenliği Bağlantısı:** Uygulama geliştiricilerin test senaryolarında kullanılabilir

### ⚡ Bettercap
- **Kullanım Amacı:** Gelişmiş MITM ve DNS spoofing saldırıları
- **Öneri:** TLS zorunlu bağlantılar ile etkisiz hale getirilebilir

### 💡 DDSpoof
- **Kullanım Amacı:** DHCP üzerinden sahte DNS sunucusu tanımlama
- **Tehlike:** Geliştirici cihazlarının sahte DNS’e yönlendirilmesi

### 🎭 SET (Social Engineering Toolkit)
- **Kullanım Amacı:** Phishing siteleri oluşturma ve DNS spoofing ile trafik yönlendirme
- **Web Güvenliği Bağlantısı:** Gerçekçi sahte web sayfaları ile kullanıcıların kandırılması

---

## 🧪 Test Ortamı

- **İşletim Sistemi:** Kali Linux
- **Ortam:** Yerel ağ (VM ağ ortamı)
- **Test Edilen Senaryo:** DNS spoofing ile sahte oturum açma sayfasına yönlendirme

---

## 🔐 Web Geliştiriciler İçin Güvenlik Önerileri

| Önlem                    | Açıklama |
|--------------------------|----------|
| HTTPS/TLS                | Şifreli bağlantılar saldırı etkisini azaltır |
| DNSSEC                   | Sahte DNS yanıtlarını engeller |
| MFA (Çok Faktörlü Kimlik Doğrulama) | Phishing saldırılarına karşı etkili |
| Web Uygulama Güvenlik Testleri     | Düzenli güvenlik testleri ile açıklar tespit edilir |
| Güvenli Sunucu Yapılandırması     | DNS ve DHCP sunucuları güvenli konfigüre edilmelidir |

---

## 📂 Dosya Yapısı (Örnek)

```
research/
├── Web-Security-DNS-Spoofing/
│   ├── README.md
│   ├── spoofed-hosts.txt
│   ├── dnschef-config.json
│   ├── ettercap-filter.ecf
│   └── logs/
│       ├── ettercap.log
│       ├── dnschef.log
│       └── phishing-report.html
```

---

## 📚 Kaynakça

- [OWASP Foundation](https://owasp.org/)
- [Kali Linux Tools Documentation](https://tools.kali.org/)
- [Bettercap Resmi Sitesi](https://www.bettercap.org/)
- [Ettercap Documentation](https://www.ettercap-project.org/)

---

## ✍️ Hazırlayan

**İREM ÇAYIR - MURAT ENES ÜNSAL**  
**Web Geliştirme ve Güvenliği Araştırması - 2025**
