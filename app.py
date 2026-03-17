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

    # KPIs principales
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Disponibilidad equipos", "92%", "+2%")
    col2.metric("Cobertura inventario", "5 días", "-1 día")
    col3.metric("Desviación inventario", "3%", "-0.5%")
    col4.metric("Rendimiento descargue", "450 ton/h", "+20 ton/h")

    st.markdown("---")

    # Flujo integrado de la operación
    st.markdown("### Flujo integrado de la operación")
    flujo_cols = st.columns(6)

    flujo_cols[0].info("**Minería**\n\nExtracción y suministro")
    flujo_cols[1].info("**Abastecimiento**\n\nPlan de arribo")
    flujo_cols[2].info("**Logística**\n\nRecepción y descargue")
    flujo_cols[3].info("**Patios / Inventarios**\n\nAlmacenamiento y control")
    flujo_cols[4].info("**Molienda**\n\nSuministro a producción")
    flujo_cols[5].info("**Seguimiento**\n\nIndicadores y decisiones")

    st.markdown("---")

    # Dos bloques: alertas y estado general
    col_izq, col_der = st.columns([1, 1])

    with col_izq:
        st.markdown("### Alertas operativas")
        st.warning("Cargador 109 próximo a mantenimiento.")
        st.warning("Cobertura de yeso por debajo de meta.")
        st.warning("Desviación inventario físico vs sistema en revisión.")

    with col_der:
        st.markdown("### Estado general de la operación")
        estado_df = pd.DataFrame({
            "Frente": [
                "Equipos",
                "Personal",
                "Descargues",
                "Inventarios",
                "Abastecimiento"
            ],
            "Estado": [
                "Operativo",
                "Completo",
                "En seguimiento",
                "Con desviación",
                "Programado"
            ]
        })
        st.dataframe(estado_df, use_container_width=True, hide_index=True)

    st.markdown("---")

    st.info(
        "Esta vista resume el estado de la operación de materias primas, "
        "integrando equipos, personal, descargues, inventarios y abastecimiento."
    )

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
