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
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Operadores en turno", "2")
    with col2:
        st.metric("Supervisor en turno", "1")
    with col3:
        st.metric("Cobertura operativa", "100%")
    with col4:
        st.metric("Accidentes (mes)", "1", delta="+1")
    with col5:
        st.metric("Días sin accidentes", "5")

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

    # ACCIDENTALIDAD
    st.markdown("### Seguridad y accidentalidad")

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("#### Personal propio")
        st.success("🟢 Sin accidentes recientes")
        st.write("**Accidentes mes:** 0")
        st.write("**Último evento:** Sin registro")
        st.write("**Severidad:** N/A")

    with col5:
        st.markdown("#### Personal externo")
        st.warning("🟡 Evento registrado")
        st.write("**Accidentes mes:** 1")
        st.write("**Tipo:** Golpe menor en maniobra")
        st.write("**Severidad:** Leve")
        st.write("**Estado:** Investigado")

    st.markdown("---")

    # ESTADO OPERATIVO
    st.markdown("### Estado de cobertura")

    col6, col7 = st.columns(2)

    with col6:
        st.info("""
        **Cobertura actual**
        
        La operación cuenta con la totalidad del personal requerido para atender
        las actividades programadas del turno.
        """)

    with col7:
        st.success("""
        **Condición operativa**
        
        No se presentan ausencias que afecten la continuidad; sin embargo,
        se mantiene monitoreo por condiciones de seguridad.
        """)

    st.markdown("---")

    # ALERTAS AUTOMÁTICAS
    st.markdown("### Alertas de seguridad")

    accidentes_mes = 1

    if accidentes_mes > 0:
        st.warning("⚠️ Se han registrado accidentes en el periodo. Reforzar controles operativos y HSE.")
    else:
        st.success("🟢 Sin eventos de seguridad registrados.")

    st.markdown("---")

    # RECOMENDACIÓN GERENCIAL
    st.markdown("### Recomendación operativa")

    st.info("""
    **Conclusión del estado de personal y seguridad:**
    
    La operación mantiene una **cobertura del 100%**, lo que garantiza continuidad operativa.
    No obstante, se registra **1 evento de accidentalidad en personal externo**, lo que indica
    la necesidad de reforzar controles en actividades de apoyo y contratistas.

    **Acciones sugeridas:**
    - Reforzar inducción de seguridad a personal externo antes de ingreso a operación.
    - Validar cumplimiento de procedimientos en maniobras de descargue.
    - Incrementar supervisión en frentes con participación de terceros.
    - Realizar retroalimentación operativa posterior al evento.
    """)
