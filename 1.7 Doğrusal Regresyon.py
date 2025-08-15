"""
Doğrusal Regresyon

Doğrusal regresyon, istatistik ve makine öğrenmesinde en temel ve en yaygın kullanılan
yöntemlerden biridir. Amaç, bağımsız değişken(yani sonuç) ile bir veya birden fazla
bağımsız değişken (girdi) arasındaki doğrusal ilişkiyi modellemektir.

y = ax + b
y:bağımlı değişken
x:bağımsız değişken
a:katsayı
b:sabit sayı


Doğrusal regresyon ise

y = b0 + b1x + £
y: tahmin edilmek istenen değer (bağımlı değişken)
x: girdi verisi (bağımsız değişken)
b0: sabit sayı
b1: eğim (katsayı) - x'in y üzerindeki etkisini gösterir.
£: hata payı



Doğrusal Regresyonun Önemi:
1. Model çıktısı bir denklem olduğundan, hangi değişken sonucu nasıl etkilediği kolayca anlaşılır.

2.Diğer karmaşık modellere kıyasla az hesaplama gücü ister

3.Makine öğrenmesinin birçok gelişmiş modekin temelini oluşturur.

4.Overfitting riski düşüktür.


Yeri:
1.İlk öğrenilen makine öğrenmesi dilir.

2.Karmaşık modellerin eğitiminden önce referans model olarak kullanılır.

3.Büyük veir kümelerinde hızlı ve etkili bir başlangıç sağlar.

4.Özellikşe mühendisliği ve ilişki analizi için çok kullanışlıdır.


"""
import pandas as pd
import numpy as np

veriler = pd.read_csv('satislar.csv')
