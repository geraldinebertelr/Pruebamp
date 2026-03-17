import streamlit as st
import pandas as pd

st.set_page_config(page_title="Operación MP", layout="wide")

# -----------------------
# HEADER
# -----------------------
st.title("Operación Integrada de Materias Primas")
st.caption("Continuidad operativa | Control de inventarios | Eficiencia en descargues")

# -----------------------
# KPIs
# -----------------------
st.subheader("Indicadores Clave")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Disponibilidad equipos", "92%")
col2.metric("Cobertura inventario", "5 días")
col3.metric("Desviación inventario", "3%")
col4.metric("Rendimiento descargue", "450 ton/h")

# -----------------------
# MENU
# -----------------------
menu = st.sidebar.selectbox(
    "Selecciona módulo",
    ["Equipos", "Personal", "Descargues", "Organización MP", "Abastecimiento", "Inventarios"]
)

# -----------------------
# EQUIPOS
# -----------------------
if menu == "Equipos":
    st.subheader("Gestión de Equipos")

    df = pd.DataFrame({
        "Equipo": ["102", "103", "109", "Lavaruedas", "Parrillas"],
        "Disponibilidad (%)": [95, 90, 88, 98, 100],
        "Horas trabajo": [180, 200, 210, 120, 95],
        "Combustible (L)": [320, 350, 370, 0, 0],
        "Próx mtto": ["50h", "30h", "20h", "15 días", "OK"],
        "Estado": ["OK", "Observación", "Crítico", "OK", "OK"]
    })

    st.dataframe(df, use_container_width=True)

# -----------------------
# PERSONAL
# -----------------------
elif menu == "Personal":
    st.subheader("Gestión de Personal")

    st.metric("Total personal", "8")
    st.write("Turno día: 5")
    st.write("Turno noche: 3")

# -----------------------
# DESCARGUES
# -----------------------
elif menu == "Descargues":
    st.subheader("Descargues 2026")

    df = pd.DataFrame({
        "Barco": ["B1", "B2"],
        "Material": ["Caliza", "Yeso"],
        "Toneladas": [20000, 15000],
        "Tiempo (h)": [40, 35],
        "Rendimiento (ton/h)": [500, 428]
    })

    st.dataframe(df, use_container_width=True)

# -----------------------
# ORGANIZACIÓN
# -----------------------
elif menu == "Organización MP":
    st.subheader("Organización de Materias Primas")

    st.write("Patio Norte: Caliza - 80% ocupación")
    st.write("Patio Sur: Yeso - 60% ocupación")

# -----------------------
# ABASTECIMIENTO
# -----------------------
elif menu == "Abastecimiento":
    st.subheader("Plan de Abastecimiento")

    st.write("Próximo arribo: Caliza - 25,000 ton")
    st.write("Ubicación: Patio Norte")

# -----------------------
# INVENTARIOS
# -----------------------
elif menu == "Inventarios":
    st.subheader("Inventarios")

    st.write("Inventario físico: 50,000 ton")
    st.write("Inventario sistema: 48,500 ton")
    st.write("Desviación: 3%")
