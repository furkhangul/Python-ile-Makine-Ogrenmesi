"""
Naif Bayes Sınıflandırıcısı ( Naive Bayes)
Herhangi bir sınıflandırma probleminde olduğu gibi, amacımız birden fazla özelliği
taşıyan bir vektör kullanarak verilen bilgilerden bir eğitim oluşturmak ve bu eğitim
neticesinde gelen yeni verileri doğru bir şekilde sınıflandırmaktadır. Sınıflandırma
işlemleri sırasında, nasıl bir yol izlendiği örnekler üzerinden açıklayacak olursak.

Kısım  Maaş  Yaş  İş Tecrübesi

Yazılım 3000  26    4

Muhasebe 1500  22   2

Yazılım  5000  30   9

Muhasebe  2000  30  7

Muhasebe  500   18  3

Yazılım   2000  20  2

Yazılım   7000  29  5

Muhasebe  6000  45  15


Yukarıda sadedce muhasebe ve yazılım kısımlarında çalışan kişilerin maaş, yaş
ve iş tecrübelerinin içerdiği tablo bulunuyor. MAAŞ:3000 YAŞ:30 TECRÜBE:5 YIL
Bu kişinin hangi meslek dalında çalıştığını bulunuz ?

Öncelikle eğitim ile işe başlayalım sonra da testimizi yaparız. Basitçe veri kümemizideki (data set)
Yazılım ve Muhasebe kısımlarının ortalama ve varyans değerlerini hesaplıyoruz. Bu değerler aşağıdaki şekildedir:


Muhasebe    2500     28,75    6,75
Yazılım     4250     26,25    5
Muhasebe    5833,3   142,25   34,91666667
Yazılım     4916,7   20,25    8,666666667

Yukarıdaki ilk iki satır ortalama ve ikinci iki satır ise varyans değerleridir. Bu değerleri basitçe Excel ile hesapladık.

Şimdi beklenen değeri hesaplayacağız. Yani gelen test verimizin Muhasebe kısmında birisine ait olması veya Yazılım kısmından birisine ait olması için beklenen durum hesabı yapacağız.

Hesaplamaya geçmeden önce yazının konusu olan naive bayes kavramını hızlıca açıklayalım. Aslında naive bayes sınıflandırıcısı basiçte bütün koşullu olasılıkların çarpımıdır.

Aşağıdaki şekilde gösterilebilir:

Sınıflandırma (s1,s2,s3...) = azami p (K=k= ..
"""
