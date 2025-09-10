"""
LDA

Sınıflandırma problemlerinde kullanılır. PCA gibi boyut indirgeme yöntemi olsa da amacı farklıdır.
PCA yalnızca varyansı maksimize ederken, LDA sınıflar arasındaki farkı en iyi şekilde ayırmayı hedefler.

Genelde gözetimli öğrenme problemlerinde kullanılır.
Yani verilerde sınıf  bilgisi varsa tercih edilir.

Özellikle:
Görüntü tanıma
Yüz tanıma
Metin sınıflandırma
Tıbbi veri analizi
gibi alanlarda kullanılır.

Sınıflar arası ayrımı artırırken, sınıf içi dağılımı azaltmak için.
Bu sayede daha doğru sınıflandırma elde edilir.

LDA Algoritması
- Her sınıfın ortalaması hesaplanır.
- Genel ortalama yani tüm sınıfların ortalaması bulunur.
- Sınıf içi scatter matrisi ve sınıflar arası scatter matrisi hesaplanır.
- Bu iki matrisle genelleştirilmiş özdeğer problemi çözülür
- Elde edilen özvektörlerden en yüksek özdeğere sahip olan k tanesi seçilir.
- Bu vektörlerle orijinal veri uzayı dönüştürülür.

PCA varyansı dikkate alır ama sınıf etiketlerini bilmez.
LDA sınıfları bilir ve sınıf ayrımını maksimize etmeye çalışır.
"""
