"""
Gradyan Açılışı

Yapay sinir ağları öğrenmeyi ağırlıklarını güncelleyerek yapar.
Peki ağırlıklar neye göre güncellenir

Hata fonksiyonu kullanılır.
Bu fonksiyon, modelin tahmin ettiği değer ile gerçek değer arasındaki farkı ölçer.

Amaç ise bu hatayı en aza indirmek.

İşte burada GRADYAN devreye girer.

Gradyan, hata fonksiyonunun ağırlıklara göre türevidir.
Yani ağırlığı nasıl değiştirirsek, hatanın ne kadar artıp azalacağını gösterir.

Örnek:
W1 = 0.5, hata = 1.2
hata / W1 = -0.3 → Bu, W1’i artırmak hatayı azaltır demek.
Bu bilgiyle W1 güncellenir:
yeni W1 = W1 - ÖğrenmeOranı × hata/W1

Buna GRADYAN İNİŞİ denir.

ksıaca
1. Gradyan, hata fonksiyonunun eğimini verir.
2. Eğim → Ağırlıkları hangi yönde değiştirmeliyim sorusunun cevabıdır.
3. Gradyan inişi ile model, adım adım hatayı azaltacak şekilde öğrenir.

Bu işlem her veri örneği için veya her epoch sonunda tekrar edilir.
"""

