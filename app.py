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
# -----------------------------------
# EQUIPOS
# -----------------------------------
elif menu == "Equipos":

    st.header("Equipos Operativos")

    # RESUMEN GENERAL
    st.markdown("### Resumen de equipos")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Disponibles", "2", delta="66.7% flota")
    with c2:
        st.metric("En mantenimiento", "1", delta="33.3% flota")
    with c3:
        st.metric("Horas acumuladas", "368 h")
    with c4:
        st.metric("Combustible promedio", "62%")

    st.markdown("---")

    # DETALLE DE EQUIPOS
    st.markdown("### Estado por equipo")

    equipos = [
        {
            "nombre": "Cargador 102",
            "estado": "Disponible",
            "horas": 120,
            "combustible": 85,
            "proximo_mtto": 20,
            "ultimo_mtto": "OK"
        },
        {
            "nombre": "Cargador 103",
            "estado": "En operación",
            "horas": 98,
            "combustible": 60,
            "proximo_mtto": 35,
            "ultimo_mtto": "OK"
        },
        {
            "nombre": "Cargador 109",
            "estado": "En mantenimiento",
            "horas": 150,
            "combustible": 40,
            "proximo_mtto": 0,
            "ultimo_mtto": "Observación"
        }
    ]

    cols = st.columns(3)

    for col, eq in zip(cols, equipos):
        with col:
            st.markdown(f"#### 🚜 {eq['nombre']}")

            if eq["estado"] == "Disponible":
                st.success("🟢 Disponible")
            elif eq["estado"] == "En operación":
                st.info("🔵 En operación")
            else:
                st.error("🔴 En mantenimiento")

            st.write(f"**Horas trabajadas:** {eq['horas']} h")
            st.write(f"**Combustible:** {eq['combustible']}%")

            if eq["proximo_mtto"] > 0:
                st.write(f"**Próximo mtto:** {eq['proximo_mtto']} h")
            else:
                st.write("**Próximo mtto:** En proceso")

            st.write(f"**Último mtto:** {eq['ultimo_mtto']}")

            # ALERTAS OPERATIVAS
            if eq["combustible"] < 50 and eq["estado"] != "En mantenimiento":
                st.warning("⚠️ Requiere programación de abastecimiento de combustible.")

            if eq["proximo_mtto"] > 0 and eq["proximo_mtto"] <= 20:
                st.warning("⚠️ Programar mantenimiento preventivo en corto plazo.")

    st.markdown("---")

    # OTROS EQUIPOS
    st.markdown("### Otros equipos críticos")
    col4, col5 = st.columns(2)

    with col4:
        st.markdown("#### 🧼 Lavaruedas")
        st.success("🟢 Operativo")
        st.write("**Estado actual:** Disponible")
        st.write("**Última revisión:** OK")
        st.write("**Observación:** Sin restricciones operativas.")

    with col5:
        st.markdown("#### 🟫 Parrillas")
        st.success("🟢 Operativas")
        st.write("**Estado actual:** Sin novedad")
        st.write("**Última revisión:** OK")
        st.write("**Observación:** Aptas para descargue continuo.")

    st.markdown("---")

    # RECOMENDACIÓN GERENCIAL
    st.markdown("### Recomendación operativa")

    st.info("""
    **Conclusión del estado de flota:**
    
    La operación cuenta actualmente con **2 equipos disponibles de 3**, lo que permite atender la demanda actual;
    sin embargo, se identifica una **condición de atención prioritaria** sobre el **Cargador 102**, debido a su cercanía
    al mantenimiento preventivo, y sobre el **Cargador 109**, que permanece fuera de servicio.

    **Acciones sugeridas:**
    - Programar el mantenimiento preventivo del **Cargador 102** antes de alcanzar el límite operativo.
    - Hacer seguimiento al cierre del mantenimiento del **Cargador 109** para recuperar disponibilidad de flota.
    - Mantener control diario de combustible y horas trabajadas para evitar afectaciones al descargue.
    """)
# -----------------------------------
# PERSONAL
# -----------------------------------
elif menu == "Personal":

    st.header("Gestión de Personal")

    # KPIs GENERALES
    st.markdown("### Resumen de personal")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Operadores en turno", "2")
    with col2:
        st.metric("Supervisor en turno", "1")
    with col3:
        st.metric("Cobertura operativa", "100%")
    with col4:
        st.metric("Turnos críticos", "0")

    st.markdown("---")

    # DISTRIBUCIÓN DEL TURNO
    st.markdown("### Distribución del turno actual")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 👷 Operador 1")
        st.success("🟢 Activo")
        st.write("**Equipo asignado:** Cargador 102")
        st.write("**Ubicación:** Patio Norte")
        st.write("**Turno:** Día")
        st.write("**Observación:** Sin novedad")

    with col2:
        st.markdown("#### 👷 Operador 2")
        st.success("🟢 Activo")
        st.write("**Equipo asignado:** Cargador 103")
        st.write("**Ubicación:** Patio Sur")
        st.write("**Turno:** Día")
        st.write("**Observación:** Sin novedad")

    with col3:
        st.markdown("#### 👨‍💼 Supervisor")
        st.success("🟢 Activo")
        st.write("**Responsabilidad:** Supervisión general")
        st.write("**Cobertura:** Operación MP")
        st.write("**Turno:** Día")
        st.write("**Observación:** Seguimiento operativo")

    st.markdown("---")

    # ESTADO OPERATIVO
    st.markdown("### Estado de cobertura")

    col4, col5 = st.columns(2)

    with col4:
        st.info("""
        **Cobertura actual**
        
        La operación cuenta con la totalidad del personal requerido para atender
        las actividades programadas del turno.
        """)

    with col5:
        st.success("""
        **Condición operativa**
        
        No se presentan vacantes, ausencias ni restricciones de personal
        que afecten la continuidad de la operación.
        """)

    st.markdown("---")

    # ALERTAS Y RECOMENDACIONES
    st.markdown("### Recomendación operativa")

    st.info("""
    **Conclusión del estado de personal:**
    
    La operación mantiene una **cobertura del 100%** en el turno actual, con asignación
    completa de operadores y supervisión activa, lo que permite sostener la atención
    de descargues y movimiento de materias primas sin restricciones por recurso humano.

    **Acciones sugeridas:**
    - Mantener seguimiento a la asignación diaria por equipo y frente de trabajo.
    - Verificar relevo oportuno en cambios de turno para evitar tiempos muertos.
    - Asegurar comunicación continua entre operadores y supervisor ante cambios en la operación.
    """)

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
