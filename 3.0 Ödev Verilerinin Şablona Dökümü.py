"""
Odev: Kendi Makine Öğrenmesi programını yazmak
"""
import pandas as pd
import numpy as np

veriler = pd.read_csv("odev_tenis.csv")
#print(veriler)

#Numeric verileri ayırıyoruz.
NumericVeriler =  veriler.iloc[:,1:3].values


#Verileri Numeric hale çevirme:
outlooks = veriler.iloc[:,0:1].values
from sklearn import preprocessing
ohe = preprocessing.OneHotEncoder()
outlooks =ohe.fit_transform(outlooks).toarray()


#rüzgar değerlerini de çevirecek olursak:
windys = veriler.iloc[:,3:4].values
windys = ohe.fit_transform(windys).toarray()


#Oyananıp oynanmadığını da çevirecek olursak:
plays = veriler.iloc[:,4].values
plays = plays.reshape(-1,1)
plays = ohe.fit_transform(plays).toarray()


#DataFrame Haline Getirme
birinci = pd.DataFrame(data=NumericVeriler, index=range(14),columns=['Sıcaklık', 'Nem Oranı'])
ikinci = pd.DataFrame(data=outlooks, index=range(14), columns=['Kapalı','Yağmurlu','Güneşli'])
ucuncu = pd.DataFrame(data=windys[:,1].reshape(-1,1), index=range(14), columns=['Rüzgar var mı?'])
dorduncu = pd.DataFrame(data=plays[:,1].reshape(-1,1), index=range(14), columns=['Oynandı mı ?'])

#Birleştirmeye başlıyoruz.
toplam1 = pd.concat([birinci,ikinci], axis=1)
toplam2 = pd.concat([toplam1,ucuncu], axis=1)
toplam = pd.concat([toplam2,dorduncu], axis=1)
print(veriler)
#Tamamını okumak için to_string kullanılılyordu unutma.
print(toplam.to_string())

