import streamlit as st
import pandas as pd

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
st.set_page_config(
    page_title="Operación Integrada MP",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# NAVEGACIÓN
# -----------------------------
if "menu" not in st.session_state:
    st.session_state.menu = "Inicio"

def go_to(section):
    st.session_state.menu = section

# -----------------------------
# HEADER
# -----------------------------
st.title("Operación Integrada de Materias Primas")
st.caption("Visualización integrada de la operación")

# -----------------------------
# MENÚ LATERAL
# -----------------------------
menu = st.sidebar.radio(
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
    ],
    key="menu"
)

# -----------------------------
# INICIO
# -----------------------------
if menu == "Inicio":

    st.subheader("Vista integrada de la operación")

    # 🔥 BANNER LIMPIO CON ICONOS
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #0f3c68, #1f6aa5);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
    ">

        <h2 style="margin-bottom:10px;">
            Operación Integrada de Materias Primas
        </h2>

        <div style="font-size:28px;">
            ⛏️ ➜ 📦 ➜ 🚢 ➜ 🏗️ ➜ ⚙️
        </div>

        <div style="margin-top:8px; font-size:14px;">
            Minería | Abastecimiento | Descargue | Almacenamiento | Molienda
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    Esta aplicación integra la operación de materias primas, permitiendo visualizar
    equipos, descargues, inventarios, abastecimiento y recursos en una sola vista.
    """)

    st.markdown("---")

    # 🔁 FLUJO OPERATIVO
    st.markdown("### Flujo operativo")

    f1, f2, f3, f4, f5 = st.columns(5)

    with f1:
        st.info("⛏️ Minería")
    with f2:
        st.info("📦 Abastecimiento")
    with f3:
        st.info("🚢 Descargue")
    with f4:
        st.info("🏗️ Almacenamiento")
    with f5:
        st.info("⚙️ Molienda")

    st.markdown("---")

    # 🚀 ACCESOS RÁPIDOS
    st.markdown("### Acceso rápido")

    b1, b2, b3 = st.columns(3)
    b4, b5, b6 = st.columns(3)

    with b1:
        if st.button("🚜 Equipos operativos", use_container_width=True):
            go_to("Equipos operativos")

    with b2:
        if st.button("👷 Gestión de personal", use_container_width=True):
            go_to("Gestión de personal")

    with b3:
        if st.button("🚢 Descargues 2026", use_container_width=True):
            go_to("Descargues 2026")

    with b4:
        if st.button("🏗️ Organización MP", use_container_width=True):
            go_to("Organización de materias primas")

    with b5:
        if st.button("📦 Abastecimiento", use_container_width=True):
            go_to("Abastecimiento")

    with b6:
        if st.button("📊 Inventarios", use_container_width=True):
            go_to("Inventarios y desviaciones")

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
    st.info("Aquí veremos disponibilidad, horas, combustible y mantenimiento de los cargadores 102, 103 y 109.")

# -----------------------------
# GESTIÓN DE PERSONAL
# -----------------------------
elif menu == "Gestión de personal":
    st.subheader("Gestión de personal")
    st.info("Aquí veremos operadores, supervisores y turnos.")

# -----------------------------
# DESCARGUES
# -----------------------------
elif menu == "Descargues 2026":
    st.subheader("Descargues 2026")
    st.info("Aquí veremos tiempos de descargue, materiales y costos.")

# -----------------------------
# ORGANIZACIÓN MP
# -----------------------------
elif menu == "Organización de materias primas":
    st.subheader("Organización de materias primas")
    st.info("Aquí veremos ocupación de patios y distribución de materiales.")

# -----------------------------
# ABASTECIMIENTO
# -----------------------------
elif menu == "Abastecimiento":
    st.subheader("Abastecimiento")
    st.info("Aquí veremos plan de arribo y almacenamiento por MP.")

# -----------------------------
# INVENTARIOS
# -----------------------------
elif menu == "Inventarios y desviaciones":
    st.subheader("Inventarios y desviaciones")
    st.info("Aquí veremos inventario físico vs sistema y desviaciones.")
