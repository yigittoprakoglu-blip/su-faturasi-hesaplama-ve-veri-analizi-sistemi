# su-faturasi-hesaplama-ve-veri-analizi-sistemi
Python, Pandas ve Matplotlib kullanılarak geliştirilmiş; farklı abone tiplerine göre kademeli su faturası hesaplayan, istatistiksel analizler yapan ve görsel grafikler sunan veri analizi projesi.

Python ile geliştirilmiş; farklı abone tiplerine göre kademeli su faturası hesaplayan, elde edilen verileri Pandas ile analiz eden ve Matplotlib kullanarak istatistiksel grafikler sunan kapsamlı bir veri analizi otomasyonudur.

### Proje Hakkında
Bu proje, kullanıcıdan alınan sayaç okuma değerleri (önceki/şimdiki) ve gün sayısı üzerinden su tüketimini (ton) hesaplar. Konut, İşyeri, Kamu Kurumu ve Turistik Tesis gibi farklı abone tipleri için belirlenmiş kademeli fiyat tarifelerini uygulayarak su tüketim ücreti, atık su ücreti ve KDV dahil toplam fatura tutarını belirler. Aynı zamanda toplanan veriler üzerinden çeşitli istatistiksel analizler (en yüksek tüketim, abone dağılımları, gelir oranları) yapar ve bunları görselleştirir.

### Öne Çıkan Özellikler
* **Kademeli Fiyatlandırma Algoritması:** Günlük ortalama su tüketimine göre (örneğin konutlar için 1., 2. ve 3. kademe) dinamik fatura hesaplama mantığı.
* **Veri Çerçevesi (DataFrame) Yönetimi:** Tüm abone verilerinin, hesaplamaların ve sonuçların Pandas kütüphanesi ile yapılandırılmış tablolarda tutulması ve işlenmesi.
* **Detaylı İstatistiksel Analiz:** Abone tipine göre yüzdelik dağılımlar, kademe sınırlarını aşan kullanıcı oranları, en yüksek fatura ödeyen aboneler ve kurumsal bazda toplam gelir/su tüketim raporlarının otomatik çıkarılması.
* **Veri Görselleştirme:** Matplotlib kullanılarak abone dağılımları (Pasta Grafiği) ve ücret/gelir analizleri (Sütun Grafikleri) için tekli ve çoklu (subplot) grafik ekranları oluşturma.

### Kullanılan Teknolojiler
* Python 
* Pandas, NumPy, Matplotlib, Sys

### Kurulum ve Çalıştırma
1. Proje dosyasını bilgisayarınıza indirin.
2. Terminal veya komut satırını açın.
3. Gerekli kütüphanelerin yüklü olduğundan emin olmak için şu komutu çalıştırın: `pip install pandas numpy matplotlib`
4. Programı başlatmak için dosya dizinindeyken `python TamamlanmışProje_1.py` komutunu çalıştırın.
5. Konsol üzerinden abone bilgilerini girerek fatura hesaplamalarını ve analizleri görüntüleyebilirsiniz.
