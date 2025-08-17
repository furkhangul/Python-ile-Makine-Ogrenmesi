"""

basit doğrusal regresyonda
x bağımsı değişkeni y bağımlı değişkeninini bulmamızı sağlıyordur.
çok değişkenli modellerde
birden fazla değişken var ve bunların ne oranda y yi etkilediğini bilemeyiz.

burada hangi değişkeni seçitğimiz çpk önemlidir.

bunun için fakrlo yaklaşımlar mevcuttur.
1-Tüm değişkenleri dahil etmek
2-Geriye doğru eleme
3-İleri seçim
4-İki yönlü eleme
5-Skor karşılaştırma

Değişken Seçimi:
Çok fazla değişken varsa model karmaşık hale gelir.
Gereksiz değişkenler modele gürültü katar.
Aşırı değişken sayısı → aşırı uyum riski.
Yorumlamak zorlaşır.
Hesaplama maliyeti artar.


1*Tüm Değişkenleri Dahil Etmek
Hiçbir değişkeni elemeden hepsini modele koyarsın.
“Hiçbir şeyi kaçırmayayım” düşüncesiyle yapılır.

2*Geriye Doğru Eleme
Tüm değişkenlerle başlarsın.
En önemsiz (yüksek p-değeri) olanı silersin.
Modeli yeniden kurarsın.
Tekrar en anlamsız değişkeni silersin.
Bu işlemi, tüm kalan değişkenler istatistiksel olarak anlamlı
olana kadar tekrar edersin (genelde p < 0.05).


3* İleri Seçim
Hiçbir değişkenle başlamazsın (boş model).
En anlamlı (düşük p-değerli) değişkeni eklersin.
Sonra diğer değişkenleri tek tek denersin, hangisi modeli daha iyi yapıyorsa onu eklersin.
Model iyileşmeyi bırakana kadar devam edersin.


4*İki Yönlü Eleme
İleri seçim + Geriye eleme birleşimidir.
Hem yeni değişken ekler, hem de mevcut olanlardan gerekirse çıkarır.
Her adımda “model gelişiyor mu?” diye kontrol edilir.

5*Skor Karşılaştırma
Farklı modelleri istatistiksel kıyaslama skorları ile karşılaştırırsın.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("veriler.csv")
