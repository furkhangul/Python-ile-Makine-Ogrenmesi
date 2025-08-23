"""
Karar Ağacı kullanarak tahmin yöntemi:

Diyelim ki elimizde bir sürü meyve var ve bi robota bu meyvelerin ne olduğunu
tahmin etmesini bekliyoruz.
Ona farklı sorular sorduarbiliriz:
BU meyvenin rengi ne ?
Şekli uzun mu yuvarlak mı ?
Kabuğu kalın mı ince mi?
bu sorulara cevap vererek robot her seferinde bir seçeneği eler ve sonunda Muz tanımını yapar.

Bu şekilde ulaşmaya karar ağacı denir.

Daha terimsel olarak karar ağacı :
İF - ELSE - THEN gibi kurallara dayanan bir sınıflandırma ve tahmin yöntemidir.
Verileri alır, onlara bölerek dallanır ve sonunda yapraklarda tahmin sonucunu verir

-Karar ağacının kullanım nedenleri
/*Kolay anlaşılır, insan gibi düşünür kuralları nettir.
/*Görselleştirebilir.
/*Önişleme az ister, verileri özel olarak hazırlamaya ihtiyaç duymaz
/*Karışık ilişkileri çözebilir. Çok sayıda değişkenle çalışabilir.


Tercih Edilir - Edilmezleri:

|->Tercihler:
>Anlaşılması ve açıklanması gereken durumlarda.
>Verinin boyutu çok büyük değilse.
>Hızlı prototipleme gereken yerde.

|->Tercih Edilmez:
>Çok büyük veri varsa ve model çok dallanıyorsa
>Sürekli değişen veri varsa
>Daha yüksek doğruluk gerektiren bazı durumlarda


***Nasıl Oluşturulur:
1-Tüm veri kümesiyle başlşar
2-Her özellik için veri ne kadar iyi arıyor diye bak
3-En iyi ayıran özellik seç
4-Bu ösellik üzerinden veriyi dallara ayır.
5-Her dalda aynı işlemi tekrarla.
6-Tüm veriler ya aynı sınıfa ait olana ya da durma kriterine ulaşana kadar devam et.
7- Ağacın yapraklarında sonuç olur: Evet/Hayır gibi.
"""
