import pandas as pd
import numpy as np

veriler = pd.read_csv('maaslar.csv')

"""
Polinom Regresyon:
Polinom regresyon, doğrusal regresyonuun genelleştirilmiş bir halidir. Değişkenler
arasında doğrusal olmayan ilişkileri modellemek için kullanılır.

Basit Doğrusal REG.:
Bir bağımlı değişken ve bir bağımsız değişken arasındaki doğrusal ilişkiyi modelleyen
yöntemdir.
Y = B0 + B1 * X + £

Çoklu Doğrusal Reg.:
Birden fazla bağımsız değişkeni  bir bağımlı değişkenn üzerindeki etkisini inceleyen
modeldir.
Y = B0 + B1 * X1 + B2 * X2 + ..... + Bn * Xn + £

Polinom Reg.:
Bağımlı değişken ile bir ya da birkaç bağımsız değişkenin doğrusal olmayan ilişkilerini
modellemek için bağısmız değişkenin kuvvetlierini de modele dahil eden regresyon yöntemidir.

Y = B0 + B1 * X + B2 * X^2 + B3 * X^3 + B4 + X^4 + .... + Bn * X^n
Veya
Y = B0 + B1 * X1 * X2 + B1 * X1 + B2 * X^2 + B3 * X^3 + B4 + X^4 + .... + Bn * X^n
"""
  
