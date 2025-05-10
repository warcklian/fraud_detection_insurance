# dashboard_fraude.py

"""
Dashboard interactivo para revisión de predicciones de fraude.

- Carga de resultados desde CSV
- Filtros dinámicos por predicción
- Gráficos embebidos

Autor: Jorge Octavio Gómez González
Fecha: 2025-05-10
"""

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configuración del panel
st.set_page_config(page_title="Dashboard de Fraude", layout="wide")
DATA_PATH = "reports/fraud_predictions_report.csv"

# Cargar datos con cache (para versiones streamlit <=1.15)
@st.cache
def load_data(path):
    return pd.read_csv(path)

# Verificación de existencia del archivo
if not os.path.exists(DATA_PATH):
    st.error(f"No se encontró el archivo de datos: {DATA_PATH}")
    st.stop()

df = load_data(DATA_PATH)

# Sidebar con filtros
st.sidebar.header("Filtros")
fraude_filtrado = st.sidebar.selectbox("Mostrar registros:", ["Todos", "Solo FRAUDE", "Solo NO FRAUDE"])
umbral = st.sidebar.slider("Umbral de Probabilidad (%)", 0, 100, 60)

# Aplicar filtros
df_filtrado = df.copy()
if fraude_filtrado == "Solo FRAUDE":
    df_filtrado = df_filtrado[df_filtrado["is_predicted_fraud"] == 1]
elif fraude_filtrado == "Solo NO FRAUDE":
    df_filtrado = df_filtrado[df_filtrado["is_predicted_fraud"] == 0]

df_filtrado = df_filtrado[df_filtrado["fraud_probability"] * 100 >= umbral]

# Encabezado principal
st.title("Predicción de Fraude en Seguros")
st.markdown("Este panel permite explorar las predicciones de riesgo generadas por el modelo entrenado.")

st.metric("Registros Cargados", len(df))
st.metric("Registros Filtrados", len(df_filtrado))

# Tabla de resultados filtrados
st.subheader("Registros Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

# Visualizaciones
col1, col2 = st.columns(2)

with col1:
    st.subheader("Histograma de Probabilidades")
    fig1, ax1 = plt.subplots()
    sns.histplot(df["fraud_probability"], bins=20, kde=True, ax=ax1)
    ax1.set_title("Distribución de Probabilidades")
    st.pyplot(fig1)

with col2:
    st.subheader("Ingreso vs Probabilidad de Fraude")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x="income", y="fraud_probability", hue="is_predicted_fraud", palette="coolwarm", ax=ax2)
    ax2.set_title("Relación Ingreso - Riesgo")
    st.pyplot(fig2)

# Ejecutar el dashboard solo si no está en modo recarga de Streamlit
if __name__ == "__main__":
    import os
    import threading
    import time
    import webbrowser
    import streamlit.web.bootstrap

    # Solo abrir si no hay variable de entorno indicando recarga
    if os.environ.get("STREAMLIT_SERVER_RUN_ONCE", "0") != "1":
        def abrir_navegador():
            time.sleep(1.5)
            webbrowser.open("http://localhost:8501")

        os.environ["STREAMLIT_SERVER_RUN_ONCE"] = "1"
        threading.Thread(target=abrir_navegador).start()
        streamlit.web.bootstrap.run(__file__, "", [], {})
