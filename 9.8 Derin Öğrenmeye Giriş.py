"""
Yapay Sinir Ağı, insan beyninin çalışma biçiminden esinlenerek oluşturulmuş bir makine
öğrenmesi modelidir. Bu ağlar, veriler arasındaki karmaşık ilişkileri öğrenmekte oldukça başarılıdır.
Bir sinir ağı, üç ana katmandan oluşur:
1-Girdi Katmanı
2-Gizli Katman(lar)
3-Çıktı Katmanı

Her katman, nöron adı verilen birimlerden oluşur.


**********************/*/*/*/*/*
Yapay Nöron (Neuron)
Bir yapay nöron, biyolojik bir nöronun basit bir matematiksel modelidir.
Aşağıdaki adımlarla çalışır:

1-Girdi ve Ağırlıklar:
Nöron, dışarıdan gelen birden fazla girdiyi (x₁, x₂, ..., xₙ) alır.
Her girdinin bir ağırlığı (w₁, w₂, ..., wₙ) vardır.
Ağırlıklar, öğrenme sürecinde ayarlanır.
z = w1 * x1 + w2 * x2 + . . . + wn * xn + b

burada b bir bias (sapma) terimidir.


2-Aktivasyon Fonksiyonu:
Bu toplam değer bir aktivasyon fonksiyonundan geçirilir.
Bu fonksiyon, nöronun “ateşleyip ateşlemeyeceğini” belirler.

3-Sinir Ağlarının Eğitimi:
Sinir ağları veri ile eğitilir. Eğitim süreci şu adımları içerir:

a-İleri Yayılım:
Girdi verisi ağdan geçer ve bir çıktı üretilir. Bu çıktı, nöronlar aracılığıyla katman katman hesaplanır. Her nöron, girdileri alır, ağırlıklarla çarpar, bias ekler ve aktivasyon fonksiyonundan geçirerek bir sonraki katmana iletir.

b-Hata Hesaplama:
Ağdan elde edilen çıktı ile gerçek değer karşılaştırılır. Bu fark, yani **hata (loss)**, genellikle bir kayıp fonksiyonu (örneğin, Ortalama Kare Hata - MSE veya Çapraz Entropi) kullanılarak hesaplanır.

c-Geri Yayılım :
Hesaplanan hata, ağda geriye doğru yayılır. Bu işlem sırasında zincir kuralı kullanılarak, her ağırlığın hataya olan katkısı hesaplanır.

d-Ağırlıkların Güncellenmesi:
Ağ, hatayı en aza indirmek için ağırlıkları günceller. Bu işlem genellikle **gradyan inişi (gradient descent)** adı verilen bir optimizasyon algoritması ile yapılır. Böylece model zamanla daha doğru tahminler yapmayı öğrenir.


**********************/*/*/*/*/*

Aktivasyon Fonksiyonları:

Sinir ağlarının doğrusal olmayan ilişkileri öğrenebilmesi için aktivasyon fonksiyonlarına ihtiyaç vardır. Bazı yaygın aktivasyon fonksiyonları şunlardır:

1-Sigmoid:
Herhangi bir sayıyı 0 ile 1 arasına sıkıştırır. Genellikle binary sınıflandırma problemlerinde kullanılır.
σ(z) = 1 / (1 + e^(-z))

2-Tanh :
Çıktıyı -1 ile 1 arasına sıkıştırır. Genellikle sıfır merkezli verilerde tercih edilir.
tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))

3-ReLU :
Pozitif değerleri olduğu gibi geçirir, negatifleri ise sıfırlar. Derin ağlarda en yaygın kullanılan fonksiyondur.
ReLU(z) = max(0, z)

4-Leaky ReLU:
ReLU’nun geliştirilmiş halidir. Negatif değerlerde küçük bir eğim sağlar, bu sayede ölü nöron problemini azaltır.




"""
