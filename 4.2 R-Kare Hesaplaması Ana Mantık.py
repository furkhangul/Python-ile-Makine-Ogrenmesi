"""
Tahmin Algoritmalarının Değerlendirilmesi
R-Kare yöntemi:
R^2 yöntemi, özellikle regresyon modellerinin performansını değerlendirmek için
kullanılan istatistik bir ölçüttür. Belirtme katsayısı olarak adlandırılır.
R-Kare, modelin bağımlı değişkendeki toplam varyansın ne kadarını ifade eder.

R²'nin Sınırlamaları
Aşırı iyimser olabilir: Özellikle çok fazla değişken varsa, model gereğinden fazla öğrenmiş (overfitting) olabilir.
Karmaşık modellerde yanıltıcıdır: Model çok iyi tahmin yapsa bile, R² düşük çıkabilir (örneğin bazı doğrusal olmayan problemler).
Sadece doğrusal ilişkiyi ölçer: Veride doğrusal olmayan güçlü ilişkiler varsa, R² bunu yakalayamaz.
Hedef değişkenin dağılımına bağlıdır.
Modelin doğruluğunu tek başına garanti etmez. RMSE, MAE gibi metriklerle birlikte değerlendirilmelidir.


Formül:

R2=   1 -  Tahmin Hata / Toplam Hata


Üstteki kısım: Modelin yaptığı hataların toplamı (tahmin hatası)
Alttaki kısım: Eğer hiç model kurmasaydık ve hep ortalamayı tahmin etseydik, ne kadar hata yapardık?

"""
