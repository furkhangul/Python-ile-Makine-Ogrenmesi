"""
Thompson Örneklemesi — Thompson Sampling

Thompson örneklemesi, çok kollu bandit problemini çözmek için
oldukça sezgisel bir yöntemdir. Temel mantık, her kolun yani
her seçeneğin kazanma ihtimalini bir olasılık dağılımı ile
temsil etmektir. Genellikle Beta dağılımı kullanılır çünkü
başarı ve başarısızlık sayıları ile güncellenmesi kolaydır.

Başlangıçta her kol için geniş bir dağılım vardır. Örneğin
başarı=0, başarısızlık=0 alındığında Beta(1,1) yani
tamamen belirsiz bir dağılım elde edilir. Zaman geçtikçe
kol seçildikçe sonuçlara göre dağılımlar güncellenir. Eğer
kol bir ödül kazandırırsa başarı parametresi artar,
kazandırmazsa başarısızlık parametresi artar. Böylece
her kolun dağılımı geçmiş performansına göre şekillenir.

Algoritma her adımda şu şekilde çalışır: önce her kol için
olasılık dağılımından rastgele bir değer örneklenir.
Sonra en yüksek değeri üreten kol seçilir. Bu sayede
yüksek başarı ihtimali olan kollar daha çok tercih edilir
ama aynı zamanda düşük görünen kolların da şansı vardır,
çünkü dağılımlar rastgele örnekleme ile fırsat tanır.

Bu yöntem deneme ve keşif arasında doğal bir denge kurar.
Hem iyi performans gösteren kollar öne çıkar, hem de
yeterince denenmemiş kollar tamamen dışlanmaz. Bu yüzden
Thompson örneklemesi pratikte oldukça güçlü ve etkili bir
yöntem olarak kullanılır.
"""
