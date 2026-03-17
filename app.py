import streamlit as st

# -----------------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------------
st.set_page_config(
    page_title="Operación Materias Primas",
    layout="wide"
)

# -----------------------------------
# MENÚ LATERAL
# -----------------------------------
menu = st.sidebar.selectbox(
    "Navegación",
    [
        "Inicio",
        "Equipos",
        "Personal",
        "Descargues",
        "Inventarios",
        "Abastecimiento"
    ]
)

# -----------------------------------
# INICIO
# -----------------------------------
if menu == "Inicio":

    # TÍTULO
    st.title("Operación de Materias Primas")

    # 🔥 IMAGEN MÁS PROTAGONISTA
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.image("MPImage.png", width=750)

    # 🔥 KPIs OPERATIVOS (LO MÁS IMPORTANTE)
    st.markdown("### Estado actual de la operación")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🚜 Cargadores disponibles", 2, delta="1 en mantenimiento")

    with col2:
        st.metric("👷 Operadores en turno", 5)

    with col3:
        st.metric("📦 MP programadas", 3)

    with col4:
        st.metric("🚢 Material recibido", "3,300 ton")

    # CONTEXTO
    st.markdown("## Visión general")

    st.markdown("""
    Este panel permite monitorear en tiempo real el estado de la operación, integrando
    equipos, descargues, inventarios y abastecimiento.

    Facilita la identificación de desviaciones, cuellos de botella y oportunidades de mejora,
    soportando la toma de decisiones operativas.
    """)
# -----------------------------------
# EQUIPOS
# -----------------------------------
elif menu == "Equipos":

    st.header("Equipos Operativos")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Cargador 102", "Disponible")
        st.write("Horas trabajadas: 120 h")
        st.write("Combustible: 85%")
        st.write("Próximo mtto: 20 h")

    with col2:
        st.metric("Cargador 103", "En operación")
        st.write("Horas trabajadas: 98 h")
        st.write("Combustible: 60%")
        st.write("Próximo mtto: 35 h")

    with col3:
        st.metric("Cargador 109", "En mantenimiento")
        st.write("Horas trabajadas: 150 h")
        st.write("Combustible: 40%")
        st.write("Próximo mtto: En proceso")

# -----------------------------------
# PERSONAL
# -----------------------------------
elif menu == "Personal":

    st.header("Gestión de Personal")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Operadores en turno", 5)

    with col2:
        st.metric("Supervisores en turno", 1)

    st.write("### Turnos activos")
    st.write("- Turno A: 3 operadores")
    st.write("- Turno B: 2 operadores")

# -----------------------------------
# DESCARGUES
# -----------------------------------
elif menu == "Descargues":

    st.header("Descargues de Barcos")

    st.write("### Último turno")
    st.write("- Caliza: 2,500 ton")
    st.write("- Yeso: 800 ton")

    st.write("### Tiempo promedio de descargue")
    st.metric("Horas", "8 h")

# -----------------------------------
# INVENTARIOS
# -----------------------------------
elif menu == "Inventarios":

    st.header("Inventarios")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Stock físico")
        st.write("- Caliza: 10,200 ton")
        st.write("- Yeso: 3,500 ton")

    with col2:
        st.subheader("Sistema")
        st.write("- Caliza: 10,000 ton")
        st.write("- Yeso: 3,600 ton")

    st.write("### Desviaciones")
    st.write("- Caliza: +2%")
    st.write("- Yeso: -3%")

# -----------------------------------
# ABASTECIMIENTO
# -----------------------------------
elif menu == "Abastecimiento":

    st.header("Plan de Abastecimiento")

    st.write("### Arribos programados")
    st.write("- Caliza: 15 marzo")
    st.write("- Yeso: 18 marzo")

    st.write("### Ubicación de almacenamiento")
    st.write("- Patio Norte")
    st.write("- Patio Horno")
