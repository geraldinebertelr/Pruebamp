import streamlit as st
import pandas as pd

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

    # Imagen principal
    st.image(
        "https://images.unsplash.com/photo-1581091012184-5c2b4e9c7b1c",
        use_container_width=True
    )

    st.markdown("""
    ### Operación de Materias Primas

    Esta aplicación integra la operación de materias primas, permitiendo visualizar
    equipos, descargues, inventarios, abastecimiento y recursos en una sola vista.
    """)

    st.markdown("---")

    # Flujo operativo
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

    # Acceso rápido
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
        st.markdown("### Materias primas programadas a llegar en el turno")
        df_programadas = pd.DataFrame({
            "Materia prima": ["Caliza", "Yeso"],
            "Cantidad programada (ton)": [2500, 800],
            "Ubicación prevista": ["Patio Norte", "Patio Sur"]
        })
        st.dataframe(df_programadas, use_container_width=True, hide_index=True)

    with der:
        st.markdown("### Material recibido en el turno anterior")
        df_recibido = pd.DataFrame({
            "Materia prima": ["Caliza", "Puzolana"],
            "Cantidad recibida (ton)": [900, 350],
            "Ubicación": ["Patio Norte", "Patio 3"]
        })
        st.dataframe(df_recibido, use_container_width=True, hide_index=True)

# -----------------------------
# EQUIPOS OPERATIVOS
# -----------------------------
elif menu == "Equipos operativos":
    st.subheader("Equipos operativos")
    st.write("Sección en construcción.")

# -----------------------------
# GESTIÓN DE PERSONAL
# -----------------------------
elif menu == "Gestión de personal":
    st.subheader("Gestión de personal")
    st.write("Sección en construcción.")

# -----------------------------
# DESCARGUES
# -----------------------------
elif menu == "Descargues 2026":
    st.subheader("Descargues 2026")
    st.write("Sección en construcción.")

# -----------------------------
# ORGANIZACIÓN DE MATERIAS PRIMAS
# -----------------------------
elif menu == "Organización de materias primas":
    st.subheader("Organización de materias primas")
    st.write("Sección en construcción.")

# -----------------------------
# ABASTECIMIENTO
# -----------------------------
elif menu == "Abastecimiento":
    st.subheader("Abastecimiento")
    st.write("Sección en construcción.")

# -----------------------------
# INVENTARIOS
# -----------------------------
elif menu == "Inventarios y desviaciones":
    st.subheader("Inventarios y desviaciones")
    st.write("Sección en construcción.")
