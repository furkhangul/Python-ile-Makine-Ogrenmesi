"""
Düzeltilmiş R-Kare Yöntemi :


R^2 yöntemini hatırlayacak olursak. 1 - HATALARIN KARELERİNİN TOPLAMINI /  ORTALAM FARKLARININ TOPLAMI

Yani R^2 ne kadar büyük ise method o kadar iyi olduğunu söyleyebiliyorduk.

en iyi değer : 1
en kötü değer: 0

R^2 her zaman arttırılabilek bir yöntem değildir. Her zaman olumlu katkı sağlamaya biliyor.
Hatta modelimizin pozitif yanlarını bile maskeleyebiliyor.
Yani bizi negatif yönde etkileyebilmektedir bundan dolayı biz düzeltilmiş versiyonunu
kullanmaktayız.

Modele daha fazla değişken (özellik) eklerseniz, R² daima artar ya da aynı kalır.

Ama bu artış, modelin gerçekten daha iyi tahmin yaptığı anlamına gelmez.

Overfitting (aşırı öğrenme) riski doğar.

Bu nedenle, Adjusted R², modelin karmaşıklığını da dikkate alarak adil bir başarı ölçüsü sunar.


1−R^2 Modelin açıklayamadığı hata oranı.Yani, modelin "başarısız" olduğu kısmı ölçer.

2 n−1 / n−p-1 Ceza oranıdır. Modeldeki özellik sayısı (p) arttıkça bu oran büyür, yani cezayı artırır.
Eğer çok özellik varsa (p ↑), modelin açıklayamadığı hata daha büyük varsayılır.
Ama veri sayısı da çoksa (n ↑), ceza daha küçük olur.

3 Düzeltilmiş R^2 1−[Acıklanamayan hata * Karmasıklık cezası]
"""
