"""
Boyut İndirgeme ve PCA
- Görütnü Filtrelemede kullanılır
bazen görüntüler gürültülü olabiliyor. Burada görüntüyü filtreleyerek daha iyi bi
varyasyona çeviriyor
-Görselleştirmede kulllanılır.
Görselleştirilmesi zor ve mümkün olmayan görsellerin okunabilirliğini arttırıyor.
-Öznitelik Çıkarımı
Yeni öznitelik çıkarımlarının yapılması
-Öznitelik Ekleme /Çıkarma
-Borsa Analizi
-Sağlık Verileri / Genetik Veriler


Neden kullanılır:
Boyutları dönüştürmeye yardımcı oluyor.
Boyut indirgeme ( gereksiz boyulardan kurtulma veya bazı boyutları birleştirme)
Değişkenler arasındaki bağlantıları açığa çıkarma.

PCA Algoritması
1-İndirgenmek istenen boyut k olsun
2-Veri standartlaştırılır.
3-Kovaryans ve Korelasyon matrisinde öz değerleri ve öz vektörleri elde et.
Veya SVD kullan.
4-Öz değerleri büyükten küçüğe sırala ve k tanesini al.
5-Seçilen k özdeğerden W projeksyion matrsini oluştur.
6-Orijinal veri kümesi X'i W kullanarak dönüştür ve k-boyutlu Y uzayını elde et.

Özdeğer ve Özyöney
Rastgele bir matris alın.
Bu matris tek boyutlu bir matris ile çarparsak
Çarpım şayet çarpımın herhangi bir skala katını veriyorsa, bu skala öz değer,
bu vektör öz yöneydir.

"""
