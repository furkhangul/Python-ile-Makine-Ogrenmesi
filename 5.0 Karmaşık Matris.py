"""
Karmaşık matris, elemanları karmaşık sayılardan (a + bi formunda) oluşan matristir.
Makine öğrenmesinde genellikle kullanılan veriler reel sayılardır, çünkü çoğu algoritma
gerçek sayı üzerinde çalışacak şekilde tasarlanmıştır.

Ancak bazı özel alanlarda, örneğin:

- Kuantum hesaplama,
- Sinyal işleme
- Görüntü işleme
- Radar ve telekomünikasyon uygulamaları

gibi yerlerde veriler doğal olarak karmaşık sayılar içerir. Bu durumda kullanılan veri matrisleri de
karmaşık matris olur.

Karmaşık matris, normal matristen farklı işlemler gerektirir:
- Karmaşık eşlenik transpoz,
- Üniter matris,
- Kompleks özdeğerler gibi kavramlar önem kazanır.

Karmaşık matris, genel makine öğrenmesi modellerinde Bu tür modeller karmaşık sayı desteği sunmaz. Eğer verin karmaşık sayı içeriyorsa,
önce reel ve sanalkısımları ayırıp yeni özellikler olarak modele vermen gerekir.
Karmaşık matris makine öğrenmesinde yaygın değildir, ama bazı teknik veya fiziksel uygulamalarda
olmazsa olmazdır.
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


veriler = pd.read_csv('veriler.csv')

x = veriler.iloc[:,2:4].values
y = veriler.iloc[:,4].values

#Verilerin eğitimi ev test için bölünmesi:
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=0)

#Verinin ölçeklendirilmesi
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#Lojistik Regression
from sklearn.linear_model import LogisticRegression
log_r = LogisticRegression(random_state=0)
log_r.fit(x_train,y_train)

y_pred = log_r.predict(x_test)
print(y_pred)
print(y_test)


#Confusion Matris oluşturma
from  sklearn.metrics import confusion_matrix
cm = confusion_matrix(x_test,y_pred)
print(cm)
