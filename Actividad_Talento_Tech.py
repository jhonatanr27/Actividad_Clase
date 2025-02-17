import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# 1. Configuración inicial de la aplicación
st.set_page_config(
    page_title="Dashboard Interactivo",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Dashboard Interactivo con Streamlit")
st.sidebar.title("🔍 Opciones de Navegación")

# Configurar la página
st.set_page_config(page_title="Agroindustria en Colombia", page_icon="🌾", layout="wide")

# Título del dashboard
st.title("Agroindustria en Colombia")

# Crear datos aleatorios (150x8)
np.random.seed(42)
data = pd.DataFrame(np.random.randn(150, 8), columns=[
    'Producción', 'Exportaciones', 'Importaciones', 'Consumo Interno', 
    'Precios', 'Costo de Producción', 'Inversión', 'Empleo'
])

# Mostrar los datos en la aplicación
st.write("Datos Aleatorios de Agroindustria en Colombia", data)

# Selección de variables para graficar
variables = st.multiselect("Selecciona las variables para graficar", options=data.columns, default=data.columns[:2])

# Crear figura usando Plotly Express
if variables:
    fig = px.line(data, y=variables, title="Variables Seleccionadas de Agroindustria")
    st.plotly_chart(fig)
else:
    st.write("Selecciona al menos una variable para mostrar el gráfico.")

# Ejecutar la aplicación
if __name__ == "__main__":
    st.run()
