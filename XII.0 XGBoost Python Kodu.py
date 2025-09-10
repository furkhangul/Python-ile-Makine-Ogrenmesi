from pickletools import optimize

import pandas as pd
import xgboost
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


#kütüphaneyi indirdik fakat kurulumu daha yapamadık.
import xgboost as xgb
classifier = xgboost.XGBClassifier()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
