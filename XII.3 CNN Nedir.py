"""
CNN Nedir 

CNN derin öğrenmede sıkça kullanılan özel bir yapay sinir ağı türüdür. 
Özellikle görüntü verileriyle çalışmak için tasarlanmıştır.

Yaygın kullanım alanları:
-Görüntü sınıflandırma
Nesne tanıma
Yüz tanıma
El yazısı tanıma
Tıbbi görüntü analizi

CNN, görüntülerdeki uzamsal (spatial) ilişkileri korur. 
Yani bir pikselin yanındaki piksellerle olan ilişkisini öğrenebilir.

Temel katmanları:
- katman-> Görüntüden filtrelerle özellik çıkarır
- ReLU-> Negatif değerleri sıfıra indirerek doğrusal olmayanlık katar
- Pooling-> Görüntüyü küçültür, önemli bilgileri korur
- Flatten ->  Çok boyutlu veriyi tek boyuta çevirir
- Fully connected -> Son katman, sınıflandırmayı yapar

Avantajla:
- Görüntüdeki kenar, şekil, doku gibi bilgileri otomatik öğrenir
- Elle özellik seçimi gerektirmez
- Büyük veriyle iyi çalışır

Dezavantajları:
- Eğitimi zaman alabilir
- Çok fazla veri ve işlem gücü gerekebilir

CNN, görüntülerdeki karmaşık yapıları katman katman öğrenerek güçlü bir şekilde sınıflandırma yapar
"""
