"""
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
veriler = pd.read_csv("veriler.csv")
#print(veriler)

#Boy, Yaş ve Kilo ayırma

Diger = veriler.iloc[:,1:4].values

#Encoder: Kategorikten numerice çevirme kodları
#Ülke için
ulke = veriler.iloc[:,0:1].values
#print(ulke)
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
#print(ulke)
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
#print(ulke)

#Cinsiyet için
cinsiyet = veriler.iloc[:,4].values
#print(cinsiyet)
#iki boyutlu hale getirdik
cinsiyet = cinsiyet.reshape(-1, 1)
cinsiyet[:,0] = le.fit_transform(veriler.iloc[:,4])
cinsiyet = ohe.fit_transform(cinsiyet).toarray()
#print(cinsiyet)

#Şimdi dataframe haline getirecez birleştirme işlemleri için:

birinci =  pd.DataFrame(data=ulke, index=range(22), columns=['FR','TR','US'])
ikinci = pd.DataFrame(data=Diger, index=range(22), columns=['Boy', 'Kilo', 'Yaş'])
#Kukla veri olduğundan yalnızca tek bi sütun alıyoruz. Yoksa makine hatalı işlemeye başlar.
ucuncu = pd.DataFrame(data=cinsiyet[:,:1], index=range(22), columns=['Cinsiyet'])

#Verileri Topluyoruz:
toplam1 = pd.concat([birinci,ikinci], axis=1)
toplam2 = pd.concat([toplam1,ucuncu], axis=1)

print(toplam2)

