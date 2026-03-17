import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Operación Integrada MP",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "menu" not in st.session_state:
    st.session_state.menu = "Inicio"

def go_to(section):
    st.session_state.menu = section

st.title("Operación Integrada de Materias Primas")
st.caption("Visualización integrada de la operación")

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

if menu == "Inicio":
    st.subheader("Vista integrada de la operación")

    st.markdown("### Cadena operativa")
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.info("**Minería**\n\nExtracción y suministro")
    with c2:
        st.info("**Abastecimiento**\n\nPlanificación de arribo")
    with c3:
        st.info("**Logística / Descargue**\n\nRecepción y movilización")
    with c4:
        st.info("**Almacenamiento**\n\nPatios e inventarios")
    with c5:
        st.info("**Molienda**\n\nSuministro a producción")

    st.markdown("---")
    st.markdown("### Acceso rápido a módulos")

    b1, b2, b3 = st.columns(3)
    b4, b5, b6 = st.columns(3)

    with b1:
        if st.button("Resumen operativo", use_container_width=True):
            go_to("Resumen operativo")
    with b2:
        if st.button("Equipos operativos", use_container_width=True):
            go_to("Equipos operativos")
    with b3:
        if st.button("Gestión de personal", use_container_width=True):
            go_to("Gestión de personal")
    with b4:
        if st.button("Descargues 2026", use_container_width=True):
            go_to("Descargues 2026")
    with b5:
        if st.button("Organización MP", use_container_width=True):
            go_to("Organización de materias primas")
    with b6:
        if st.button("Abastecimiento / Inventarios", use_container_width=True):
            go_to("Abastecimiento")

elif menu == "Resumen operativo":
    st.subheader("Resumen operativo del turno")
    st.write("Aquí pondremos las tarjetas de cargadores disponibles, operadores, supervisores, MP programadas y material recibido.")

elif menu == "Equipos operativos":
    st.subheader("Equipos operativos")
    st.write("Sección en construcción.")

elif menu == "Gestión de personal":
    st.subheader("Gestión de personal")
    st.write("Sección en construcción.")

elif menu == "Descargues 2026":
    st.subheader("Descargues 2026")
    st.write("Sección en construcción.")

elif menu == "Organización de materias primas":
    st.subheader("Organización de materias primas")
    st.write("Sección en construcción.")

elif menu == "Abastecimiento":
    st.subheader("Abastecimiento")
    st.write("Sección en construcción.")

elif menu == "Inventarios y desviaciones":
    st.subheader("Inventarios y desviaciones")
    st.write("Sección en construcción.")
