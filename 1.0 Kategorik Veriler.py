"""
Veri Tipleri ve dönüşümleri

Verilerin yüklenmesinin ardından verinin farklı yapı ve tanımlar içerisine
girmesi istenebilmektedir.

Bunun için yapılması gereken şey verilerin dönüşümüdür.

Veri iki ana gruba ayrılır.

1) Kategorik Veriler
    Sayı değeri yerine kategori / sınıf bilgisini ifade eder.
    Matematiksel işlemler (toplama, çıkarma) anlamlı değildir.

    A) Nominal:
        Sıra veya büyüklük ilişkisi olmayan kategoriler
        Örnek: cinsiyet (erkek, kadın), ülke (TR, US, FR)
    B)Ordinal:
        Sıra ilişkisi olan kategoriler
        Örnek: eğitim seviyesi (ilkokul < lise < üniversite)
2) Sayısal Veriler
    Doğrudan sayı ile ifade edilen ve matematiksel işlemler yapılabilen veriler.

    A) Oransal:
        Tam sayılar şeklinde, sayılabilir değerler
        Örnek: öğrenci sayısı, araç sayısı
    B) Aralık:
        Belirli bir aralıkta sonsuz değer alabilen ölçümler
        Örnek: boy, kilo, sıcaklık


Makine Öğrenmesinde: Direkt olarak modele verilebilir, ancak ölçeklendirme yapılması gerekebilir.

Örnek olarak kız değerine 0 erkek değerine 1 dediğimiz zaman
sayılar sadece simge olarak tanımlayabildiğimiz ifadeler oluyor.
Büyüklük küçüklüğü ifade etmiyor.

"""

import pandas as pd
import numpy as np
from pycparser import preprocess_file
from scipy.constants import precision
#Python Interpreter ile scikit-learn araması yaptıktan sonra kütüphaneyi indirebiliyoruz.
from sklearn.impute import SimpleImputer
#Bu kütüphane eksik verileri otomatik olarak doldurmak için kullanılır.


veriler = pd.read_csv('eksikveriler.csv')
istatistik = SimpleImputer(missing_values=np.nan, strategy='mean')
#Burada SimpleImputer ile nesne oluşturduk
#Missing_values ile eksik verileri aradık eksikler ise nan olanlar
#strategy ise strateji, bizim stratejimiz ortalama.

sayisal_sutunlar = veriler.select_dtypes(include=[np.number]).columns
#veriler.select_dtypes() bu kodda istediğimiz string, int değerlerini seçer
#.columns ise sütun isimlerini bir index olarak alır.

veriler[sayisal_sutunlar] = istatistik.fit_transform(veriler[sayisal_sutunlar])
#imputer.fit_transform(X) iki şeyi yapar:
#fit: Her sütun için doldurma istatistiğini (burada ortalama) hesaplar.
#transform: Hesaplanan ortalama ile NaN değerleri doldurur.
print(veriler)

#Şimdi buradaki verileri string yerine sayısal verilere dökecek olursak ( e: 0, k:1 gibi)

ulke = veriler.iloc[:,1:4].values
#iloc: intager location indexing -> satır ve sütunların index numarasına erişim
#iloc[satir_indexi, sutun_indexi]
#values ise saf veriye çevirir yani index göstermden yazar.

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
#LabelEncoder → Kategorik verileri (ör. "tr","use")
# sayısal etiketlere çevirir (0, 1, 2 gibi).
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

#ulke[:,0] yani 0.sütun yani ülkeler alınıyor.

#fit → Etiketleri öğrenir. Örn: ['fr', 'tr', 'us'] →
# sıralayıp sayılar atar: fr → 0, tr → 1, us → 2.

#transform → Bu haritayı kullanarak veriyi sayıya çevirir.
#Örn: ['tr', 'tr', 'us', 'fr'] → [1, 1, 2, 0]
print(ulke)


#Başka bir şekilde ise: maikne öğrenmesine uygun hale getiriyoruz.

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarry()
print(ulke)
