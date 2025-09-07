"""
Aktivasyon Fonksiyonları:

Sinir ağlarının doğrusal olmayan ilişkileri öğrenebilmesi için aktivasyon fonksiyonlarına ihtiyaç vardır.
Hemen hemen bütün fonksiyyonları kullanılabilir ama bazıları daha çok kullanılır.
Bazı yaygın aktivasyon fonksiyonları şunlardır:

1-Sigmoid:
Herhangi bir sayıyı 0 ile 1 arasına sıkıştırır.
Genellikle binary sınıflandırma problemlerinde kullanılır.
a)step function
Nörondan 0 veya 1 gelir ve bu sayede s şeklinde grafik oluşturuluyor.

b)S function
step function dan farklı olarak 1  ve 0 dan farklı veriler de verebiliyor.
σ(z) = 1 / (1 + e^(-z))

2-düzleştirilmiş fonksiyon
Negatif değerleri 0 olarak alırken. Artan pozitif değerlere göre 45 derecelik
açı ile değerleri sıra ile verir.

3-hiperbolik tanjant
sigmoid e benzer - değerler de vermektedir. Farklı yönleri mevcuttur.

Aktivasyon fonksiyonları derin öğrenmede çok fazla önemlidir. 
Yapay kavramların temelini oluşturur. 
Doğruluğu değiştirir.
"""
