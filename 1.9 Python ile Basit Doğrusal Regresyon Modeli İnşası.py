"""
Python ile Basit Doğrusal Regresyon Modeli İnşası
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
"""
Neden ayırıyoruz:
verilerin 1/3 ünü testte sokarak makinenin öğrenmesini sağlıyoruz.
Eğer model hem öğrenir, hem de aynı veride test edilirse bu hile olur
"""
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
#Modeli eğitiyoruz. bak diyoruz  x_train yani öğrenilmiş aylardan y_traini ( öğrenilmiş satışları) arasındaki doğruyu bul
#Böylece başka bir ay verirsem, sen de bana tahmini satış değerini söyle.
lr.fit(x_train,y_train)

