"""
KNN Algoritmasında k Değeri Neye Göre Belirlenir

KNN algoritmasında k, yani komşu sayısı, modelin tahmin yaparken kaç komşuya bakacağını belirler. 
Bu sayı doğrudan modelin doğruluğunu ve genelleme gücünü etkiler.

k değeri küçük seçilirse:
- Model veriye çok duyarlı olur
- Gürültülü verilerden fazla etkilenir
- Aşırı öğrenme riski artar

k değeri büyük seçilirse:
- Model daha yumuşak karar sınırları çizer
- Bazı sınıflar baskın hale gelebilir
- Az öğrenme (underfitting) olabilir

Genelde tek sayı olarak seçilir çünkü oy çokluğunda eşitliği önler.

k nasıl seçilir:
- Veri kümesinin büyüklüğüne göre değişir
- Genelde sqrt(n) yani örnek sayısının karekökü başlangıç noktası olabilir
- Farklı k değerleri denenerek en iyi sonucu veren seçilir
- Cross validation ile en uygun k bulunabilir

Doğru k değeri için deneysel deneme ve çapraz doğrulama en etkili yoldur.
"""
