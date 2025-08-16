"""
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


geçen derste aylar ve satışlar arasında doğrusal problemi çözüyorduk fakat burada birden fazla problem olmaktadır.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("veriler.csv")
