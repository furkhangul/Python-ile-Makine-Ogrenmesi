"""
 Dendrogram (Hiyerarşik Kümeleme için)

- Dendrogram, hiyerarşik kümeleme algoritmalarında kullanılan bir görselleştirme yöntemidir.
- Veriler arasındaki benzerlikleri gösteren ağaç yapısına benzer bir diyagramdır.
- Amacı neir: hangi verilerin önce hangi kümelerle birleştiğini ve kümelerin hangi mesafelerde oluştuğunu göstermektir.
 Nasıl Çalışır:
1. Her veri noktası başlangıçta kendi başına bir kümedir.
2. Birbirine en yakın iki küme birleşir.
3. Bu işlem, tek bir küme kalana kadar devam eder.
4. Sonuç olarak, birleşme adımları bir ağaç (dendrogram) üzerinde gösterilir.


Dikey çizgiler kümeler arası mesafeyi gösterir.
Yatay çizgiler kümelerin birleştiği noktayı gösterir.
Diyagramda bir “yükseklik (distance threshold)” belirlenerek uygun küme sayısı seçilebilir.
Genelde büyük mesafelerin olduğu noktalar kümelerin ayrımında tercih edilir.

üşteri segmentasyonu
DNA benzerliklerini inceleme
Belge kümelendirme

:Dendrogram, hiyerarşik kümeleme için verilerin hangi sırayla ve hangi mesafelerde birleştiğini görsel olarak anlamamızı sağlayan bir araçtır.
"""
