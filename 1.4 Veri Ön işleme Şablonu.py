from mysqlx.expr import x_test
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



#Şablon temel fikri
veriler = pd.read_csv('eksikveriler.csv')

istatistik = SimpleImputer(missing_values=np.nan, strategy='mean')
sayisal_sutunlar = veriler.select_dtypes(include=[np.number]).columns
veriler[sayisal_sutunlar] = istatistik.fit_transform(veriler[sayisal_sutunlar])

print(veriler)

ohe = OneHotEncoder(sparse=False)  
ulke_encoded = ohe.fit_transform(veriler[['ulke']]) 

ulke_df = pd.DataFrame(ulke_encoded, columns=ohe.get_feature_names_out(['ulke']))
print( ulke_df)

sayisal_df = veriler[['boy', 'kilo', 'yas']].copy()
print(sayisal_df)

cinsiyet = veriler[['cinsiyet']].copy()
print(cinsiyet)

toplam = pd.concat([ulke_df, sayisal_df, cinsiyet], axis=1)
print(toplam)

x_train, x_test, y_train, y_test = train_test_split(toplam, test_size=0.33, random_state=0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

