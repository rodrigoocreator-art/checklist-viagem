import streamlit as st

# Configuração da página
st.set_page_config(page_title="BusCheck Pro", layout="centered")

# CSS para forçar os botões a ficarem lado a lado no celular e reduzir espaços
st.markdown("""
    <style>
    div.stButton > button {
        width: 100% !important;
        height: 40px !important;
        padding: 0px !important;
        font-size: 12px !important;
    }
    [data-testid="column"] {
        padding: 1px !important;
        min-width: 0px !important;
    }
    .stApp {
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚌 BusCheck")

# Inicializa o estado das poltronas
if 'ocupadas' not in st.session_state:
    st.session_state.ocupadas = set()

# Configuração da Frota
tipo_onibus = st.selectbox("Selecione a Frota", ["42 Lugares", "46 Lugares", "50 Lugares"])
total_lugares = int(tipo_onibus.split()[0])

st.subheader(f"Ocupadas: {len(st.session_state.ocupadas)}")

# Cálculo de fileiras (4 poltronas por fileira)
fileiras = (total_lugares // 4) + (1 if total_lugares % 4 != 0 else 0)

st.caption("⬅️ Frente do Ônibus ➡️")
st.write("---")

# Renderização do Mapa
for f in range(fileiras):
    # Criamos 5 colunas: Janela, Corredor, Vazio(Corredor), Janela, Corredor
    c1, c2, corr, c3, c4 = st.columns([1, 1, 0.3, 1, 1])
    
    # Poltronas da Esquerda (1 e 2)
    with c1:
        p1 = f * 4 + 1
        if p1 <= total_lugares:
            is_sel = p1 in st.session_state.ocupadas
            if st.button(f"{p1}", key=f"p{p1}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(p1)
                else: st.session_state.ocupadas.add(p1)
                st.rerun()
    with c2:
        p2 = f * 4 + 2
        if p2 <= total_lugares:
            is_sel = p2 in st.session_state.ocupadas
            if st.button(f"{p2}", key=f"p{p2}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(p2)
                else: st.session_state.ocupadas.add(p2)
                st.rerun()

    # Corredor Central
    with corr:
        st.write("")

    # Poltronas da Direita (3 e 4)
    with c3:
        p3 = f * 4 + 3
        if p3 <= total_lugares:
            is_sel = p3 in st.session_state.ocupadas
            if st.button(f"{p3}", key=f"p{p3}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(p3)
                else: st.session_state.ocupadas.add(p3)
                st.rerun()
    with c4:
        p4 = f * 4 + 4
        if p4 <= total_lugares:
            is_sel = p4 in st.session_state.ocupadas
            if st.button(f"{p4}", key=f"p{p4}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(p4)
                else: st.session_state.ocupadas.add(p4)
                st.rerun()

st.write("---")

# Área de Finalização
manifesto = st.number_input("Passageiros no Manifesto", min_value=0, value=0, step=1)

col_fin1, col_fin2 = st.columns(2)
with col_fin1:
    if st.button("✅ Finalizar", use_container_width=True):
        if len(st.session_state.ocupadas) == manifesto:
            st.success("Tudo OK!")
        else:
            diff = len(st.session_state.ocupadas) - manifesto
            st.warning(f"Divergência: {diff:+}")

with col_fin2:
    if st.button("🗑️ Limpar", use_container_width=True):
        st.session_state.ocupadas = set()
        st.rerun()
