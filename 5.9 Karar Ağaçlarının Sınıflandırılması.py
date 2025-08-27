"""
Karar Ağacı ile Sınıflandırma


Karar Ağacı ile Sınıflandırma Yöntemi

Diyelim ki elimizde çeşitli meyvelerden oluşan bir veri seti var ve bir modelin, yani bir robotun, bu meyveleri doğru şekilde sınıflandırmasını istiyoruz.

Bunun için karar ağacı sınıflandırma yöntemini kullanabiliriz. Bu yöntem, veriye sorular sorarak her seferinde olasılıkları azaltır ve sonunda doğru sınıfa ulaşır.

Örneğin:
- Meyvenin rengi nedir?
- Şekli uzun mu yoksa yuvarlak mı?
- Kabuğu kalın mı, ince mi?

Bu tür sorular karar ağacında düğüm (node) olarak yer alır. Her soru, veriyi alt gruplara ayırır ve en sonunda karar yapraklarına (leaf) ulaşılır. Örneğin "Muz", "Elma" gibi.

Karar Ağacı Nedir:
Karar ağacı, `IF - ELSE - THEN` kurallarına dayalı bir **sınıflandırma** ve **tahmin** algoritmasıdır. Veri setini özelliklerine göre dallara ayırarak çalışır ve yaprak (leaf) düğümlerinde tahmin sonuçlarını verir.
Karar Ağacının Avantajları:

- Anlaşılması kolaydır, karar kuralları nettir.
- Görselleştirme ile modelin iç işleyişi izlenebilir.
- Verilere fazla ön işleme gerek duymaz.
- Karmaşık veri ilişkilerini yakalayabilir, çok sayıda özellik ile çalışabilir.

Tercih Edilir:
- Modelin anlaşılır olması önemliyse.
- Veri seti çok büyük değilse.
- Hızlı ve açıklanabilir bir prototip gerekiyorsa.

Tercih Edilmez:
- Büyük ve karmaşık veri setlerinde, model fazla dallanıp aşırı öğrenme (overfitting) yapabilir.
- Veri çok sık değişiyorsa model sürekli yeniden eğitilmek zorunda kalabilir.
- Daha yüksek doğruluk gereken durumlarda (örneğin derin öğrenme ile kıyaslandığında) yeterli performans vermeyebilir.

Karar Ağacı Nasıl Oluşturulur:

1. **Tüm veri kümesiyle başlanır.**
2. **Her özellik için veri ne kadar iyi ayırıyor, ölçülür.** (Gini, Entropy, Information.....)
3. **En iyi ayıran özellik seçilir.**
4. **Bu özellik üzerinden veri dallara ayrılır.**
5. **Her bir dalda aynı işlem tekrarlanır.**
6. **Veriler ya tamamen sınıflandırıldığında ya da durma kriterine ulaşınca işlem durur.**
7. **Yaprak düğümlerde sınıflar yer alır. (örneğin: Elma / Muz / Armut)**


Bu yapı sayesinde karar ağacı modeli, verilen özelliklere göre veriyi sınıflandırır.


"""
