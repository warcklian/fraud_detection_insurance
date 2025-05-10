# src/predict.py

"""
Predicción profesional de fraude en seguros.

- Evalúa múltiples registros simulados.
- Clasifica y justifica predicciones.
- Exporta CSV y visualizaciones gráficas.

Autor: Jorge Octavio Gómez González
Fecha: 2025-05-10
"""

import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Configuración
MODEL_PATH = "models/random_forest_model.pkl"
DATA_PATH = "data/fraud_data.csv"
REPORT_PATH = "reports/fraud_predictions_report.csv"
FIGURES_PATH = "reports/figures"
NUM_REGISTROS = 100
UMBRAL_FRAUDE = 0.6

def train_model():
    print("Entrenando modelo porque no se encontró uno guardado...")
    df = pd.read_csv(DATA_PATH)
    df.dropna(inplace=True)
    y = df["is_fraud"]
    X = df.drop("is_fraud", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return model

def explicar_registro(row, proba):
    razones = []
    if row["has_prior_fraud"] == 1:
        razones.append("historial de fraude previo")
    if row["claim_amount"] > 30000:
        razones.append("monto elevado del reclamo")
    if row["num_claims"] > 3:
        razones.append("número alto de reclamos")
    if row["income"] < 25000:
        razones.append("ingresos bajos")
    if proba > 0.7:
        razones.append("alta probabilidad según el modelo (>70%)")
    return "; ".join(razones) if razones else "sin señales evidentes"

# Cargar o entrenar modelo
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else train_model()

# Generar registros simulados
np.random.seed(100)
datos = pd.DataFrame({
    "age": np.random.randint(18, 70, size=NUM_REGISTROS),
    "income": np.random.randint(20000, 120000, size=NUM_REGISTROS),
    "claim_amount": np.random.randint(1000, 50000, size=NUM_REGISTROS),
    "num_claims": np.random.poisson(2, size=NUM_REGISTROS),
    "has_prior_fraud": np.random.randint(0, 2, size=NUM_REGISTROS)
})

# Predicción y justificación
probs = model.predict_proba(datos)[:, 1]
preds = model.predict(datos)
datos["fraud_probability"] = probs
datos["is_predicted_fraud"] = (probs >= UMBRAL_FRAUDE).astype(int)
datos["justification"] = [explicar_registro(row, p) for row, p in zip(datos.to_dict("records"), probs)]

# Mostrar resumen
print(f"\n== Evaluación de {NUM_REGISTROS} registros simulados ==")
print(datos[["age", "income", "claim_amount", "num_claims", "has_prior_fraud", "fraud_probability", "is_predicted_fraud"]])

# Guardar CSV
os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
datos.to_csv(REPORT_PATH, index=False)
print(f"\nInforme profesional guardado en: {REPORT_PATH}")

# Generar visualizaciones
os.makedirs(FIGURES_PATH, exist_ok=True)

# Histograma de probabilidades
plt.figure()
sns.histplot(datos["fraud_probability"], bins=20, kde=True)
plt.title("Distribución de Probabilidad de Fraude")
plt.xlabel("Probabilidad")
plt.ylabel("Frecuencia")
plt.savefig(os.path.join(FIGURES_PATH, "histograma_probabilidad_fraude.png"))
plt.close()

# Top 10 fraudes
top = datos.sort_values("fraud_probability", ascending=False).head(10)
plt.figure()
sns.barplot(y=top.index, x=top["fraud_probability"])
plt.title("Top 10 Registros con Mayor Probabilidad de Fraude")
plt.xlabel("Probabilidad")
plt.ylabel("Índice del Registro")
plt.savefig(os.path.join(FIGURES_PATH, "top_10_fraudes.png"))
plt.close()

# Dispersión: ingresos vs probabilidad
plt.figure()
sns.scatterplot(data=datos, x="income", y="fraud_probability", hue="is_predicted_fraud", palette="coolwarm")
plt.title("Ingreso vs Probabilidad de Fraude")
plt.xlabel("Ingreso")
plt.ylabel("Probabilidad")
plt.legend(title="¿Predicho como fraude?")
plt.savefig(os.path.join(FIGURES_PATH, "ingreso_vs_probabilidad.png"))
plt.close()

print(f"Gráficas guardadas en: {FIGURES_PATH}")
