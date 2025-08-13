"""
Python'da OOP uygulamaları
class ve liste örneği
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Class kullanımına bir örnek
class yetenek:
    can = 120
    def kalancan(self, hasar):
        return self.can - hasar

buyucu = yetenek()
print(buyucu.can)
print(buyucu.kalancan(150))


#Listeleme işlemleri

list1 = [1,3,5,7,9]
#Diziye çeviriyoruz
liste = np.array(list1)
print(liste)
