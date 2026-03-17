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
st.caption("Vista operativa del turno")

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
    ],
    key="menu"
)

# -------- ESTILOS --------
st.markdown("""
<style>
.kpi-card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    border-left: 6px solid #1f4e79;
    text-align: center;
}
.kpi-title {
    font-size: 15px;
    color: #5b6570;
    margin-bottom: 8px;
}
.kpi-value {
    font-size: 34px;
    font-weight: 700;
    color: #1f1f1f;
}
.block-card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    min-height: 320px;
}
.block-title {
    font-size: 20px;
    font-weight: 700;
    color: #1f4e79;
    margin-bottom: 10px;
}
.small-note {
    font-size: 13px;
    color: #6b7280;
}
.quick-btn {
    background-color: #1f4e79;
    color: white;
    padding: 14px;
    border-radius: 14px;
    text-align: center;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

if menu == "Inicio":
    st.subheader("Resumen operativo del turno")

    # KPIs visuales
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Cargadores disponibles</div>
            <div class="kpi-value">3</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Operadores en turno</div>
            <div class="kpi-value">4</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Supervisores en turno</div>
            <div class="kpi-value">1</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">MP programadas a llegar</div>
            <div class="kpi-value">2</div>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Recibido turno anterior</div>
            <div class="kpi-value">1.250 t</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Bloques centrales
    left, right = st.columns(2)

    with left:
        st.markdown("""
        <div class="block-card">
            <div class="block-title">Materias primas programadas a llegar</div>
            <div class="small-note">Programación del turno actual</div>
        </div>
        """, unsafe_allow_html=True)

        df_programadas = pd.DataFrame({
            "Materia prima": ["Caliza", "Yeso"],
            "Cantidad (ton)": [2500, 800],
            "Ubicación prevista": ["Patio Norte", "Patio Sur"]
        })
        st.dataframe(df_programadas, use_container_width=True, hide_index=True)

    with right:
        st.markdown("""
        <div class="block-card">
            <div class="block-title">Material recibido en el turno anterior</div>
            <div class="small-note">Recepción ejecutada y ubicación asignada</div>
        </div>
        """, unsafe_allow_html=True)

        df_recibido = pd.DataFrame({
            "Materia prima": ["Caliza", "Puzolana"],
            "Cantidad (ton)": [900, 350],
            "Ubicación": ["Patio Norte", "Patio 3"]
        })
        st.dataframe(df_recibido, use_container_width=True, hide_index=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### Acceso rápido")

    q1, q2, q3 = st.columns(3)
    q4, q5, q6 = st.columns(3)

    with q1:
        if st.button("🚜 Equipos operativos", use_container_width=True):
            go_to("Equipos operativos")

    with q2:
        if st.button("👷 Gestión de personal", use_container_width=True):
            go_to("Gestión de personal")

    with q3:
        if st.button("🚢 Descargues 2026", use_container_width=True):
            go_to("Descargues 2026")

    with q4:
        if st.button("🏗️ Organización MP", use_container_width=True):
            go_to("Organización de materias primas")

    with q5:
        if st.button("📦 Abastecimiento", use_container_width=True):
            go_to("Abastecimiento")

    with q6:
        if st.button("📊 Inventarios", use_container_width=True):
            go_to("Inventarios y desviaciones")

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
