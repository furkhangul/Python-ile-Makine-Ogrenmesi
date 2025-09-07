"""
YAPAY SİNİR AĞLARINDA KATMANLARLA XOR ve OR KAPILARI

1- OR KAPISI (VEYA Kapısı)
----------------------------
OR kapısı, doğrusal olarak ayrılabilir bir problemdir.
Yani, tek bir katmanla çözülebilir.

OR Kapısı Giriş-Çıkış Tablosu:
x1   x2   Y (x1 OR x2)
0    0    0
0    1    1
1    0    1
1    1    1

Yapay Sinir Ağı Yapısı:
- 1 Girdi Katmanı (2 nöron: x1 ve x2)
- 1 Çıktı Katmanı (1 nöron: y)
- Gizli katman GEREKMEZ.

Örnek Ağırlıklar:
w1 = 1
w2 = 1
bias = -0.5
Aktivasyon: Adım fonksiyonu (z > 0 → 1, z <= 0 → 0)

Çalışma:
z = w1*x1 + w2*x2 + b
y = step(z)

Örnek:
x1 = 1, x2 = 0 → z = 1*1 + 1*0 - 0.5 = 0.5 → y = 1 ✔


2- XOR KAPISI (ÖZEL VEYA Kapısı)
--------------------------------
XOR kapısı, doğrusal olarak AYRILAMAZ bir problemdir.
Yani, tek katmanlı bir yapay sinir ağı ile çözülemez.
Bu nedenle EN AZ 1 GİZLİ KATMAN gerekir.

XOR Kapısı Giriş-Çıkış Tablosu:
x1   x2   Y (x1 XOR x2)
0    0    0
0    1    1
1    0    1
1    1    0

Yapay Sinir Ağı Yapısı:
- 1 Girdi Katmanı (x1, x2)
- 1 Gizli Katman (2 nöron)
- 1 Çıktı Katmanı (1 nöron)

Ağın Öğrenme Mantığı:
Gizli katman, girdileri farklı şekillerde işler.
Çıktı katmanı, bu ara temsilleri birleştirerek XOR çıktısını üretir.

Basitleştirilmiş Ağırlık Örneği:
(Not: Bu sadece fikir vermek içindir.)

Gizli Katman:
h1 = sigmoid( w11*x1 + w12*x2 + b1 )
h2 = sigmoid( w21*x1 + w22*x2 + b2 )

Çıktı Katmanı:
y = sigmoid( v1*h1 + v2*h2 + b3 )

Burada:
- w11, w12, w21, w22: Girdi -> Gizli katman ağırlıkları
- v1, v2: Gizli -> Çıktı ağırlıkları
- b1, b2, b3: Bias terimleri

Neden Gizli Katman Gerekir?
Çünkü XOR verileri, tek bir düz çizgiyle ayırt edilemez.
Ancak gizli katman, bu verileri farklı bir düzleme taşıyarak doğrusal hale getirir.

Yani:
Tek katmanlı ağ (perceptron) → XOR'u öğrenemez 
En az 1 gizli katmanlı ağ → XOR'u öğrenir 


GENEL SONUÇ:
-------------
- OR gibi basit mantıksal kapılar tek katmanla öğrenilebilir.
- XOR gibi doğrusal ayrılmayan problemler en az bir gizli katman gerektirir.
Bu, yapay sinir ağlarında katmanların ne kadar önemli olduğunu gösterir.


"""
