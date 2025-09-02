"""
K-means kullanılırken veriler verildikten sonra rastgele seçilen kümeler sonucunda
her nokta kendine en yakın merkezde küme oluşturuyor.

Fakat rastgele oluşturulan kümelemede merkezler çok saçma yerlerde oluşursa
veya noktalar birbirine çok yakın ve verilerden uzak kalırsa sıkıntı başlar.

Veriler sonsuza kadar merkezi kaydırır ve başlangıçta bozulmaya başlar.

Burada kümelerin en başarılı şekilde olması için kümelerin en uç noktalarına bakamk yeterlidir.

İki uzaklık arası iki kümeden fazlası olması kümenin güzel bir şekilde yerleşmediğini gösterir.

K-means bu rastgelelik yüzünden çok başarılı bir kümeleme algoritması değildir.

İhtmialler çoktur başarı oranı ise düşüktür.

En olağan şey ise datapointlerin teker teker yerleştirilmesi olur.

Ama bu da oldukça maliyetlidir.


K-MEANS ++
1.Rastgele seçilen noktalardan en yakınına her noktada uzaklığı hesapla
(buna D(X)^2 ile bul )

2.Yeni noktaların mesafenin karesini olasılık alarak bul. ( D(X)^2)
"""
