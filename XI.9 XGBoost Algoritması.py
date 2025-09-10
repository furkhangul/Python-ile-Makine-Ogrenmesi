"""
XGBoost (Extreme Gradient Boosting)

XGBoost, denetimli öğrenmede kullanılan, güçlü ve hızlı bir ağaç tabanlı modeldir. 
Özellikle büyük veri setlerinde yüksek doğruluk ve düşük hata oranıyla öne çıkar.

Boosting nedir:
Zayıf öğreniciler art arda eğitilerek güçlü bir model elde edilir. 
Her yeni model önceki modelin hatalarını düzeltmeye çalışır.

XGBoost bu yöntemi optimize eder:
- Hata fonksiyonunu ikinci dereceden türevle optimize eder
- Ağaçları daha hızlı ve verimli şekilde oluşturur
- Düzenlileştirme (regularization) ile aşırı öğrenmeyi engeller

Avantajları:
- Çok hızlıdır, paralel işlem yapabilir
- Aşırı öğrenmeye karşı dayanıklıdır
- Eksik verilerle başa çıkabilir
- Hem sınıflandırma hem regresyon problemlerinde kullanılır
- Kaggle gibi yarışmalarda sıkça tercih edilir

Kullanımı:
XGBoost modelini eğitirken fit metodu kullanılır
Parametrelerle modelin derinliği, öğrenme oranı, ağaç sayısı gibi ayarlar yapılır

Önemli parametreler:
- n_estimators: Ağaç sayısı
- max_depth: Her ağacın derinliği
- learning_rate: Her adımda yapılan düzeltmenin büyüklüğü
- subsample: Eğitim verisinin ne kadarı kullanılacak
- colsample_bytree: Her ağaçta kullanılacak değişken oranı

XGBoost ayrıca modelin hangi değişkenleri ne kadar kullandığını da gösterebilir. 
Bu sayede öznitelik seçimi için de yardımcı olur.
"""
