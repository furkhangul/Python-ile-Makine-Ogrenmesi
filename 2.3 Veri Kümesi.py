"""
Veri Kümesinin Tanımı.ç.

Çoklu Doğrusal Regresyon :
Çoklu doğrusal regresyon (Multiple Linear Regression), bir bağımlı değişkenin (yani tahmin
edilmek istenen değişkenin) birden fazla bağımsız değişken (yani açıklayıcı değişkenler) ile
ilişkisini modelleyen istatistiksel bir tekniktir.


Genel Denklem:

y= b0 + b1x1 + b2x2 + b3x3 + . . . + bnxn + £


y:Bağımlı değişken
X₁, X₂, ..., Xₚ: Bağımsız değişkenler
b0: Sabit terim
b1, b2, b3...bn: Bağımsız değişkenlerin katsayıları
£: Hata terimi

Basit Doğrusal Regresyon:

y = a + bx
y = a + bx + £

y: Bağımlı değişken
a: Sabit sayı
x:bağımsız değişken
£: hata oranı

geçen derste aylar ve satışlar arasında doğrusal problemi çözüyorduk fakat burada birden fazla problem olmaktadır.

"""


"""
İlk derste gördüğümüz boy, kilo ve yaş verilerini bu derste inceleyebiliriz.

y: a + b(kilo) +c(yaş) + d(ayakkabı no) + £
gibi bi denklem kurulabilir.

doğrusal tek boyutlu iken 3 değişkenli 3 boyutlu , 4 değişken 4 boyutlu...
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("veriler.csv")
