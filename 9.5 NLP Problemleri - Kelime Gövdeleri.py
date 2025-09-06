import pandas as pd
import re
yorumlar = pd.read_csv('Restaurant_Reviews.csv', on_bad_lines='skip')
import nltk
#Burada durma kelimelerini indiriyoruz. İngilizce için indirdik
durma =nltk.download('stopwords')


from nltk.stem.porter import PorterStemmer
#Nesne oluşturuyoruz.
ps = PorterStemmer()
from nltk.corpus import stopwords
yorum = re.sub('[^a-zA-Z]', ' ', str(yorumlar['Review'][0]))
yorum = yorum.lower()
yorum = yorum.split()

#Burada liste içerisindeki köklerini çıkarır.
#Burada her bir kelimenin kökünü alıp döngüde stopword içinde oolup olmadığını kontrol ediyor.
yorum = [ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words('english'))]

#Şimdi ise birleştirme işlemi gerçekleştiriyoruz.Boşluk koyarak
yorum = ' '.join(yorum)

