import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Hatalı verileri geçmesini istedik
yorumlar = pd.read_csv('Restaurant_Reviews.csv', on_bad_lines='skip')

#Büyük küçük harf olması NLP için anlam ifade etmez fakat makine bunu farklı veri olarak algılar.
#Burada büyük harfleri küçük harfler ile değiştirerek bu yazıları eşitliyoryuz.

import re
yorum = re.sub('[^a-zA-Z]', ' ', str(yorumlar['Review'][0]))
#Tümünü küçük harf olarak değiştirdik.
yorum = yorum.lower()
