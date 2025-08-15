"""
Python ile Basit Doğrusal Regresyon Görselleştirilmesi
"""
import pandas as pd
from sklearn.model_selection import train_test_split
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

#görselleştirme için:
import matplotlib.pyplot as plt
plt.plot(x_train,y_train)


"""
Bu şekilde görselleştirildiği zaman salak saçma bir görsel ve grafik elde ederiz
Bunu düzeltme adına sıralama yapmamız gerekmektedir.
"""
#pandas fonksiyonu sıralamaya çalışır
x_train = x_train.sort_index()
#indexe göre sıralandığından her bir ayın ilgili satış miktarını alıyoruz yani hepsi büyükten küçüğe sıralanmıyor.
y_train = y_train.sort_index()

plt.plot(x_train,y_train)

"""
Artık veriler daha düzenli ve tek çizgi halinde gösterilmektedir.
"""

#Dosdoğru çizgiyi tam olarak gösterir.
plt.plot(x_test,lr.predict(x_test))

#görüntü işlemeden kalan kod, gösterim alır.
plt.show()
