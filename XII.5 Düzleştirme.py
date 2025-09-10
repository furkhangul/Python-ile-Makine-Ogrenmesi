"""
Düzleştirme

Düzleştirme işlemi derin öğrenme modellerinde özellikle CNN yapılarında kullanılır. 
Convolution ve pooling katmanları çıktıyı genellikle iki boyutlu veya üç boyutlu bir
matris olarak verir. 
Bu çıktıyı yapay sinir ağının son katmanlarına yani
fully connected katmanlara verebilmek için tek boyutlu hale getirmek gerekir. 
Bu işleme düzleştirme denir. 

Örneğin 8x8x32 boyutundaki bir veri düzleştirildiğinde 2048 boyutunda tek bir vektöre çevrilir. 
Bu vektör artık normal bir sinir ağı gibi işlenebilir hale gelir. 
Düzleştirme sırasında verinin sayısal değerleri değişmez sadece yapısı yani şekli değiştirilir.

Modelin sınıflandırma yapabilmesi için bu dönüşüm zorunludur çünkü fully connected
katmanlar yalnızca tek boyutlu verilerle çalışabilir. 
Bu yüzden flatten yani düzleştirme katmanı CNN mimarisinde convolution
ve pooling katmanlarından sonra gelir.
"""
