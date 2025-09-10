"""
Model Seçimi ve Değerlendirilmesi

Makine öğrenmesinde farklı algoritmalar farklı veri setlerinde farklı performanslar gösterebilir. 
Bu yüzden en uygun modeli seçmek ve performansını doğru değerlendirmek önemlidir.

Model seçimi sürecinde dikkat edilenler:
- Modelin doğruluk oranı
- Aşırı öğrenme ya da az öğrenme yapıp yapmadığı
- Veri setine uygunluğu
- Eğitim süresi ve hesaplama maliyeti

Model değerlendirmede kullanılan metrikler:
- Confusion matrix: Gerçek ve tahmin edilen değerleri karşılaştırır
- Accuracy: Doğru tahminlerin tüm tahminlere oranı
- Precision: Pozitif tahminlerin ne kadarı doğru
- Recall: Gerçek pozitiflerin ne kadarı doğru tahmin edildi
- F1-score: Precision ve recall'un harmonik ortalaması
- ROC ve AUC: Sınıflandırma problemlerinde modelin ayrım gücünü ölçer

Doğrulama yöntemleri:
- Hold-out: Veri eğitim ve test olarak ayrılır
- K-Fold Cross Validation: Veri k parçaya ayrılır ve her parça bir kez test olarak kullanılır
- Stratified K-Fold: Sınıf dağılımı korunarak k-fold yapılır
- Leave-One-Out: Her seferinde tek bir örnek test için ayrılır

Model seçimi yapılırken sadece tek bir metrik değil, birden fazla metriğe bakmak daha sağlıklı sonuç verir.
"""
