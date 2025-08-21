import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veriler = pd.read_csv('maaslar.csv')
#Bu bölümde daha önce kullandığımız veirlerin çoğunu kullanmaya ihtiyaç duymayacaz.

#EĞTİM SEVİYESİ VE MAAŞLARI AYRIMAK İSTİYORUZ. Ünvanlardan kurtulmuş olduk ayrıca

x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]

#Bu veriler doğrusal olarak ilişkilendirilecek veriler olmadığını biliyoruz fakat
#Yinede göstermek adına tekrardan lineer model üzerinde gösterecek olursak:
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lineer = lr.fit(x,y)

#scatter iki değişken arasındaki ilişkiyi göstermek için kullanılır.
#Regresyon analizinde, veri noktalarını dağılımını göstermek için çok yaygındır.
#Bu noktalar gerçek verilerin bilgileri
plt.scatter(x.values,y.values)

#Scatter noktalar ile gösterirken plot çizgi şeklinde veriyi görselleştirir.
#Bu çizgiler ise tahmin sonucu oluşan veriler.
plt.plot(x.values, lr.predict(x.values))


"""
Maaş ve eğitim seviyesi dümdüz çizgi ile ifade edilemiyor bundan dolayı polinom çizmemiz gerekmektedir.

"""

"""
Bu satırda kütüphaneyi import ediyoruz. Bu araç senin X verilerini polinom terimine dönüştürüyor.
x, x^2 , x^3 gibi verileri oluşturuyor.
"""
from sklearn.preprocessing import PolynomialFeatures

"""
X verisi sadece düz sayı iken yani 1, 2 ,3 gibi sayı iken bu koddan sonra x_poly verileri
1 x x^2
1 1 1
1 2 4
1 3 9
1 4 16 
şeklinde modeller bu sayede model hem x hem de x^2 ile tahmin yapabilir.
eğer Degree değerini yükselirsek x^4 'e kadar yapacağı için genellikle daha hassas sonuçları bulmamızı
sağlayacaktır.
"""
polinom_regresyonu_nesnesi = PolynomialFeatures( degree=2 )
x_poly = polinom_regresyonu_nesnesi.fit_transform(x.values)
print(x_poly)
"""
Bu kodda modeli eğitiyoruz. Yani 3 verirsek sonuç ne çıkar gibi veirileri kontrol
etmiesni sağlıyoruz.
"""
lr.fit(x_poly,y)

#Burada matploitlib üzerinden gerçek veriyi göstermeye çalışıyoruz ( noktalar ile )
plt.scatter(x,y)

"""
Öncelikle plot methodu matploitlib kütüphanesi ile öğrenilen veriyi göstermeye yarıyor ( çizgiler ile )

burada polinom_regresyonu_nesnesi.fit_transform(x.values) kodu bize yukarıda yaptığımız gibi
verileri x , x^2 gibi değerlerde modellememizi sağlıyor.

lr.predict methodu ise model polinom verilerine eğitilidği için bu X ve X^2 'yi alıp teahminler yapıyor.
Yani her x için, tahmin ettiği maaşı veriyor

en soldaki x ise zaten eğitim seviyesini veriyor.
"""
plt.plot(x,lr.predict(polinom_regresyonu_nesnesi.fit_transform(x.values)))


#Açılsın ve hemen kapanmasın diye
plt.show()