# -----------------------------------
# DESCARGUES
# -----------------------------------
elif menu == "Descargues":

    st.header("Descargues de Barcos")

    # -----------------------------------
    # DATOS BASE
    # -----------------------------------
    rata_pactada_dia = 7000
    max_dias_descargue = 5

    descargues = [
        {
            "material": "Clinker",
            "estado": "Actual",
            "ultimo_descargue": "16/03/2026",
            "ton_total_barco": 32000,
            "ton_descargadas": 14500,
            "dias_transcurridos": 2
        },
        {
            "material": "Yeso",
            "estado": "No actual",
            "ultimo_descargue": "10/03/2026",
            "ton_total_barco": 18000,
            "ton_descargadas": 18000,
            "dias_transcurridos": 3
        },
        {
            "material": "Escoria",
            "estado": "No actual",
            "ultimo_descargue": "05/03/2026",
            "ton_total_barco": 25000,
            "ton_descargadas": 25000,
            "dias_transcurridos": 4
        }
    ]

    # -----------------------------------
    # KPIs GENERALES
    # -----------------------------------
    activos = sum(1 for d in descargues if d["estado"] == "Actual")
    pendientes_total = sum(max(d["ton_total_barco"] - d["ton_descargadas"], 0) for d in descargues if d["estado"] == "Actual")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Barcos en descargue", activos)

    with col2:
        st.metric("Rata pactada", f"{rata_pactada_dia:,.0f} ton/día")

    with col3:
        st.metric("Horizonte máximo", f"{max_dias_descargue} días")

    with col4:
        st.metric("Pendiente por traer", f"{pendientes_total:,.0f} ton")

    st.markdown("---")

    # -----------------------------------
    # ESTADO POR MATERIAL
    # -----------------------------------
    st.markdown("### Estado por material")

    col1, col2, col3 = st.columns(3)

    for col, d in zip([col1, col2, col3], descargues):
        with col:
            st.markdown(f"#### 🚢 {d['material']}")

            pendiente = max(d["ton_total_barco"] - d["ton_descargadas"], 0)
            rata_real = d["ton_descargadas"] / d["dias_transcurridos"] if d["dias_transcurridos"] > 0 else 0
            porcentaje = d["ton_descargadas"] / d["ton_total_barco"] if d["ton_total_barco"] > 0 else 0
            cumplimiento = "Cumpliendo" if rata_real >= rata_pactada_dia else "No cumpliendo"

            # ESTADO
            if d["estado"] == "Actual":
                st.success("🟢 Estado: Actual")
            else:
                st.info(f"📅 Último descargue: {d['ultimo_descargue']}")

            # INFO GENERAL
            st.write(f"**Toneladas del barco:** {d['ton_total_barco']:,.0f} ton")
            st.write(f"**Toneladas descargadas:** {d['ton_descargadas']:,.0f} ton")
            st.write(f"**Pendiente por traer de puerto:** {pendiente:,.0f} ton")

            # % AVANCE
            st.write(f"**% traído a planta:** {porcentaje*100:,.1f}%")
            st.progress(porcentaje)

            # PRODUCTIVIDAD
            st.write(f"**Días transcurridos:** {d['dias_transcurridos']}")
            st.write(f"**Rata real:** {rata_real:,.0f} ton/día")

            # CUMPLIMIENTO
            if cumplimiento == "Cumpliendo":
                st.success("✅ Cumpliendo rata")
            else:
                st.warning("⚠️ Bajo la rata pactada")

    st.markdown("---")

    # -----------------------------------
    # RESUMEN OPERATIVO
    # -----------------------------------
    st.markdown("### Resumen operativo")

    actuales = [d for d in descargues if d["estado"] == "Actual"]

    if len(actuales) > 0:
        for d in actuales:
            pendiente = max(d["ton_total_barco"] - d["ton_descargadas"], 0)
            rata_real = d["ton_descargadas"] / d["dias_transcurridos"] if d["dias_transcurridos"] > 0 else 0
            porcentaje = d["ton_descargadas"] / d["ton_total_barco"] if d["ton_total_barco"] > 0 else 0

            st.info(f"""
            **{d['material']}**
            
            Avance de descargue: **{porcentaje*100:,.1f}%** del total del barco.
            
            Se han descargado **{d['ton_descargadas']:,.0f} ton** de **{d['ton_total_barco']:,.0f} ton**, 
            quedando pendientes **{pendiente:,.0f} ton** por traer de puerto.

            La rata actual es de **{rata_real:,.0f} ton/día** frente a una meta de 
            **{rata_pactada_dia:,.0f} ton/día**.
            """)
    else:
        st.info("Actualmente no hay descargues activos.")

    st.markdown("---")

    # -----------------------------------
    # CONCLUSIÓN AUTOMÁTICA
    # -----------------------------------
    st.markdown("### Recomendación operativa")

    if len(actuales) > 0:
        cumple_global = True

        for d in actuales:
            rata_real = d["ton_descargadas"] / d["dias_transcurridos"] if d["dias_transcurridos"] > 0 else 0

            if rata_real < rata_pactada_dia:
                cumple_global = False

        if cumple_global:
            st.success("""
            La operación de descargue presenta un desempeño adecuado, cumpliendo con la rata pactada
            y con un avance acorde al plan de atención del barco.
            """)
        else:
            st.warning("""
            Se presentan desviaciones frente a la rata de descargue. Se recomienda evaluar:
            - Disponibilidad de equipos
            - Continuidad de operación
            - Tiempos muertos en patio o muelle
            - Coordinación logística puerto-planta
            """)
    else:
        st.info("Sin descargues activos actualmente.")
