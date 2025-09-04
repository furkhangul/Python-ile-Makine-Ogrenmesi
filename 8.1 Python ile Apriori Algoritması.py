#Apriori Algoritması

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Başlık olmadığını bildiriyoruz.
veriler = pd.read_csv('sepet.csv', header=None)


liste = []
#Toplam liste sayısı olacak bu da:
for i in range(0,7501):
    liste.append((str(veriler.values[i,j]) for j in range(0,20)))
from apyori import apriori
kurallar = apriori(liste,min_support = 0.01, min_confidince =0.2, min_left =3, min_length=2)
print(list(kurallar))
