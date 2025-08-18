
import pandas as pd


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

#Verilerin eğitimi ve tesi için bölünmesi
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(toplam2,cinsiyet, test_size=0.33, random_state=0)

#Lineer model gibi benzer model ile öğretme
from sklearn.linear_model import LinearRegression
regresser = LinearRegression()
regresser.fit(x_train,y_train)

#Öğrenmeye girmeyen %66lık veriyi derliyoruz.
y_pred = regresser.predict(x_test)
print("Sonuç:",y_pred)


#Şimdi elimdeki boy verisini makineye tahmin ettirmek istiyorum.
#Bunun için sol ve sağa ayırarak boyu çekmek ve hemen ardından tahminlere başlamak.

boy = toplam2.iloc[:,3:4].values
sol = toplam2.iloc[:,:3]
sag = toplam2.iloc[:,4:]

birlestir = pd.concat([sol,sag], axis=1)

#Şimdi öğretme zamanı :
x_train,x_test,y_train,y_test = train_test_split(birlestir,boy, test_size=0.33, random_state=0)

regresyon = LinearRegression()
regresyon.fit(x_train,y_train)
#Makineden tahmin istiyoruz.
y_pred = regresyon.predict(x_test)
print(y_pred)
