import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

veriler = pd.read_csv('Wine.csv')
x = veriler.iloc[:, 3:13].values
y = veriler.iloc[:, 13].values

# Eğitim ve test bölme
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

# Ölçekleme
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Lojistik regresyon için parametre aralığı
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'solver': ['liblinear', 'lbfgs'],
    'penalty': ['l2']
}

# GridSearchCV
grid_search = GridSearchCV(
    estimator=LogisticRegression(random_state=0),
    param_grid=param_grid,
    scoring='accuracy',
    cv=5,
    n_jobs=-1
)

grid_search.fit(x_train, y_train)

print("En iyi parametreler:")
print(grid_search.best_params_)

print("En iyi skor:")
print(grid_search.best_score_)

# En iyi model ile test verisi tahmini
best_model = grid_search.best_estimator_
y_pred = best_model.predict(x_test)

# Değerlendirme
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print("Confusion Matrix:")
print(cm)
print("Test Accuracy:")
print(acc)
