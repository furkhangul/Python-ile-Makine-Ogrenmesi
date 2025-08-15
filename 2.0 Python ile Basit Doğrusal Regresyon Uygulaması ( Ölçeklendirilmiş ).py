"""
Python ile Basit Doğrusal Regresyon Uygulaması
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#Verileri yükledim
veriler = pd.read_csv("satislar.csv")
print(veriler)
#ayrı ayrı çıkarıyoruz
aylar = veriler[['Aylar']]
satislar = veriler[['Satislar']]
print(aylar)
print(satislar)

#veya
satislar2 = veriler.iloc[:,:1].values
print(satislar2)

#Setlere ayırdık
x_train,x_test,y_train,y_test = train_test_split(aylar,satislar, test_size=0.33,random_state=0)

#Ölçekleme işlemi:
sc= StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
y_train = sc.fit_transform(y_train)
y_test = sc.fit_transform(y_test)

#Model oluşturma kütüphanesini import edecek olursak.
from sklearn.linear_model import LinearRegression
#Modelin nesnesini oluşturuyoruz.
lr  = LinearRegression()
#Modeli eğitiyoruz.
lr.fit(x_train,y_train)

#tahmin yapıyoruz.
#predict: tahmin
#x_test verileri makinenin hiç görmediği veriler bunu tahmin edecek x_train verilerine bakarak
tahmin =lr.predict(x_test)
print("tahmin:",tahmin)

