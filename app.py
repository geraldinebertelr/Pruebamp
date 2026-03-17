import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Operación Integrada MP",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Operación Integrada de Materias Primas")
st.caption("Vista integrada de turno")

menu = st.sidebar.radio(
    "Módulos",
    [
        "Inicio",
        "Equipos operativos",
        "Gestión de personal",
        "Descargues 2026",
        "Organización de materias primas",
        "Abastecimiento",
        "Inventarios y desviaciones"
    ]
)

if menu == "Inicio":
    st.subheader("Resumen operativo del turno")

    # KPIs del turno
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Cargadores disponibles", "3")
    col2.metric("Operadores en turno", "4")
    col3.metric("Supervisores en turno", "1")
    col4.metric("MP programadas a llegar", "2")
    col5.metric("Material recibido turno anterior", "1,250 ton")

    st.markdown("---")

    # Programación del turno + recibido turno anterior
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

    st.markdown("---")

    st.markdown("### Acceso rápido a módulos")

    b1, b2, b3 = st.columns(3)
    b4, b5, b6 = st.columns(3)

    with b1:
        if st.button("Ir a Equipos operativos", use_container_width=True):
            st.info("Selecciona 'Equipos operativos' en el menú lateral.")

    with b2:
        if st.button("Ir a Gestión de personal", use_container_width=True):
            st.info("Selecciona 'Gestión de personal' en el menú lateral.")

    with b3:
        if st.button("Ir a Descargues 2026", use_container_width=True):
            st.info("Selecciona 'Descargues 2026' en el menú lateral.")

    with b4:
        if st.button("Ir a Organización MP", use_container_width=True):
            st.info("Selecciona 'Organización de materias primas' en el menú lateral.")

    with b5:
        if st.button("Ir a Abastecimiento", use_container_width=True):
            st.info("Selecciona 'Abastecimiento' en el menú lateral.")

    with b6:
        if st.button("Ir a Inventarios", use_container_width=True):
            st.info("Selecciona 'Inventarios y desviaciones' en el menú lateral.")

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
