#Eksik verilerin kullanımı

"""
Örnek olarak elimizde bulunan bir veri setinde eksik veya yanlış
veri girildiği zaman makine hata verebilir veya yanlış öğrenmeye yönelebilir.

Bunun önüne geçebilmemiz için verilerin düzletilmesi ve onarılmaya çalışılmasını
çalışacağız.
Bu şekilde yapay zeka ile eksik verilerin tahmini ile düzeltilmesine de
bi adım atmış olacağız.
"""
import pandas as pd


#Bu verilerde eksik veriler mevcut. Bunları düzeltmeye çalışacağız.
eksikveriler  = pd.read_csv('eksikveriler.csv')
#Görüntülediğimiz zaman NaN hatası geçen bölgelerde hata veya eksik bilgiler mevcuttur.
print(eksikveriler)

"""
Düzeltmek için verilerin hepsini toplayıp bu verilerin ortalamasını alıp
bu eksik verileri import edecez.

Bu ortalamyı değiştirmeyecek ve verilerin daha tutarlı olmasını sağlayacaktır.
"""



"""
Dropna() fonksiyonu pandasta içeri aktardığımız datada nan olarak geçen satırları es geçerek bize datayı temizleyip sunmaktadır.
Örnekte verdiğimiz üzere 22. satırda nan değeri varken dropna bu satırı çıktı olarak vermeyip doğrudan 21 den 23 e geçerek hataların önlenmesini
sağlamaya çalışmıştır.
"""

"""
Boş değerleri silmek yerine alternatiflerimiz de vardır mesela boş olan bir satırı fakrlı değerler ile 
doldurarak veri kaybını önleyebilmekteyiz bunun için de fillna() fonkisyonunu kullanmaktayız.
"""

#Ortalama değer alınır.
avarage = eksikveriler['kilo'].mean()

eksikveriler["kilo"].fillna(avarage,inplace=True)

print(eksikveriler)


#Yaş için de yapabiliriz.
eksikveriler['yas'].fillna(eksikveriler['yas'].mean(), inplace=True)



