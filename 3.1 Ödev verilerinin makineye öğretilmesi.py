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
le = preprocessing.LabelEncoder()
windys = veriler.iloc[:,3:4].values
windys = le.fit_transform(windys)


#Oyananıp oynanmadığını da çevirecek olursak:
plays = veriler.iloc[:,4].values
plays = le.fit_transform(plays)


#DataFrame Haline Getirme
birinci = pd.DataFrame(data=NumericVeriler, index=range(14),columns=['Sıcaklık', 'Nem Oranı'])
ikinci = pd.DataFrame(data=outlooks, index=range(14), columns=['Kapalı','Yağmurlu','Güneşli'])
ucuncu = pd.DataFrame(data=windys, index=range(14), columns=['Rüzgar var mı?'])
dorduncu = pd.DataFrame(data=plays, index=range(14), columns=['Oynandı mı ?'])

#Birleştirmeye başlıyoruz.
toplam1 = pd.concat([ikinci,ucuncu], axis=1)
toplam2 = pd.concat([toplam1,dorduncu], axis=1)
toplam = pd.concat([toplam2,birinci], axis=1)
#Tamamını okumak için to_string kullanılılyordu unutma.
#print(toplam.to_string())

#sadece nem oranı bağımsız olduğundan ayrımamız gerekmektedir
#Verilerin test için bölünmesi:
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(toplam.iloc[:,:-1],toplam.iloc[:,-1:], test_size=0.33, random_state=0 )

from sklearn.linear_model import LinearRegression
regresyon = LinearRegression()
regresyon.fit(x_train,y_train)

#Test etme
y_pred = regresyon.predict(x_test)

print(y_pred)

