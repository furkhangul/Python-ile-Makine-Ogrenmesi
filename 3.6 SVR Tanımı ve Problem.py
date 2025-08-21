"""
SVC -> Support Vector Regeression -> Destek Vektör Regresyonu:

SVR, veriler arasında ilişkiyi çok hassas bir şekilde tahmin etmek için kullanılan
makine öğrenmesi yöntemidir. Destek Vektör Makineleri adında bir sistemden gelir ama bu sefer
sınıflandırma değil tahmin yapar.

Örneğin bi bebeğe annesi, ona yaşına göre kaç saat uyuması gerektiğini öğretiyor.
1.yaş -> 14 SAAT
2.yaş -> 13 SAAT
3.yaş -> 12 SAAT
.
.
.

Bebek artık düşünüyor ve 2.5 yaşında bir bebek kaç saat uyur diye kendi çözmeye çalışıyor.

İşte bu sırada SVR ortaya çıkıyor ve bebeğe ben tüm verilere bakacağım, ama sadece dümdüz bir çizgi değil
ben hataları olan bir alan çizeceğim, bu alanın içerisindeysen tamam yakın diyeceğim der.


Çalışma mantığı ise:
1-TAHMİN BANDI:
ortada bir tahmin çizgisi çeker
sonra onun etrafına yukarıdan aşağıdan küçük bir boşluk (epsilon) bırakır.
der ki bu bandın içindeki tahminler yeterince iyi, kabul edilebilir .
buna "margin of tolerance" denir.

2- EN İYİ ÇİZGİYİ ÇEKEM
verilere en yakın duran ama epsilon bandının dışına fazla taşmayan bir çizgi
vebu bandın dışına çıkan her noktaya küçük hatalar verir.


---------------------------------
DOĞRUSAL REGRESYON İLE FARKI
- Doğrusal regresyon düz çizgi çeker, SVR ise tolerans bandı içerisinde en iyi çizgiyi
- Doğrusal regresyon her hatayı dikkate alır ama SVR ise sadece bandın dışındaki hatalara odaklanır.
- Doğrusal regresyonda eseneklik azken SVR'de daha yüksektir.

-----------------------------------
SVR KULLANIM ALANLARI:
-Veriler doğru şeklinde değilse nolineer ise yani kullanılır.
-Aykırı değerler varsa yani uç noktalarda garip veriler varsa.
-Daha yüksek doğruluk isteniyorsa kullanılır.
-Verilerin az ama hassas tahmin yapmasını istiyorsak kullanırız.

--------------------------------
epsilon: Tolerans sınırını ifade eder. bu kadar hata olur bu kadar olmaz sınırını belirler.
Destek Vektörü: Tahmin bandının dışındaki önemli noktalar. modeli etkileyen özel veriler.
kernel: verileri başka uzaay taşıyarak daha karmaşık ilişkileri yakalamak yöntemidir. Burada eğri çizgiler bile çizilebiliyormuş.


-----------------------------------
Ölçeklendirme kullanılması önemlidir çünkü svr büyük- küçük sayılara duyarlıdır.
"""

#Not: Hangi regresyon modelini kullanacağımızı kendimiz belirliyoruz.
#Not2: https://scikit-learn.org/ sitesi üzerinden araştırma yap.
