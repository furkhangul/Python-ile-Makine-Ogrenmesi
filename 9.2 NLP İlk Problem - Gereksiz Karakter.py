import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Hatalı verileri geçmesini istedik
yorumlar = pd.read_csv('Restaurant_Reviews.csv', on_bad_lines='skip')

#İlk olarak noktalama işaretleri boş veya fazla kullanıldığı zaman
#Makine bunu yeni bir cümle olarak algılıyor. Biz de ilk başta noktalama
#işaretlerini kaldırmayı hedefliyoruz.



"""Regular Expression kütüphanesini import ediyoruz.
Bu kütüphane, metin verileriyle düzenli ifadeler kullanarak karmaşık arama,
eşleştirme ve manipülasyon işlemerli yapmanıza olanak tanır. Burada metin içerisinde
belirli desenleri aramak, bu desenleri değiştirmek veya çıkarmak için kullanılır.
"""
import re

yorum = re.sub('[^a-zA-Z]', ' ', str(yorumlar['Review'][0]))
#re.sub() parametresi, verilen deseni metinde arar ve onu belirtilen değer ile değiştirir.
#[^a-zA-Z] ifadesi a'dan z'ye ve büyük harfler için A'dan Z'ye harfler dışında kalan karakterler.
# ," " ifadesi a - z arasında olmayan karakterleri boşluk ile değiştir demek istemektedir.
#str() ifadesi verilen değerleri string'e dönüştürmesini istemektedir.
#yorumlar['Rewiew'] ifadesi ise yorumlar DataFrame'inin Rewiew adlı sütununu seçer.Restoran yorumlarının bulunduğu sütundur.
print(yorum)
