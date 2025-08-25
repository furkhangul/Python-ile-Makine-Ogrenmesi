"""
Logistic Function
Logistic Regression, makine öğrenmesinde sınıflandırma problemleri için kullanılan
temel ve etkili bir algoritmadır.

Bir gözlemin belirli bir sınıfa ait olma olasılığını tahmin eder.


ÖrneK OLARAK:
Bir müşterinin kredi kartı başvurusunun onaylanıp onaylanmayacağını tahmin etme
VEYA:
Bir e-postanın spam olup olmadığını belirleme


TEMEL MANTIK:

1-Lineer Kombinasyon:
Önce tıpkı lineer regresyonda olduğu gibi, giriş verilerinin (özelliklerin)
ağırlıklı toplamı alınır:
z=w0+w1x1+w2x2+⋯+wnxn=w^Tx

Xi: giriş değişkenleri
Wi: Ağırlıkları
Z: Lineer Skor

2-Sigmond Fonkisyonu:
Bu z değeri daha sonra bir sigmoid (lojistik) fonksiyondan geçirilerek [0, 1] aralığına çekilir:

3-Sınıf Kararı:
Olasılık 0.5’ten büyükse pozitif sınıf (örneğin: 1), değilse negatif sınıf (0) seçilir:

Modelin Öğrenmesi:
Model, bu kaybı azaltacak ağırlıkları öğrenmek için genellikle gradient descent algoritmasını kullanır
"""
