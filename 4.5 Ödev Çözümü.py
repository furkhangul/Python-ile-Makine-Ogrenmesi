import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

df = pd.read_csv("maaslar_yeni.csv")
X = df[["UnvanSeviyesi", "Kidem", "Puan"]]
y = df["maas"]

mlr = LinearRegression()
mlr.fit(X, y)

poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(X, y)

sc_X = StandardScaler()
sc_y = StandardScaler()
X_scaled = sc_X.fit_transform(X)
y_scaled = sc_y.fit_transform(y.values.reshape(-1, 1)).ravel()

svr = SVR(kernel='rbf')
svr.fit(X_scaled, y_scaled)

dt = DecisionTreeRegressor(random_state=0)
dt.fit(X, y)

rr = Ridge(alpha=1.0)
rr.fit(X, y)

models = {
    "MLR": mlr,
    "Polynomial": poly_model,
    "SVR": svr,
    "Decision Tree": dt,
    "Ridge": rr
}

for name, model in models.items():
    if name == "SVR":
        y_pred = sc_y.inverse_transform(model.predict(X_scaled))
    else:
        y_pred = model.predict(X)
    print(f"{name} R2: {r2_score(y, y_pred):.4f}")

ceo_input = [[10, 10, 100]]
mudur_input = [[7, 10, 100]]

for name, model in models.items():
    if name == "SVR":
        ceo_pred = sc_y.inverse_transform(model.predict(sc_X.transform(ceo_input)).reshape(-1, 1))[0][0]
        mudur_pred = sc_y.inverse_transform(model.predict(sc_X.transform(mudur_input)).reshape(-1, 1))[0][0]
    else:
        ceo_pred = model.predict(ceo_input)[0]
        mudur_pred = model.predict(mudur_input)[0]
    print(f"{name} → CEO: {ceo_pred:.2f} TL, Müdür: {mudur_pred:.2f} TL")
print("\n--- Tahmin Özeti ---")
print(f"{'Model':<15} {'CEO Maaşı (TL)':>20} {'Müdür Maaşı (TL)':>20}")
print("-" * 60)

for name, model in models.items():
    if name == "SVR":
        ceo_pred = sc_y.inverse_transform(model.predict(sc_X.transform(ceo_input)).reshape(-1, 1))[0][0]
        mudur_pred = sc_y.inverse_transform(model.predict(sc_X.transform(mudur_input)).reshape(-1, 1))[0][0]
    else:
        ceo_pred = model.predict(ceo_input)[0]
        mudur_pred = model.predict(mudur_input)[0]
    print(f"{name:<15} {ceo_pred:>20.2f} {mudur_pred:>20.2f}")
