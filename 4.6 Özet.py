"""
Regresyon Yöntemleri Özeti (Python Uygulamaları için)

1. Multiple Linear Regression (MLR)
- Açıklama: Bağımlı değişken ile bağımsız değişkenler arasında doğrusal ilişki kurar.
- Python: sklearn.linear_model.LinearRegression
- Avantaj: Hızlı çalışır, kolay yorumlanır.
- Dezavantaj: Doğrusal olmayan ilişkileri modelleyemez.

2. Polynomial Regression (PR)
- Açıklama: Lineer olmayan ilişkileri modellemek için bağımsız değişkenlerin polinomlarını kullanır.
- Python: sklearn.preprocessing.PolynomialFeatures + LinearRegression
- Avantaj: Eğrisel ilişkiyi modelleyebilir.
- Dezavantaj: Derece arttıkça overfitting riski artar.

3. Support Vector Regression (SVR)
- Açıklama: Verileri kernel fonksiyonlarıyla daha yüksek boyutlara taşıyarak regresyon yapar.
- Python: sklearn.svm.SVR (kernel='rbf', 'linear', vs.)
- Not: Veriler mutlaka ölçeklenmelidir (StandardScaler).
- Avantaj: Karmaşık yapıları genellemede başarılı.
- Dezavantaj: Parametre ayarı hassastır (C, epsilon, kernel).

4. Decision Tree Regressor (DT)
- Açıklama: Veri setini karar düğümleriyle dallara ayırarak tahmin yapar.
- Python: sklearn.tree.DecisionTreeRegressor
- Avantaj: Yorumu kolaydır, model görselleştirilebilir.
- Dezavantaj: Aşırı öğrenme (overfitting) eğilimi vardır.

5. Ridge Regression (RR)
- Açıklama: Lineer regresyona L2 regularizasyonu ekler; katsayıları küçülterek aşırı uyumu engeller.
- Python: sklearn.linear_model.Ridge
- Avantaj: Multicollinearity durumunda kararlıdır, overfitting'e karşı dayanıklıdır.
- Dezavantaj: Model klasik lineer regresyona çok benzeyebilir.

"""
