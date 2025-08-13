"""
Verilerin import edilme aşamaları farklı olabilir. Bunun için json veya csv dosylarına aktarıp bunun 
üzerinden verileri pandas yardımı ile makineye aktarmak mümkündür.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#csv dosyasını okumak için read_csv kullanılır aynı şekilde json olsyadı read_json olurdu.
veriler = pd.read_csv('veriler.csv')
#Pandas sayesinde dataframe gibi kullanabiliyoruz.
#İndex ile istediğimiz verileri çağırabiliyoruz. Bu da çok büyük bi avantaj.
kilo = veriler[['kilo']]
print(kilo)

boyvekilo = veriler[['boy', 'kilo']]
print(boyvekilo)
