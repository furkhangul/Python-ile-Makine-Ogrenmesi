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
