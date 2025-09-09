from pickletools import optimize

import pandas as pd
from tensorflow.python.keras.saving.saved_model.load import metrics

veriler = pd.read_csv('Churn_Modelling.csv')
#Burada öğrenilmesi gerekilmeyen isim, id ve indexi aşırı öğrenmeyi
#tetikleyebileceğinedn bu kolonları kaldırmamız daha iyi olacaktır.
x = veriler.iloc[:, 3:13].values
#Burada bankada 10 yıl içerisinde bankayı bırakıp bırakmadığımızı öğrenmek istiyoruz.
y = veriler.iloc[:,13].values

#Encoding yapılması gerekiyor.
from sklearn.preprocessing import LabelEncoder
#Ülkeler için
le = LabelEncoder()
x[:,1] = le.fit_transform(x[:,1])
#Kadın erkek için
le2 = LabelEncoder()
x[:,2] = le2.fit_transform(x[:,2])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ohe = ColumnTransformer([('ohe', OneHotEncoder(dtype=float),[1])])
x[:,1] = ohe.fit_transform(x[:,1])
x = ohe.fit_transform(x)
x = x[:,1:]

#Verilerin Eğitimi ve Test Edilmesi
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#Artık yapay sinir ağı oluşturuyoruz.
from keras.models import Sequential
#Yapay sinir ağını oluşturacağımız nesne için
from keras.layers import Dense

classifier = Sequential()
#Units: kaç nöron olacağı //Elimizde 11 eleman oluğundan yarısı diyoruz üçgen olsun diye
#Activation:None -> Aktivasyon fonksiyonunun olup olmayacağı
#use_baes: Baes fonksiyonu kullanılıp kullanılmayacağını
#İnit: katmandaki ağırlıkların nasıl başlatılacağını (initialization) belirler.
#input_dim: başlangıçta kaç girdi olduğunu veriyoruz

#Burada 6 nörondan oluşan bi katman oluşturduk.
classifier.add(Dense(units=6, init='uniform',activation='relu',input_dim=11 ))
#İkinci bir katman daha oluşturuyoruz. Sınıfa bu katman da ekleniyor. BU katman gizli katman
classifier.add(Dense(units=6, init='uniform',activation='relu'))

#Çıkış katmanını yapmamız için:
#Sigmoid aktivasyon fonkisyonu kullanılır.
classifier.add(Dense(units=1, init='uniform',activation='sigmoid'))

#Artık Nöron sistemini oluşturduk artık nasıl çalışacağını python üzerine getimemiz gerekiyor.
#adam yöntemi sktatic grand yönteminin bir parçasıdır.
#Optimize fonksiyonunun yenilenmesini sağlar.
classifier.compile(optimizer='adam', loss='binary_crosstropy', metrics=['accuracy'])

#epochs: kaç defa öğrenmesi gerektiğini ifade ediyor.
classifier.fit(x_train, y_train, batch_size=32, epochs=50)

y_pred = classifier.predict(x_test)

#0.5 ALTINDA İSE DOĞRU DEĞİLSE YANLIŞ DÖNDÜRÜR.
Y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
