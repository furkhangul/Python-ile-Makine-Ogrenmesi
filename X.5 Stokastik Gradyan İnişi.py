"""
Stokastik Gradyan İnişi

Daha önce gradyan inişi ile ağırlıkların, hata fonksiyonuna göre nasıl güncellendiğini öğrendik.
Ancak bu işlemi tüm eğitim verisi üzerinde yapmak  pahalı ve yavaştır.

Çözüm ise verileri küçük parçalara ayırmak. Daha hızlı, daha sık güncelleme

İşte burada "Stokastik" Gradyan İnişi devreye girer.

Stokastik kelimesi : Rastlantısal, örnek bazlı anlamına gelir.

SGD, her bir eğitim örneği (ya da küçük bir örnek grubu) için ağırlıkları ayrı ayrı günceller.

Örnek:
Veri kümesi: 1000 veri
Batch Gradient Descent -> Tüm 1000 veri ile bir kerede güncelleme
SGD -> Her bir veri için tek tek güncelleme yapar

Avantajları:
- Daha hızlı öğrenme (özellikle büyük veri setlerinde)
- Yerel minimumlardan çıkabilir (çünkü her adım biraz rastgele)
- Daha az hafıza kullanımı

Dezavantaj:
- Ağırlıklar her adımda biraz sallanır (gürültülü öğrenme)
- Doğru öğrenme oranı ayarlanmazsa, model kararsız olur

kısaca,
1. Stokastik = Rasgele = Tek veriyle öğrenme
2. Daha hızlı, daha az maliyetli
3. Büyük veri setleri için idealdir
"""
