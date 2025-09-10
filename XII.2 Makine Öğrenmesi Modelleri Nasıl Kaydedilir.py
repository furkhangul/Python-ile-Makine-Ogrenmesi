"""
Makine Öğrenmesi Modelleri Nasıl Kaydedilir

Model eğitildikten sonra her seferinde tekrar eğitmek zaman kaybıdır.
Modeli kaydederek daha sonra doğrudan yükleyip kullanmak mümkündür.

Kaydetme işlemi genelde pickle veya joblib kütüphaneleriyle yapılır

pickle ile model kaydetme:
1- import pickle yapılır
2- model dosya olarak yazma modunda açılır
3- pickle.dump ile model dosyaya kaydedilir

pickle ile model yükleme:
1- model dosya okuma modunda açılır
2- pickle.load ile model geri yüklenir

joblib ile model kaydetme:
joblib, büyük numpy dizileriyle daha verimli çalışır
1- from joblib import dump, load
2- dump ile model kaydedilir
3- load ile model geri yüklenir

Örnek (pickle):
import pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

Örnek (joblib):
from joblib import dump, load
dump(model, 'model.joblib')
loaded_model = load('model.joblib')

Model yüklendikten sonra normal tahmin yapılır:
y_pred = loaded_model.predict(x_test)

Modelle birlikte scaler gibi ön işlem adımları da kaydedilebilir
"""
