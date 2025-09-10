"""
Uçtan Uca CNN Süreci

CNN modeli oluşturup, eğitip, test ederek bir görüntü sınıflandırma problemi nasıl çözülür adım adım:

1 Veri Hazırlığı
Görüntüleri etiketleriyle birlikte topla veya hazır veri seti kullan
Görüntüleri uygun boyuta yeniden boyutlandı
Piksel değerlerini ölçeklendir (0-1 arası gibi)
Veriyi eğitim ve test olarak ayır

2 Model Mimarisi Kurma
Convolution katmanları ile özellik çıkarma başlar
ReLU aktivasyonları ile doğrusal olmayanlık eklenir
Pooling katmanları ile boyut küçültülür, önemli özellikler korunur
Katmanlar birkaç kez tekrarlanabilir
Flatten katmanı ile 2D veriyi 1D vektöre çevir
Fully connected (Dense) katmanlarla sınıflandırma yapılır
Son katman softmax aktivasyonuyla sınıf olasılıkları verir

3 Modeli Derleme
Kayıp fonksiyonu seç
Optimizasyon algoritması seç (Adam yaygın tercih)
Performans metriği belirle (accuracy sıklıkla kullanılır)

4 Model Eğitimi
Eğitim verisiyle model fit edili
Epoch sayısı ve batch size belirlenir
Validation set ile aşırı öğrenme kontrol edilir

5 Model Değerlendirme
Test verisi ile modelin performansı ölçülür
oğruluk, loss gibi metriklere bakılır
Gerekirse hiperparametre ayarı yapılır

6 Model Kullanımı
Yeni görüntüler için model tahmin yapar
Sınıf olasılıkları veya etiketler elde edilir

7 Model Kaydetme
Eğitilen model dosyaya kaydedilir
Daha sonra yüklenip kullanılabilir

Özetle uçtan uca CNN süreci veri hazırlığı, model oluşturma, eğitim, değerlendirme ve kullanım aşamalarından oluşur.
Her aşama dikkatli planlanmalı ve optimize edilmelidir.
"""
