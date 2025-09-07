import pandas as pd
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sklearn
yorumlar = pd.read_csv('Restaurant_Reviews.csv', on_bad_lines='skip')

stop_words = set(stopwords.words('english'))

ps = PorterStemmer()

derlemelerim = []

# Yorum sayısını 1000 ile sınırlıyoruz
for i in range(min(1000, len(yorumlar))):

    yorum = re.sub('[^a-zA-Z]', ' ', str(yorumlar['Review'][i]))  # i'yi dinamik hale getirdik
    yorum = yorum.lower()
    yorum = yorum.split()
    yorum = [ps.stem(kelime) for kelime in yorum if kelime not in stop_words]  # Stopwords'leri çıkar ve stemle
    yorum = ' '.join(yorum)
    derlemelerim.append(yorum)


print(derlemelerim)

"""
Geçen bölümlerde NLP'de veri ön işleme kısmını teşkil ediyordu.
Bu bölümde ise Öznitelik Çıkarımı bölümüde ise kelime sayıları, featuring engineering, kelime
grupları, Ngram gibi noktaları çözümleyeip artık makine öğrenmesine hazır hale getirmiş olacağız.
"""
#Kütüphane yüklemeleri için
from sklearn.feature_extraction.text import CountVectorizer
#Max_features: makisimum alınacak veri.
cv = CountVectorizer(max_features=2000)
x = cv.fit_transform(derlemelerim).toarray()
y = yorumlar.iloc[:, 1].values

#Artık makine öğrenmesi bölümüne geçiyoruz.

from sklearn.preprocessing import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#Navies Baye kullanıldı
from sklearn.naive_bayes import MultinomialNB
gnb = MultinomialNB().fit(x_train, y_train)

y_pred = gnb.predict(x_test)

from sklearn import metrics
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)