# -----------------------------------
# INVENTARIOS
# -----------------------------------
elif menu == "Inventarios":

    st.header("Inventarios y Almacenamiento")

    # -----------------------------------
    # DATOS BASE
    # -----------------------------------
    espacios = [
        {
            "espacio": "Cubículo 1",
            "ocupacion": 82,
            "material": "MP2 / MP4",
            "recibiendo": "MP2",
            "consumiendo": "MP4",
            "tipo": "cubiculo_doble"
        },
        {
            "espacio": "Cubículo 2",
            "ocupacion": 75,
            "material": "MP3 / MP5",
            "recibiendo": "MP3",
            "consumiendo": "MP5",
            "tipo": "cubiculo_doble"
        },
        {
            "espacio": "Cubículo 3",
            "ocupacion": 68,
            "material": "MP6 / MP2",
            "recibiendo": "MP6",
            "consumiendo": "MP2",
            "tipo": "cubiculo_doble"
        },
        {
            "espacio": "Cubículo 4",
            "ocupacion": 91,
            "material": "MP4 / MP7",
            "recibiendo": "No aplica",
            "consumiendo": "MP4",
            "tipo": "cubiculo_doble"
        },
        {
            "espacio": "Cubículo 5",
            "ocupacion": 63,
            "material": "MP5 / MP6",
            "recibiendo": "MP5",
            "consumiendo": "MP6",
            "tipo": "cubiculo_doble"
        },
        {
            "espacio": "Cubículo 6",
            "ocupacion": 58,
            "material": "MP2",
            "recibiendo": "No aplica",
            "consumiendo": "MP2",
            "tipo": "simple"
        },
        {
            "espacio": "Salón",
            "ocupacion": 87,
            "material": "MP1",
            "recibiendo": "MP1",
            "consumiendo": "MP1",
            "tipo": "mp1_exclusivo"
        },
        {
            "espacio": "Domo",
            "ocupacion": 72,
            "material": "MP1",
            "recibiendo": "No aplica",
            "consumiendo": "MP1",
            "tipo": "mp1_exclusivo"
        },
        {
            "espacio": "Patio Horno",
            "ocupacion": 79,
            "material": "MP8",
            "recibiendo": "MP8",
            "consumiendo": "MP8",
            "tipo": "simple"
        },
        {
            "espacio": "Patio Abierto",
            "ocupacion": 66,
            "material": "MP9",
            "recibiendo": "MP9",
            "consumiendo": "No aplica",
            "tipo": "simple"
        }
    ]

    ocupacion_promedio = sum(e["ocupacion"] for e in espacios) / len(espacios)
    espacios_criticos = sum(1 for e in espacios if e["ocupacion"] >= 85)
    recibiendo_activos = sum(1 for e in espacios if e["recibiendo"] != "No aplica")
    consumiendo_activos = sum(1 for e in espacios if e["consumiendo"] != "No aplica")

    # -----------------------------------
    # KPIs GENERALES
    # -----------------------------------
    st.markdown("### Resumen de almacenamiento")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Espacios monitoreados", f"{len(espacios)}")
    with col2:
        st.metric("Ocupación promedio", f"{ocupacion_promedio:.1f}%")
    with col3:
        st.metric("Espacios críticos", espacios_criticos)
    with col4:
        st.metric("Frentes activos", f"{recibiendo_activos} recibo / {consumiendo_activos} consumo")

    st.markdown("---")

    # -----------------------------------
    # ESTADO POR ESPACIO
    # -----------------------------------
    st.markdown("### Estado por espacio de almacenamiento")

    cols = st.columns(2)

    for i, e in enumerate(espacios):
        with cols[i % 2]:
            st.markdown(f"#### 📦 {e['espacio']}")

            if e["ocupacion"] >= 90:
                st.error(f"🔴 Ocupación alta: {e['ocupacion']}%")
            elif e["ocupacion"] >= 75:
                st.warning(f"🟡 Ocupación media-alta: {e['ocupacion']}%")
            else:
                st.success(f"🟢 Ocupación controlada: {e['ocupacion']}%")

            st.progress(e["ocupacion"] / 100)

            st.write(f"**Material almacenado:** {e['material']}")
            st.write(f"**Recibiendo actualmente:** {e['recibiendo']}")
            st.write(f"**Consumo desde este espacio:** {e['consumiendo']}")

            if e["tipo"] == "cubiculo_doble":
                st.caption("Configuración: admite hasta 2 MP simultáneamente.")
            elif e["tipo"] == "mp1_exclusivo":
                st.caption("Configuración: uso exclusivo para MP1.")
            else:
                st.caption("Configuración: almacenamiento simple.")

    st.markdown("---")

    # -----------------------------------
    # REGLAS OPERATIVAS DEL ÁREA
    # -----------------------------------
    st.markdown("### Reglas operativas de almacenamiento")

    col5, col6 = st.columns(2)

    with col5:
        st.info("""
        **Reglas de segregación**
        
        - **Salón** y **Domo** son exclusivos para **MP1**.
        - **Cubículo 1 al 5** permiten almacenar **hasta 2 MP simultáneamente**.
        - **Cubículo 6**, **Patio Horno** y **Patio Abierto** operan como posiciones simples.
        """)

    with col6:
        st.info("""
        **Criterios de operación**
        
        - Se debe controlar ocupación por espacio.
        - Se debe visualizar qué material está entrando a cada posición.
        - Se debe identificar desde qué espacio se está alimentando la operación.
        """)

    st.markdown("---")

    # -----------------------------------
    # ALERTAS OPERATIVAS
    # -----------------------------------
    st.markdown("### Alertas de inventario")

    alertas = []

    for e in espacios:
        if e["ocupacion"] >= 90:
            alertas.append(f"{e['espacio']} presenta ocupación crítica ({e['ocupacion']}%).")

        if e["tipo"] == "mp1_exclusivo" and e["material"] != "MP1":
            alertas.append(f"{e['espacio']} tiene un material no permitido para su configuración.")

    if alertas:
        for alerta in alertas:
            st.warning(f"⚠️ {alerta}")
    else:
        st.success("🟢 No se identifican alertas operativas en almacenamiento.")

    st.markdown("---")

    # -----------------------------------
    # RECOMENDACIÓN OPERATIVA
    # -----------------------------------
    st.markdown("### Recomendación operativa")

    st.info(f"""
    La operación de almacenamiento presenta una **ocupación promedio de {ocupacion_promedio:.1f}%**,
    con **{espacios_criticos} espacios en condición crítica**.

    Actualmente se tienen **{recibiendo_activos} espacios recibiendo material** y
    **{consumiendo_activos} espacios desde los cuales se está consumiendo inventario**.

    **Acciones sugeridas:**
    - Priorizar liberación o redistribución de espacios con ocupación alta.
    - Verificar compatibilidad de materiales según tipo de almacenamiento.
    - Mantener seguimiento a los frentes activos de recibo y consumo.
    - Revisar balance entre ocupación, ingreso de material y puntos de consumo.
    """)
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
