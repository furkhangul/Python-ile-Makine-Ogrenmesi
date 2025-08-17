"""
P-Value(Olasılık Değeri)
h0: farksızlık hipotezi, sıfır hipotezi, boş hipotez
h1: alternatif hipotez
p-değeri:olasılık değeri 0.05 alınır genelde
p değeri küçüldükçe h0 hatalı olma ihtimali artar
p değeri büyüdükçe h1 hatalı olma ihtimali artar

Mesela bi deney yapıyorum ve deneyde yeni ilaç eskisinden etkili mi diye kontreol edecem.
Bunun için hipotez testki kullanılır.

h0 testi:
Her şey olduğu gibi devam ediyor der.
Hiçbir fark yoktur der.
Yeni ilaç eski ilaçtan farklı değildir der.

h1 testi:
Hayır yeni ilaç daha farklı der.
Yeni ilaç daha etkilidir gibi bir iddiada bulunur.

biz de deney yapıyoruz ve elimize p değeri çıkıyor.
p değeri h0 doğru gibi düşünüldüğünde, bizim elimizdeki verilerin ortaya çıkma olasılığıdır.



p < 0.05  h₀ reddedilir.
p ≥ 0.05  h₀ reddedilemez.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("veriler.csv")
