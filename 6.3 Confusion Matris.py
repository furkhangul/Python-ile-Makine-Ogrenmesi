"""
             Tahmin                  Tahmin
               C1                      C2

Gerçek       True Positive           False Negative
  C1

Gerçek       False Positive          True Negative
  C2


Yaptığımız sınıflandırma işleminin sınıf sayısı büyüklüğünde bir Matrix oluştururuz.
Örneğin; Binary  sınıflandırma işlemi için 2x2 bir matrix oluştururken, 5 sınıfa ait bir
sınıflandırma işlemi yaparken 5x5 bir matris kullanırız.

Elimizde kedi ve köpek olmak üzere 2 sınıfa ait toplam 10 veri var. Bu iki sınıfa ait modelimiz tahminler üretiyor
ve biz bu tahminleri gerçek veriler ile karşılaştırmak istiyoruz. O zaman ilk olarak confusion matrix
çizimi ile başlarsak.
Hatırlatma: 2 sınıflı bir sınıflandırma problemi için elimizde 2x2 matrix olmalı.
"""
