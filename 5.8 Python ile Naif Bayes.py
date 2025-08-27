import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veriler = pd.read_csv('veriler.csv')

# Bağımsız ve bağımlı değişkenler
x = veriler.iloc[:, 1:4].values
y = veriler.iloc[:, 4].values

# Verilerin eğitim ve test olarak bölünmesi
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

# Ölçeklendirme
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Lojistik Regresyon
from sklearn.linear_model import LogisticRegression
log_r = LogisticRegression(random_state=0)
log_r.fit(x_train, y_train)

y_pred = log_r.predict(x_test)
print("Lojistik Regresyon Tahminleri:", y_pred)
print("Gerçek Değerler:", y_test)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Lojistik Regresyon Confusion Matrix:", cm)

# KNN ile Sınıflandırma
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
knn.fit(x_train, y_train)

y_pred_knn = knn.predict(x_test)
cm_knn = confusion_matrix(y_test, y_pred_knn)

print("KNN Confusion Matrix:", cm_knn)

#SCV KULLANIMI:
from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(x_train,y_train)

y_pred = svc.predict(x_test)
cm = confusion_matrix(y_test,y_pred)

print("SVC için sonuçlar: ",cm)


#Çoklu Kernel
from sklearn.svm import SVC
#rbf, poll, sigmouid veya linear kullanılabilir.
#Kernel oluştururken aslında buradan bashediliyor.
svc = SVC(kernel='linear')
svc.fit(x_train,y_train)

#Naif Bayes Kullanımı
#Gaussian Kullanıyoruz.
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train,y_train)
y_pred=gnb.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print("GNB için sonuçlar: ",cm)
