# -*- coding: utf-8 -*-
"""
Created on Wed May 28 13:54:57 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración general
st.set_page_config(page_title="Portafolio Profesional", layout="wide")
st.title("📌 Portafolio Profesional – Javier Horacio Pérez Ricárdez")

st.markdown("""
Matemático con Maestría en Ciencias de la Computación y estudiante de Doctorado en Inteligencia Artificial. 
Especialista en análisis de datos, gestión de proyectos tecnológicos y estrategias digitales para el sector público.
""")

# -------------------------
# 📂 1. DataFrame base
# -------------------------
st.subheader("📂 Datos base de proyectos estratégicos simulados")
df_proyectos = pd.DataFrame({
    "Proyecto": [
        "Digitalización de trámites",
        "Portal de transparencia",
        "Gestión presupuestal",
        "App ciudadana"
    ],
    "Impacto": [9, 8, 6, 10],
    "Esfuerzo": [4, 5, 3, 9],
    "OKR": [
        "85% satisfacción",
        "Transparencia total",
        "10% ahorro anual",
        "Cobertura nacional"
    ],
    "Avance_OKR": [80, 70, 65, 90],
    "Riesgo": [
        "Retrasos legislativos",
        "Recorte presupuestal",
        "Problemas técnicos",
        "Rotación de personal"
    ],
    "Probabilidad_Riesgo": [0.7, 0.6, 0.5, 0.4]
})
st.dataframe(df_proyectos)

# -------------------------
# 📊 2. Dashboard de Indicadores Estratégicos
# -------------------------
st.header("📊 Dashboard de Indicadores Estratégicos")

fechas = pd.date_range(start="2024-01-01", periods=12, freq="M")
df_kpis = pd.DataFrame({
    "Fecha": fechas,
    "Cobertura (%)": np.random.uniform(70, 95, len(fechas)),
    "Eficiencia (%)": np.random.uniform(60, 90, len(fechas)),
    "Satisfacción (%)": np.random.uniform(65, 85, len(fechas)),
    "Avance Presupuestal (%)": np.random.uniform(50, 95, len(fechas))
})

fig_ind = px.line(df_kpis, x="Fecha", y=df_kpis.columns[1:], markers=True)
fig_ind.update_layout(title="Evolución de KPIs", xaxis_title="Fecha", yaxis_title="Porcentaje (%)")
st.plotly_chart(fig_ind, use_container_width=True)

# -------------------------
# 📆 2.1 Filtro por fecha y KPIs filtrados
# -------------------------
st.subheader("📅 Filtro de KPIs por Fecha")

# Selector de fecha
fecha_inicio = st.date_input("Fecha de inicio", fechas.min().date())
fecha_fin = st.date_input("Fecha de fin", fechas.max().date())

# Convertimos a datetime
fecha_inicio = pd.to_datetime(fecha_inicio)
fecha_fin = pd.to_datetime(fecha_fin)

# Filtramos
df_filtrado = df_kpis[(df_kpis["Fecha"] >= fecha_inicio) & (df_kpis["Fecha"] <= fecha_fin)]

# Mostrar tabla con KPIs filtrados
st.write(f"🔎 Mostrando KPIs desde **{fecha_inicio.date()}** hasta **{fecha_fin.date()}**")
st.dataframe(df_filtrado.reset_index(drop=True), use_container_width=True)

# KPIs Promedio
if not df_filtrado.empty:
    st.markdown("### 📈 Promedio de KPIs en el periodo seleccionado:")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cobertura", f"{df_filtrado['Cobertura (%)'].mean():.2f}%")
    col2.metric("Eficiencia", f"{df_filtrado['Eficiencia (%)'].mean():.2f}%")
    col3.metric("Satisfacción", f"{df_filtrado['Satisfacción (%)'].mean():.2f}%")
    col4.metric("Avance Presupuestal", f"{df_filtrado['Avance Presupuestal (%)'].mean():.2f}%")
else:
    st.warning("⚠️ No hay datos para el rango de fechas seleccionado.")

# -------------------------
# 🛑 3. Evaluación de Riesgos
# -------------------------
st.header("🛑 Evaluación de Riesgos")

df_riesgos = df_proyectos[["Proyecto", "Riesgo", "Probabilidad_Riesgo"]]
fig_riesgo = px.bar(df_riesgos, x="Riesgo", y="Probabilidad_Riesgo", color="Probabilidad_Riesgo", 
                    color_continuous_scale="reds", text="Proyecto")
fig_riesgo.update_layout(title="Evaluación de Riesgos por Proyecto")
st.plotly_chart(fig_riesgo)

# -------------------------
# 🧭 4. Matriz de Priorización
# -------------------------
st.header("📌 Matriz de Priorización de Proyectos")

fig_prior = px.scatter(df_proyectos, x="Esfuerzo", y="Impacto", text="Proyecto",
                       color="Impacto", size=[20]*4, color_continuous_scale="blues")
fig_prior.update_traces(textposition='top center')
fig_prior.update_layout(title="Matriz Impacto vs. Esfuerzo")
st.plotly_chart(fig_prior)

# -------------------------
# 🎯 5. Panel de OKRs
# -------------------------
st.header("🎯 Panel de OKRs (Objetivos y Resultados Clave)")

df_okrs = df_proyectos[["Proyecto", "OKR", "Avance_OKR"]].rename(columns={
    "Proyecto": "Objetivo",
    "OKR": "Resultado Clave",
    "Avance_OKR": "Avance (%)"
})
st.dataframe(df_okrs)

# -------------------------
# 📄 6. Descargar CV
# -------------------------
st.header("📄 Descarga de CV")
try:
    with open("CV_Javier HPR.pdf", "rb") as f:
        st.download_button("📥 Descargar CV en PDF", f, file_name="CV_Javier HPR.pdf")
except FileNotFoundError:
    st.warning("⚠️ El archivo `cv_javier.pdf` no se encontró en el directorio. Asegúrate de subirlo.")

# -------------------------
# 📬 7. Contacto
# -------------------------
st.header("📬 Contacto")
st.markdown("""
- 📧 **Email:** jahoperi@gmail.com  
- 📱 **Teléfono:** +52 56 1056 4095  
- 🌐 **LinkedIn:** [linkedin.com/in/javierhoracio](https://www.linkedin.com/in/javier-horacio-perez-ricardez-5b3a5777/)  
""")
