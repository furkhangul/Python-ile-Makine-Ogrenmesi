import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veriler = pd.read_csv('musteriler.csv')

x = veriler.iloc[:, 2:4].values

#Hiyeraşik Bölütleme
from sklearn.cluster import AgglomerativeClustering

ac = AgglomerativeClustering(n_clusters= 3, metric='euclidean', linkage="ward")
y_tahminleri = ac.fit_predict(x)
#0 , 1 , 2 olmak üzere hangi kümede olduğunu gösterir.
print(y_tahminleri)

plt.scatter(x[y_tahminleri == 0,0],x[y_tahminleri==0,1], s=100, c='red')
plt.scatter(x[y_tahminleri == 1,0],x[y_tahminleri==1,1], s=100, c='green')
plt.scatter(x[y_tahminleri == 2,0],x[y_tahminleri==2,1], s=100, c='blue')
plt.show()

#Dendogra
