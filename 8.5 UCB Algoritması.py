"""
UCB — Upper Confidence Bound - ÜST GÜVENME SINIRI 

UCB algoritması aslında tek kollu canavar probleminin devamı gibi
düşünülebilir. Birden fazla makine var ve her birinin kazanma
olasılığı farklı. İnsan deneme yaptıkça hangi makinenin daha çok
kazandırdığını anlamak istiyor ama aynı zamanda hiç denemediği
makinelerde gizli bir şans olup olmadığını da merak ediyor. UCB tam
da bu ikilemi çözmek için geliştirilmiş bir yöntemdir. Bir yandan
bildiğin, kazandırma ihtimali yüksek olan makineyi kullanmaya devam
ederken, diğer yandan keşif yapmayı da bırakmazsın.

Bu algoritmada her seçenek için bir güven aralığı hesaplanır. Elinde
bir makine hakkında ne kadar veri varsa, ortalaması o kadar güvenilir
hale gelir. Az denenen makinelerde ise daha geniş bir güven payı
bırakılır. Bu yüzden UCB’de her turda her makine için bir skor
hesaplanır. Bu skor hem o makinenin ortalama başarısını hem de
kaç defa denendiğini dikkate alır. Böylece hem güçlü görünen
makineler öne çıkar hem de az denenenler tamamen göz ardı edilmez.

UCB’nin güzelliği şuradadır: ne tamamen rastgele seçim yapar ne de
tek bir makineye saplanıp kalır. Matematiksel olarak zamanla en iyi
makineyi bulmaya yaklaşır. İlk başlarda daha çok keşif yapar ama
ilerleyen adımlarda güçlü seçeneklere ağırlık verir. Sonuçta uzun
vadede toplam kazancı maksimize eder.

Kısacası UCB bize şunu gösterir: karar alırken yalnızca geçmişe
bakmak yetmez, belirsizliği de hesaba katmak gerekir. Az denenmiş bir
seçenek beklenenden çok daha iyi olabilir ama aynı zamanda öğrendiğin
şeyleri de kullanmayı bilmelisin. UCB tam da bu dengeyi kuran akıllı
bir yöntemdir.
"""
