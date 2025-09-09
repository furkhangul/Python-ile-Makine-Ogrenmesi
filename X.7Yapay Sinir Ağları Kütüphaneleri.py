#Yapay Sinir Ağları Kütüphaneleri
"""
-Pytorch
-Tensorflow -> Google tarafından kuruldu.
-Caffe
-Keras -> Daha pratik
-DeepLearning4J
-Diğerleri


CPU (Central Processing Unit) - Merkezi İşlem Birimi
-----------------------------------------------------
- Bilgisayarın beyni olarak bilinir.
- Genel amaçlı işlemler için tasarlanmıştır.
- Az sayıda, güçlü çekirdeğe sahiptir (örneğin 4-16 çekirdek).
- Seri işlemlerde (tek tek adım adım yapılan hesaplamalar) çok iyidir.
- İşletim sistemi, ofis yazılımları, tarayıcılar gibi görevlerde kullanılır.

GPU (Graphics Processing Unit) - Grafik İşlem Birimi
-----------------------------------------------------
- İlk olarak grafik işlemek için tasarlandı, ama artık paralel hesaplamalarda kullanılıyor.
- Yüzlerce veya binlerce çekirdeğe sahiptir.
- Aynı anda çok sayıda işlemi paralel yapabilir.
- Yapay zeka, görüntü işleme, bilimsel hesaplama gibi yoğun matematiksel işlemlerde kullanılır.

Karşılaştırma:
- CPU → Akıllı ama az kişiyle çalışan yönetici gibi
- GPU → Aynı anda çok işçi çalıştıran büyük bir fabrika gibi

Yapay Zeka Eğitiminde Neden GPU?
- Çünkü sinir ağı hesaplamaları (matris çarpımları vs.) paralel yapılabilir.
- GPU bu işlemleri çok daha hızlı yapar → Eğitim süresi kısalır.


Theano kütüphanesi. GPU'u dağıtmakta kullanılır.
Kares ve Tenseflow kullanılacak.
"""
