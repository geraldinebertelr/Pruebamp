import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Operación Integrada MP",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Operación Integrada de Materias Primas")
st.caption("Continuidad operativa | Control de inventarios | Eficiencia en descargues")

menu = st.sidebar.radio(
    "Módulos",
    [
        "Resumen ejecutivo",
        "Equipos operativos",
        "Gestión de personal",
        "Descargues 2026",
        "Organización de materias primas",
        "Abastecimiento",
        "Inventarios y desviaciones"
    ]
)

if menu == "Resumen ejecutivo":
    st.subheader("Resumen ejecutivo")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Disponibilidad equipos", "92%")
    col2.metric("Cobertura inventario", "5 días")
    col3.metric("Desviación inventario", "3%")
    col4.metric("Rendimiento descargue", "450 ton/h")

    st.markdown("### Visión integrada de la operación")
    st.info(
        "Esta vista resume el estado operativo de equipos, personal, descargues, "
        "organización de materias primas, abastecimiento e inventarios."
    )

elif menu == "Equipos operativos":
    st.subheader("Equipos operativos")
    st.write("Aquí mostraremos disponibilidad, horas de trabajo, combustible, próximo mantenimiento y resultado del último mantenimiento.")

elif menu == "Gestión de personal":
    st.subheader("Gestión de personal")
    st.write("Aquí mostraremos recursos actuales, roles y turnos diarios.")

elif menu == "Descargues 2026":
    st.subheader("Descargues 2026")
    st.write("Aquí mostraremos histórico del año, tipo de material, tiempos de descargue y recursos utilizados.")

elif menu == "Organización de materias primas":
    st.subheader("Organización de materias primas")
    st.write("Aquí mostraremos ocupación de patios, materiales por espacio y fotos del estado actual.")

elif menu == "Abastecimiento":
    st.subheader("Abastecimiento")
    st.write("Aquí mostraremos el plan de arribo por materia prima y la ubicación prevista de almacenamiento.")

elif menu == "Inventarios y desviaciones":
    st.subheader("Inventarios y desviaciones")
    st.write("Aquí mostraremos inventario físico, inventario en sistema, desviaciones y cobertura.")
