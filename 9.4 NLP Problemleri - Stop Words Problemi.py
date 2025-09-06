import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

yorumlar = pd.read_csv('Restaurant_Reviews.csv', on_bad_lines='skip')


import re
yorum = re.sub('[^a-zA-Z]', ' ', str(yorumlar['Review'][0]))
yorum = yorum.lower()
#Ardından kelimeleri ayrımamız gerekiyor.
yorum = yorum.split()
"""
Bu bölümde artık kelimeleri tane tane ayırdığımız için noktalama gibi bi sorunda 
kalmadığı için kelimelerin anlamlarına bakma vakti geliyor.

Örnek olarak it kelimesi veya the kelimeleri İngilizcede pek bi anlam ifade etmiyor. 
Biz bu kelimeleri kullanmak yerine çıkarmamız daha doğru olacaktır.
Çünkü herhangi bir anlam katmamakta.
"""


#Bunun için nltk kütüphanesine ihtiyacımız var. Bu kütüphane her dil için stop word
#ifadelerini ayırır. Yani kendi içinde anlamsız kelimelerini bilip çıkarmamıza yardımcı oluyor.
import nltk
#Burada durma kelimelerini indiriyoruz. İngilizce için indirdik
durma =nltk.download('stopwords')
#Kendimiz de bir liste oluşturup ekleyebiliriz.

from nltk.stem.porter import PorterStemmer
#Nesne oluşturuyoruz.
ps = PorterStemmer()


