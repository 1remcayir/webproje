## 🔐 Web Security Analyzer

### 📄 Proje Tanımı

Python tabanlı bu araç, web trafiğini analiz ederek yaygın güvenlik açıklarını (XSS, SQL Enjeksiyonu, CSRF vb.) tespit eder ve `.pcap` dosyalarından anlamlı güvenlik çıktıları üretir.

---

### ⚙️ Özellikler

* **Otomatik Güvenlik Açığı Tespiti**
  `.pcap` dosyalarındaki XSS, SQL Enjeksiyonu ve CSRF gibi sık karşılaşılan açıkları analiz eder.

* **Cookie ve HTTP Header Analizi**
  `HttpOnly` veya `Secure` gibi bayrakları olmayan güvensiz çerezleri ve eksik/güvensiz HTTP başlıklarını tespit eder.

* **Raporlama**
  Tespit edilen açıkları ve risk seviyelerini detaylandıran bir çıktı raporu oluşturur.

---

### 👥 Ekip

* **2320191020 - İREM ÇAYIR**: Paket analizi ve açık tespit sistemi
* **2320191011 - MURAT ÜNSAL**: Arayüz ve raporlama modülü

---

### 🚧 Yol Haritası

Projeye dair ileriye dönük planlar için `ROADMAP.md` dosyasını inceleyebilirsiniz.

---

### 🔍 Araştırmalar

| Konu                    | Dosya                     | Açıklama                                        |
| ----------------------- | ------------------------- | ----------------------------------------------- |
| HTTP Header Saldırıları | researchs/http-headers.md | HTTP başlıklarının zafiyet analizleri           |
| Aircrack-ng İncelemesi  | researchs/aircrack.md     | Kablosuz ağ analiz aracı derinlemesine inceleme |
| Payload Örnekleri       | researchs/payloads.md     | Sık kullanılan XSS/SQL payload örnekleri        |

---

### 📀 Kurulum

```bash
# Reponun klonlanması
git clone https://github.com/YOUR_USERNAME/web-security-analyzer.git
cd web-security-analyzer

# Sanal ortam kurulumu (isteğe bağlı)
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

# Gerekli paketlerin yüklenmesi
pip install -r requirements.txt
```

---

### ▶️ Kullanım

```bash
python main.py --input test_capture.pcap --output analysis_report.txt
```

**Adımlar:**

1. Bir ağ trafiği kaydı olan `.pcap` dosyasını hazırlayın.
2. Yukarıdaki komutla analiz sürecini başlatın.
3. `analysis_report.txt` dosyasından tespitleri inceleyin.

---

### 🤝 Katkı

1. Reponun çatallanmasını (fork) yapın.
2. Ayrı bir dal oluşturun: `feature/ozellik`
3. Anlamlı commit mesajlarıyla geliştirmenizi yapın.
4. Pull Request oluşturun.

Detaylar için `CONTRIBUTING.md` dosyasına bakın.

---

### 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

### 🙏 Teşekkürler

* [Scapy](https://scapy.net/) - Paket analiz altyapısı
* [OWASP](https://owasp.org/) - Güvenlik standartları
* Katkı sağlayan tüm geliştiricilere sonsuz teşekkürler


###Contact / İletişim (Optional)
*Project Maintainer: İREM ÇAYIR - MURAT ÜNSAL - iremgur780@gmail.com - muratunsal675@gmail.com
Found a bug? Open an issue.

*Proje Sorumlusu: İREM ÇAYIR - MURAT ÜNSAL - iremgur780@gmail.com - muratunsal675@gmail.com. Hata bulursanız bir sorun bildirin.
