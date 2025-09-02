import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veriler = pd.read_csv('musteriler.csv')

x = veriler.iloc[:, 2:4].values # -> yaş ve hacim

#kmeans kullanma
from sklearn.cluster import KMeans
#küme sayısı ve kullanılan yöntem
kmeans = KMeans(n_clusters=3, init ="k-means++")
kmeans.fit(x)

print(kmeans.cluster_centers_)

#Sürekli sonuçları döndürerek en doğru eleman sayısını seçmemize yardım eder.
sonuclar = []
for i in range(1,10):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=100)
    kmeans.fit(x)
    sonuclar.append(kmeans.inertia_)

plt.plot(range(1,10),sonuclar)
plt.show()
