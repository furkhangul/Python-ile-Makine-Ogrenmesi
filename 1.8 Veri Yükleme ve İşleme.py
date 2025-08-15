"""
Veri Yükleme ve İşleme
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
x_test = sc.transform(x_test)

print("\nx_train (ölçekli):\n", x_train)
print("\nx_test (ölçekli):\n", x_test)
