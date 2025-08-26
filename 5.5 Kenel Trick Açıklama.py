"""
Kernel trick (çekirdek hilesi), doğrusal olmayan verileri sınıflandırmak için kullanılan bir tekniktir.
Özellikle SVM gibi algoritmalarda kullanılır.

Neden kullanılır:
- Gerçek hayattaki veriler çoğu zaman doğrusal olarak  ayrılamaz.
- Kernel trick, veriyi yüksek boyutlu bir uzaya dönüştürmeden, 
  sanki dönüştürülmüş gibi hesap yapmamıza olanak sağlar.
- Böylece doğrusal olmayan veriler, bu yeni uzayda doğrusal hale gelir ve kolayca sınıflandırılabilir.

Nasıl çalışır:
- Kernel trick, orijinal verileri dönüştürmek yerine, iki veri noktası arasındaki 
  iç çarpımı yüksek boyutlu uzayda olaylı olarak hesaplar.
- Bu iç çarpımı hesaplayan fonksiyona kernel fonksiyonu denir.

Yaygın kernel fonksiyonları:
- Linear kernel: Doğrusal ayırma için
- Polynomial kernel: Polinom dereceli ayırma
- RBF (Radial Basis Function) kernel: Gauss dağılımlı, en yaygın kullanılan kernel
- Sigmoid kernel: Yapay sinir ağlarına benzer davranır

Ne değildir:
- Kernel trick bir makine öğrenmesi algoritması değildir, sadece bir matematiksel tekniktir.
- Kernel trick kullanıldığında veriler fiziksel olarak yüksek boyutlu hale getirilmez;
  bu işlemler dolaylı yoldan, hesaplamalar üzerinden yapılır — bu sayede işlem maliyeti düşer.
- Her durumda kernel kullanmak iyi sonuç vermez; uygun kernel seçilmezse model aşırı öğrenebilir (overfitting)
  ya da yetersiz kalabilir.


Kernel trick, doğrusal olmayan verilerde güçlü sınıflandırma yapmak için kullanılır.
SVM başta olmak üzere kernel destekli algoritmalarda doğruluk ve esneklik kazandırır,
ama kernel seçimi dikkatle yapılmalıdır.
"""
