import pandas as pd
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
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
