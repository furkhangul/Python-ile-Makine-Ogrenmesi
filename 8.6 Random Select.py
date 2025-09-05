"""
Rastgele yakalama,bandit probleminde her seferinde kollardan (arms) tamamen rastgele
birini seçmeyi amaçlayan basit bir yöntemdir.

Bu stratejide, önceden edinilmiş bilgi dikkate alınmaz. Her kolun seçilme olasılığı eşittir.

Avantajı ise uygulaması çok basittir.

Dezavantajı: öğrenme gerçekleşmez, iyi kolların farkı anlaşılmaz, zamanla ödül ortalaması düşük kalır.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

# Random Selection (Rasgele Seçim)
'''
import random

N = 10000
d = 10 
toplam = 0
secilenler = []
for n in range(0,N):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    toplam = toplam + odul


plt.hist(secilenler)
plt.show()
'''
