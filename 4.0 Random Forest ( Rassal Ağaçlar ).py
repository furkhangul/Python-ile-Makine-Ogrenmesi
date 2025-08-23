"""
Random Forest ( Rassal Ağaçlar )

Rassal Orman, birden fazla karar ağacının bir araya gelerek beraber çalıştığı bir bakine
öğrenmesi yöntemidir.
Yani,tek bir karar ağacı yerine 100 veya 500 tane küçük karar ağacı oluşturulabilir.
Her ağaç farklı bir bakış açısıyla veriye bakabilir.
En sonunda bu ağaçların verdiği kawrarlar oylanır.
    Eğer bu sınıflandırma ise en çok oy alan sınıf seçilir.
    Regresyon ise tahminlerin ortalaması alınır.

Benzetme yapacak olursam:
Meslek hakkında karar alacak olursam.
Sana tek bir kişiye (dolaylı yoldan karar ağacına) sorar ve o mesleği tek kişinin
fikri ile belirlerdik.
Bir orman oldusu kişiye sorarsak (her biri farklı yerlerden bakıyor) ve çoğu farklı
meslek derse, o zaman daha doğru karar verirsin.
-Her karar ağacı kendi görüşünü belirtir
-Hepsi oylama yapılır
-Daha güvenilir tahmin elde edilir.

NEDEN RASSAL ORMAN:
*Karar ağaçları kolay öğrenir ama fazla ÖĞRENİR ( OVERFİTTİNG)
*Rassal orman, overfittingi azaltır, genelleştirme gücünü arttırır.
*Farklı ağaçlar farklı verilerle çalışır, bu da çeşitlilik katar.

"""
