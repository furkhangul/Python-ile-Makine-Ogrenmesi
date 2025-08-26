"""
Support Vector Mackine:
Sınıflandırma konusunda kullanılan oldukça etkili ve basit yöntemlerden birdir.
Sınıflandırma için bir düzlemde bulunan iki grup arasında bir sınır çizilerek iki grubu
ayrımak mümkündür. Bu sınırların çizileceği yer ise iki grubun da üyelerine en uzak olan
yer olmalıdır.

Bu işlemnin yapılası için iki gruba da yakın ve birbirine paralel iki sınır
çizgisi çizilir ve bu sınır birbirine yaklaştırılarak ortak sınır çizgisi üretilir.

Örnek olarak:

iki grup iki boyutlu bir düzlem üzerinde gösterilmiştir. Bu düzlemi ve boyutları birer
özellik olarak düşünmek mümkündür. Yani basit anlamda sisteme giren
her girdinin bir özellik çıkarımı yapılmış ve sonuç olarak bu iki boyutlu düzlemde her
girdiyi gösteren bir nokta elde edilmiştir. Bu noktaların sınıflandırılması demek, çıkarılmış olan
özelliklere göre girdilerin sınıflandırılması demek.

Her iki sınıf arasında oluşan aralığa tolerans demek mümkündür.
Bu düzlemdeki her bir noktanın tanımı formül ile ifade edilebilir.

Aslında bu denklemler doğruların kaydırılması sonucunda elde edilen en yüksek değerlerin bulunması işleminin bir sonucudur.
Aynı zamanda bu denklemlerle problemin doğrusal ayrılabilir  olduğu da kabul edilmiş olur.

SVM'nin Avantajları
Karmaşık verileri bile ayırabilir (nonlineer sınıflandırma için kernel kullanılır).
Overfitting'e karşı dayanıklıdır.->yani fazla öğrenme oluyor 
Özellikle yüksek boyutlu verilerde iyi çalışır.
"""
