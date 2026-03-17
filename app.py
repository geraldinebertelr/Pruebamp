import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Operación Integrada MP",
    layout="wide"
)

# -----------------------------
# TÍTULO
# -----------------------------
st.title("Operación Integrada de Materias Primas")
st.caption("Visualización integrada de la operación")

# -----------------------------
# MENÚ LATERAL
# -----------------------------
menu = st.sidebar.selectbox(
    "Módulos",
    [
        "Inicio",
        "Resumen operativo",
        "Equipos operativos",
        "Gestión de personal",
        "Descargues 2026",
        "Organización de materias primas",
        "Abastecimiento",
        "Inventarios y desviaciones"
    ]
)

# -----------------------------
# INICIO
# -----------------------------
if menu == "Inicio":
    st.subheader("Vista integrada de la operación")

    st.markdown("""
    ## Operación Integrada de Materias Primas

    ⛏️ **Minería** → 📦 **Abastecimiento** → 🚢 **Descargue** → 🏗️ **Almacenamiento** → ⚙️ **Molienda**
    """)

    st.markdown("---")

    st.markdown("""
    Esta plataforma permite visualizar de forma integrada la operación de materias primas, 
    incluyendo equipos, descargues, inventarios y abastecimiento, facilitando la toma de decisiones operativas.
    """)

# -----------------------------
# RESUMEN OPERATIVO
# -----------------------------
elif menu == "Resumen operativo":
    st.subheader("Resumen operativo del turno")

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Cargadores disponibles", "3")
    c2.metric("Operadores en turno", "4")
    c3.metric("Supervisores en turno", "1")
    c4.metric("MP programadas a llegar", "2")
    c5.metric("Material recibido turno anterior", "1.250 ton")

    st.markdown("---")

    izq, der = st.columns(2)

    with izq:
        st.markdown("### Materias primas programadas")
        df_programadas = pd.DataFrame({
            "Materia prima": ["Caliza", "Yeso"],
            "Cantidad (ton)": [2500, 800],
            "Ubicación": ["Patio Norte", "Patio Sur"]
        })
        st.dataframe(df_programadas, use_container_width=True, hide_index=True)

    with der:
        st.markdown("### Material recibido turno anterior")
        df_recibido = pd.DataFrame({
            "Materia prima": ["Caliza", "Puzolana"],
            "Cantidad (ton)": [900, 350],
            "Ubicación": ["Patio Norte", "Patio 3"]
        })
        st.dataframe(df_recibido, use_container_width=True, hide_index=True)

# -----------------------------
# EQUIPOS OPERATIVOS
# -----------------------------
elif menu == "Equipos operativos":
    st.subheader("Equipos operativos")

    df_equipos = pd.DataFrame({
        "Equipo": ["102", "103", "109", "Lavaruedas", "Parrillas"],
        "Disponibilidad (%)": [95, 90, 88, 98, 100],
        "Horas trabajo": [180, 200, 210, 120, 95],
        "Combustible": [320, 350, 370, 0, 0],
        "Próx. mtto": ["50 h", "30 h", "20 h", "15 días", "OK"],
        "Último mtto": ["OK", "Observación", "Crítico", "OK", "OK"]
    })
    st.dataframe(df_equipos, use_container_width=True, hide_index=True)

# -----------------------------
# GESTIÓN DE PERSONAL
# -----------------------------
elif menu == "Gestión de personal":
    st.subheader("Gestión de personal")

    c1, c2, c3 = st.columns(3)
    c1.metric("Operadores", "4")
    c2.metric("Supervisores", "1")
    c3.metric("Total personal", "5")

    df_personal = pd.DataFrame({
        "Cargo": [
            "Operador cargador",
            "Operador cargador",
            "Operador cargador",
            "Operador cargador",
            "Supervisor"
        ],
        "Turno": ["Día", "Día", "Noche", "Noche", "Día"]
    })
    st.dataframe(df_personal, use_container_width=True, hide_index=True)

# -----------------------------
# DESCARGUES
# -----------------------------
elif menu == "Descargues 2026":
    st.subheader("Descargues 2026")

    df_descargues = pd.DataFrame({
        "Barco": ["B1", "B2", "B3"],
        "Material": ["Caliza", "Yeso", "Puzolana"],
        "Toneladas": [20000, 15000, 18000],
        "Tiempo (h)": [40, 35, 42],
        "Rendimiento (ton/h)": [500, 428, 429]
    })
    st.dataframe(df_descargues, use_container_width=True, hide_index=True)

# -----------------------------
# ORGANIZACIÓN MP
# -----------------------------
elif menu == "Organización de materias primas":
    st.subheader("Organización de materias primas")

    df_mp = pd.DataFrame({
        "Espacio": ["Patio Norte", "Patio Sur", "Patio 3"],
        "Material": ["Caliza", "Yeso", "Puzolana"],
        "% utilización": [80, 60, 45]
    })
    st.dataframe(df_mp, use_container_width=True, hide_index=True)

# -----------------------------
# ABASTECIMIENTO
# -----------------------------
elif menu == "Abastecimiento":
    st.subheader("Abastecimiento")

    df_abast = pd.DataFrame({
        "MP": ["Caliza", "Yeso"],
        "Cantidad programada (ton)": [25000, 5000],
        "Ubicación prevista": ["Patio Norte", "Patio Sur"]
    })
    st.dataframe(df_abast, use_container_width=True, hide_index=True)

# -----------------------------
# INVENTARIOS
# -----------------------------
elif menu == "Inventarios y desviaciones":
    st.subheader("Inventarios y desviaciones")

    c1, c2, c3 = st.columns(3)
    c1.metric("Inventario físico", "50.000 ton")
    c2.metric("Inventario sistema", "48.500 ton")
    c3.metric("Desviación", "3%")

    df_inv = pd.DataFrame({
        "Materia prima": ["Caliza", "Yeso", "Puzolana"],
        "Físico (ton)": [30000, 10000, 10000],
        "Sistema (ton)": [29000, 9800, 9700],
        "Desviación (%)": [3.4, 2.0, 3.1]
    })
    st.dataframe(df_inv, use_container_width=True, hide_index=True)
