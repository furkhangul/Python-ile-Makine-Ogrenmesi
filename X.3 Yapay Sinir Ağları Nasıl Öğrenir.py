"""
Gerçek bir örnekte bunu deneyecek olursak.
boy ve kilo girdilerinin olduğu bir örnekte.
Boy * W1 + Kilo * W2 = Z
Eşik değeri T olan bi nöronda
Z değeri > T değerinden ve T => Erkek olur.
Z değeri < T değerinden ve T => Kız olur.

Eğer bu değeler XOR örneğinde olduğu gibi tek bölüt ile iki parçaya ayrılmayıp
en az 2 vektöre ihtiyaç duyuyorsak farklı T değerleri olabilir.

Bu dersteki amacımız:
Yapay sinir ağı nasıl öğrenir ?
En temel öğrenme modeli Algılama modelidir.

Algılayıcı, en basit yapay sinir ağı modelidir.
Bir giriş katmanı, bir ağırlık (weight), bir toplama işlemi (Z değeri) ve
bir aktivasyon fonksiyonu (eşikleme) içerir.

Z = Boy × W₁ + Kilo × W₂

Buradaki:
Boy ve Kilo → Girdiler
W₁ ve W₂ → Bu girdilere ait öğrenilen ağırlıklar
Z → Girdiler ile ağırlıkların çarpımının toplamı
T (threshold) → Eşik değeri, karar fonksiyonunu belirler

Eğer Z > T → Erkek
Eğer Z < T → Kız

Bu, doğrusal bir karar sınırı oluşturarak iki sınıfı ayırmak anlamına gelir.

Ama XOR problemi gibi problemler, doğrusal olarak ayrılabilir olmayan problemdir.
Tek bir algılayıcı (perceptron) yeterli değildir.
En az iki gizli katmanlı yapıya ihtiyaç vardır.
Bu, çok katmanlı algılayıcı fikrinin temelini oluşturur.
"""
