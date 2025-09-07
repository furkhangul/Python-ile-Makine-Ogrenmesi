"""
Yapay Sinir Ağlarında Katman Kavramı

Yapay sinir ağları, birden fazla **katmandan (layer)** oluşur.
Bu katmanlar, verinin işlenmesini ve öğrenme sürecini sağlar.
Her katman, belirli bir görevi yerine getirir ve ardışık olarak veri aktarımı yapılır.

Sinir ağlarında temel olarak üç tür katman bulunur:

1- Girdi Katman:
Modelin dışarıdan veri aldığı ilk katmandır.
Bu katmanda, nöron sayısı genellikle giriş verisinin boyutu ile aynıdır.
Örneğin, 28x28 piksellik bir görüntü için 784 nöron bulunabilir.

2- Gizli Katman veya katmaları:
Girdilerin işlenerek öğrenildiği katmanlardır.
Her gizli katmandaki nöronlar, önceki katmandan gelen bilgiyi alır, işler ve bir sonraki katmana iletir.
Birden fazla gizli katman varsa bu tür ağlara **derin sinir ağı (deep neural network)** denir.
Gizli katmanların sayısı ve nöron sayısı, modelin kapasitesini belirler.

3- Çıktı Katman:
Modelin nihai çıktısını verdiği katmandır.
Bu katmandaki nöron sayısı, problemin türüne göre değişir.
- Eğer sınıflandırma problemi çözülüyorsa, sınıf sayısı kadar nöron bulunur.
- Regresyon problemlerinde genellikle tek bir nöron olur.

**********************/*/*/*/*/*86541654

Katmanlar Arası Bağlantılar:

Her nöron, bir önceki katmandaki tüm nöronlarla bağlantılıdır.
Bu bağlantılar, ağırlıkları aracılığıyla gerçekleştirilir.
Her bağlantı bir sayı  ile temsil edilir ve bu sayılar modelin öğrenmesini sağlar.

Her katman arasında ayrıca bir sapma terimi de bulunur.
Bu terim, modelin esnekliğini artırır ve daha doğru sonuçlar elde etmesini sağlar.

**********************/*/**

Derin Öğrenmede Katmanların Rolü:

- İlk katmanlar, genellikle **düşük seviyeli özellikleri** (örneğin kenar, renk, şekil) öğrenir.
- Orta katmanlar, bu özellikleri birleştirerek daha **karmaşık yapılar** elde eder.
- Son katmanlar ise **nihai çıktıyı** üretir (örneğin bir nesnenin hangi sınıfa ait olduğunu belirlemek).

Bu yapı, veriden soyut kavramların hiyerarşik bir şekilde öğrenilmesini sağlar.

"""
