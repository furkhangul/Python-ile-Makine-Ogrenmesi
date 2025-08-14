from mysqlx.expr import x_test
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
#Yeni kütüphane: belli satıra bölme
from sklearn.model_selection import train_test_split
# CSV'yi oku
veriler = pd.read_csv('eksikveriler.csv')

#Eksik sayısal verileri ortalama ile doldurma işlemi
istatistik = SimpleImputer(missing_values=np.nan, strategy='mean')
sayisal_sutunlar = veriler.select_dtypes(include=[np.number]).columns
veriler[sayisal_sutunlar] = istatistik.fit_transform(veriler[sayisal_sutunlar])

print(veriler)

#Kategorik verileri OneHotEncoder ile dönüştürme
ohe = OneHotEncoder(sparse=False)  # sparse=False ile doğrudan numpy array verir
ulke_encoded = ohe.fit_transform(veriler[['ulke']])  # 0. sütunu veya 'ulke' adı ile al

# Kolon isimlerini otomatik al
ulke_df = pd.DataFrame(ulke_encoded, columns=ohe.get_feature_names_out(['ulke']))
print( ulke_df)

#Sayısal veriler
sayisal_df = veriler[['boy', 'kilo', 'yas']].copy()
print(sayisal_df)

#Cinsiyet
cinsiyet = veriler[['cinsiyet']].copy()
print(cinsiyet)

#Tüm parçaları birleştir
toplam = pd.concat([ulke_df, sayisal_df, cinsiyet], axis=1)
print(toplam)


#Verieri bölmek için:

# Veriyi eğitim ve test olarak bölme
# train_test_split -> veriyi ikiye böler
# test_size=0.33 → verilerin %33'ü test seti, %67'si eğitim seti olarak ayrılır
# random_state=0 → aynı bölmeyi tekrar edebilmek için sabit bir rastgelelik sağlar
# DİKKAT: Burada 'toplam' hem X (bağımsız değişken) hem de y (bağımlı değişken) olarak kullanılıyor.
# Doğru kullanım için cinsiyet sütununu y olarak ayırmak gerekir.
x_train, x_test, y_train, y_test = train_test_split(toplam, test_size=0.33, random_state=0)
