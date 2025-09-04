"""
Eclat algoritması, apriori algoritması gibi birliktelik kural çıkarımı
üzerine geliştirilmiş bir algoritmadır.
APriori'ye benzemektedir fakat farklı yönleri vardır.

FPRor algoritması da bunlar ile aynı kümede bulunmaktadır.


Eclat algoritması da aynı şekilde bebek bezi, bira ikilemesine benzemektedir.

Apriori algoritması ile en büyük farkı farklı, Apriori Breadth First Search kullanırken
Eclat algoritması Deept First Search algoritması kullanmaktadır.

ÇALIŞMA MANTIĞI:

1-Başlangıç:
Diyelim ki elimizde sepetler var:
(Ekmek, Süt, Yumurta)
(Ekmek, Süt)
(Süt, Çikolata)
(Ekmek, Çikolata)

ECLAT her ürüne bir numara listesi (TID seti) çıkarır.
Ekmek → {1,2,4}
Süt → {1,2,3}
Yumurta → {1}
Çikolata → {3,4}

2-Kesişim mantığı:
Şimdi ECLAT der ki: “Ekmek ve Süt acaba aynı sepetlerde kaç kere çıkmış?”
Ekmek {1,2,4}
Süt {1,2,3}
Kesişim {1,2} → 2 defa beraber alınmış.

Ekmek ve Çikolata: {1,2,4} ∩ {3,4} = {4} → sadece 1 defa.
(Eşik değerimiz 2 ise bu çift elenir).

Yani ECLAT aslında küme kesişimi yaparak birlikte alınan ürünleri buluyor.

3-Derinlemesine DEEPTH FİRST SEARCH
Önce tekli ürünlerden başlıyor → (Ekmek), (Süt), (Yumurta), (Çikolata).
Sonra bunları derinlemesine genişletiyor:
Ekmek → (Ekmek, Süt) → (Ekmek, Süt, Çikolata)…
Böyle böyle her yolun en sonuna kadar gidiyor.
DFS mantığı = “bir üründen başla, sonuna kadar git, sonra geri dön”..

4-sONUC
En sonunda elimizde şöyle kurallar çıkıyor:
Ekmek ve Süt birlikte sık sık alınır.
Süt ve Çikolata bazen beraber alınır.
Yumurta çok az alındığı için çıkarılmaz.
"""
