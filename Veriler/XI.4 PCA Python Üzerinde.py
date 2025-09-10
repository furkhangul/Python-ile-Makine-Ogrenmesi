import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Veri setini yükle
veriler = pd.read_csv('Wine.csv')
x = veriler.iloc[:, 3:13].values
y = veriler.iloc[:, 13].values

# Eğitim ve test bölme
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

# Ölçekleme
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# PCA
pca = PCA(n_components=2)
x_train_pca = pca.fit_transform(x_train)
x_test_pca = pca.transform(x_test)

# Lojistik regresyon (PCA sonrası)
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train_pca, y_train)

# Tahminler
y_pred = classifier.predict(x_test_pca)
y_proba = classifier.predict_proba(x_test_pca)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
