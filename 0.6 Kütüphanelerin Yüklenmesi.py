"""
Makine öğrenmesinde, makinenin veriyi anlayabilmesi ve çözümleyebilmesi
için sürekli verileri yutması yani bir sürü veriyi birleştirip konu hakkınnda
bilgi sahibi olması gerekmektedir.

Bunun için makine öğrenmesinin en temel basamağı olan veri yükleme adımı
devreye giriyor.

Veriyi yüklemek için kütüphaneler kullanılır.
En popülerleri ise Numpy ve pandas gibi kütüphanelere ihtiyaç duyarız.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Basit kod mantığında önce kütüphaneler bulunur ardından kütüphaneler ile 
gelen komutlar kullanılır.
Bu kodları da kendi arasında ikiye ayırabiliriz.
Veri yükleme adımı ve veri ön işleme adımı olarak. 
"""
#csv dosyasını okumak için read_csv kullanılır aynı şekilde json olsyadı read_json olurdu.
veriler = pd.read_csv('veriler.csv')
#Pandas sayesinde dataframe gibi kullanabiliyoruz.
#İndex ile istediğimiz verileri çağırabiliyoruz. Bu da çok büyük bi avantaj.
kilo = veriler[['kilo']]
print(kilo)

boyvekilo = veriler[['boy', 'kilo']]
print(boyvekilo)
