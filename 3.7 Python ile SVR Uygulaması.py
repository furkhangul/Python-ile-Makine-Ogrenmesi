"""
Python ile SVR Uygulaması
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Verileri yükleme
veriler = pd.read_csv("maaslar.csv")

#DataFrame hale getirme ( Bmölme )
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]

#Numpy array dönüşümü
X = x.values
Y = y.values

#LineerRegresyon - Doğrusal model oluşturma
from  sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,Y)

#Polinormal Regresyon - Doğrusal olmayan model oluşturma
#2.Dereceden polinom için:
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(X)
lr1 = LinearRegression()
lr1.fit(x_poly,y)

#4.Dereceden polinom için:
poly_reg1 = PolynomialFeatures(degree=4)
x_poly1 = poly_reg1.fit_transform(X)
lr2 = LinearRegression()
lr2.fit(x_poly1, y)

#Görselleştirme
plt.scatter(X,Y, color='red')
plt.plot(x, lr.predict(X), color='blue')
plt.plot(x, lr.predict(X), color='blue')
plt.show()

plt.scatter(X,Y, color='red')
plt.plot(x, lr1.predict(poly_reg.fit_transform(X)), color='blue')
plt.show()

plt.scatter(X,Y, color='red')
plt.plot(x, lr2.predict(poly_reg1.fit_transform(X)), color='blue')
plt.show()

#Tahmin
print(lr.predict([[11]]))
print(lr.predict([[6.6]]))

print(lr1.predict(poly_reg.fit_transform([[11]])))
print(lr1.predict(poly_reg.fit_transform([[6.6]])))

#Verileri ölçeklememiz gerektiğini geçen yazıda yazdık:
from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(Y)

#SVR Kodlanması
from sklearn.svm import SVR

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_olcekli,y_olcekli)
plt.scatter(x_olcekli,y_olcekli)

#Tahmin şablonu ise:
plt.plot(x_olcekli,svr_reg.predict(x_olcekli))
plt.show()


#Soralım bakalım:
print(svr_reg.predict([[11]]))
print(svr_reg.predict([[6.6]]))
