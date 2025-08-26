"""
KNN
Sınıflandırmada kullanılan bu algoritmaya göre sınıflandırma sırasında çıkarılan özelliklerden,
sınıflandırılmak istenen yeni bireyin daha önceki bireylerin k tanesine yakınlığına bakmasıdır.

Örnek olarak:
k 3 için yeni bir eleman sınıflandırmak istersek bu durumda eski sınıflandırılmış elemanlardan en yakın
3 tanesi alınır. Bu elemanlar hangi sınıfa dahilse, yeni eleman da o sınıfa
dahil edilir. Mesafe hesabında genellikle öklid mesafesi kullanılır.

Neden kullanılır:/
- Etiketli veri varsa ve yeni bir verinin hangi sınıfa ait olduğunu tahmin etmek istiyorsan kullanılır.
- Yeni veriye en yakın K tane komşuyu (örneğin: 3 en yakın komşu) bulur ve onların sınıfına göre
  tahmin yapar.
- Özellikle sınıflandırma problemlerinde çok kullanılır çünkü model eğitimi gerekmez — veriyi saklar ve
  tahmin anında işlem yapar.

Nasıl çalışır:
- Eğitim verisini bellekte tutar.
- Yeni bir veri geldiğinde, bu veriye olan uzaklığı (genellikle Öklid uzaklığı) tüm verilerle hesaplar.
- En yakın K tanesini seçer ve bunların sınıf çoğunluğuna göre karar verir (sınıflandırma) veya ortalamasını alır (regresyon).

KNN basit ama güçlüdür. Küçük ve temiz veri setlerinde iyi çalışır, parametresi azdır, yorumlaması kolaydır.
Ancak ölçekleme şarttır ve büyük veri için uygun değildir.
"""
