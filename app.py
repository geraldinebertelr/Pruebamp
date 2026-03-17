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

    st.title("Operación de Materias Primas")

    # IMAGEN PRINCIPAL
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("MPImage.png", width=900)

    # KPIs GENERALES
    st.markdown("### Estado actual de la operación")

    # Fila 1
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🚜 Cargadores", "2", delta="1 en mtto")

    with col2:
        st.metric("👷 Operadores", "2")

    with col3:
        st.metric("👨‍💼 Supervisor", "1")

    with col4:
        st.metric("🚢 Descargues activos", "2")
        st.caption("Caliza / Yeso")

    # Fila 2
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📦 Descargue hoy", "3,300 ton")

    with col2:
        st.metric("🏗️ Ocupación patios", "78%")

    with col3:
        st.metric("⚠️ MP críticas", "2")
        st.caption("Yeso / Puzolana")

    with col4:
        st.metric("📍 En proceso", "Caliza")

    st.markdown("---")

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

    # RESUMEN GENERAL
    st.markdown("### Resumen de equipos")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Disponibles", "2")
    with c2:
        st.metric("En mantenimiento", "1")
    with c3:
        st.metric("Horas acumuladas", "368 h")
    with c4:
        st.metric("Combustible promedio", "62%")

    st.markdown("---")

    # TARJETAS POR EQUIPO
    st.markdown("### Estado por equipo")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Cargador 102")
        st.success("Disponible")
        st.write("**Horas trabajadas:** 120 h")
        st.write("**Combustible:** 85%")
        st.write("**Próximo mtto:** 20 h")
        st.write("**Último mtto:** OK")

    with col2:
        st.subheader("Cargador 103")
        st.info("En operación")
        st.write("**Horas trabajadas:** 98 h")
        st.write("**Combustible:** 60%")
        st.write("**Próximo mtto:** 35 h")
        st.write("**Último mtto:** OK")

    with col3:
        st.subheader("Cargador 109")
        st.error("En mantenimiento")
        st.write("**Horas trabajadas:** 150 h")
        st.write("**Combustible:** 40%")
        st.write("**Próximo mtto:** En proceso")
        st.write("**Último mtto:** Observación")

    st.markdown("---")

    # OTROS EQUIPOS
    st.markdown("### Otros equipos")
    col4, col5 = st.columns(2)

    with col4:
        st.subheader("Lavaruedas")
        st.success("Operativo")
        st.write("**Estado actual:** Disponible")
        st.write("**Última revisión:** OK")

    with col5:
        st.subheader("Parrillas")
        st.success("Operativas")
        st.write("**Estado actual:** Sin novedad")
        st.write("**Última revisión:** OK")
# -----------------------------------
# PERSONAL
# -----------------------------------
elif menu == "Personal":

    st.header("Gestión de Personal")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Operadores en turno", 2)

    with col2:
        st.metric("Supervisor en turno", 1)

    with col3:
        st.metric("Cobertura operativa", "100%")

    st.write("### Turno actual")
    st.write("- Operador 1: Cargador 102")
    st.write("- Operador 2: Cargador 103")
    st.write("- Supervisor: Activo")

# -----------------------------------
# DESCARGUES
# -----------------------------------
elif menu == "Descargues":

    st.header("Descargues")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Descargues activos", "2")

    with col2:
        st.metric("Toneladas hoy", "3,300 ton")

    with col3:
        st.metric("Tiempo promedio", "8 h")

    st.write("### Material en descargue")
    st.write("- Caliza")
    st.write("- Yeso")

    st.write("### Histórico del día")
    st.write("- Barco 1: Caliza - 2,500 ton")
    st.write("- Barco 2: Yeso - 800 ton")

# -----------------------------------
# INVENTARIOS
# -----------------------------------
elif menu == "Inventarios":

    st.header("Inventarios")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Ocupación patios", "78%")

    with col2:
        st.metric("MP críticas", "2")

    with col3:
        st.metric("Desviación total", "3%")

    st.write("### Existencia física vs sistema")
    st.write("- Caliza: 10,200 ton | Sistema: 10,000 ton")
    st.write("- Yeso: 3,500 ton | Sistema: 3,600 ton")
    st.write("- Puzolana: 2,800 ton | Sistema: 2,700 ton")

    st.write("### Materias primas críticas")
    st.write("- Yeso")
    st.write("- Puzolana")

# -----------------------------------
# ABASTECIMIENTO
# -----------------------------------
elif menu == "Abastecimiento":

    st.header("Plan de Abastecimiento")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Arribos programados")
        st.write("- Caliza: 15 marzo")
        st.write("- Yeso: 18 marzo")
        st.write("- Puzolana: 20 marzo")

    with col2:
        st.subheader("Ubicación de almacenamiento")
        st.write("- Caliza: Patio Norte")
        st.write("- Yeso: Patio Sur")
        st.write("- Puzolana: Patio Horno")
