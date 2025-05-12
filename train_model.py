# src/train_model.py

"""
Entrenamiento de modelo para detección de fraude en seguros.

- Crea el dataset si no existe o si RECREATE_DATA es True.
- Entrena un RandomForestClassifier.
- Evalúa y guarda métricas, gráficas y el modelo entrenado.

Autor: Jorge Octavio Gómez González
Fecha: 2025-05-10
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------- CONFIGURACIÓN ----------------------
DATA_PATH = "data/fraud_data.csv"
MODEL_PATH = "models/random_forest_model.pkl"
RECREATE_DATA = True  # Cambiar a True si se desea recrear el CSV
DATA_SIZE = 500000       # Número de registros a generar si se recrea
# -----------------------------------------------------------

def create_synthetic_data(path: str, num_records: int):
    """
    Crea un dataset simulado de fraudes y lo guarda como archivo CSV.

    Args:
        path (str): Ruta donde guardar el archivo CSV.
        num_records (int): Cantidad de registros a generar.
    """
    np.random.seed(42)
    data = {
        "age": np.random.randint(18, 70, size=num_records),
        "income": np.random.randint(20000, 120000, size=num_records),
        "claim_amount": np.random.randint(1000, 50000, size=num_records),
        "num_claims": np.random.poisson(2, size=num_records),
        "has_prior_fraud": np.random.randint(0, 2, size=num_records),
        "is_fraud": np.random.choice([0, 1], size=num_records, p=[0.9, 0.1])
    }
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Archivo creado: {path} con {num_records} registros.")

# Crear datos si es necesario
if RECREATE_DATA or not os.path.exists(DATA_PATH):
    create_synthetic_data(DATA_PATH, DATA_SIZE)
else:
    print(f"Usando datos existentes: {DATA_PATH}")

# Cargar y preprocesar datos
df = pd.read_csv(DATA_PATH)
df.dropna(inplace=True)
y = df["is_fraud"]
X = df.drop("is_fraud", axis=1)

# División de datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluación
y_pred = model.predict(X_test)
print("Reporte de Clasificación:\n", classification_report(y_test, y_pred))
print("Matriz de Confusión:\n", confusion_matrix(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))

# Guardar matriz de confusión
os.makedirs("visualizations", exist_ok=True)
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.title("Matriz de Confusión")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.savefig("visualizations/confusion_matrix.png")
plt.close()

# Guardar modelo entrenado
os.makedirs("models", exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"Modelo guardado en: {MODEL_PATH}")
