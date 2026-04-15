import streamlit as st

st.set_page_config(page_title="BusCheck Pro", layout="centered")

# CSS Minimalista para botões em linha
st.markdown("""
    <style>
    /* Força os botões a não pularem linha */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 5px !important;
    }
    button {
        width: 60px !important;
        height: 45px !important;
        padding: 0px !important;
    }
    .corredor {
        width: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚌 BusCheck")

if 'ocupadas' not in st.session_state:
    st.session_state.ocupadas = set()

# Configuração simples
total_lugares = st.number_input("Total de Poltronas", value=42, step=4)

st.write(f"### Ocupadas: {len(st.session_state.ocupadas)}")
st.caption("⬅️ Frente")

# Gerando as fileiras
fileiras = (total_lugares // 4) + (1 if total_lugares % 4 != 0 else 0)

for f in range(fileiras):
    # Criamos 5 colunas, mas a do meio é apenas um espaço
    c1, c2, corr, c3, c4 = st.columns([1, 1, 0.5, 1, 1])
    
    # Poltronas
    p_esq = [f * 4 + 1, f * 4 + 2]
    p_dir = [f * 4 + 3, f * 4 + 4]

    with c1:
        n = p_esq[0]
        if n <= total_lugares:
            if st.button(f"{n}", key=f"p{n}", type="primary" if n in st.session_state.ocupadas else "secondary"):
                if n in st.session_state.ocupadas: st.session_state.ocupadas.remove(n)
                else: st.session_state.ocupadas.add(n)
                st.rerun()
    with c2:
        n = p_esq[1]
        if n <= total_lugares:
            if st.button(f"{n}", key=f"p{n}", type="primary" if n in st.session_state.ocupadas else "secondary"):
                if n in st.session_state.ocupadas: st.session_state.ocupadas.remove(n)
                else: st.session_state.ocupadas.add(n)
                st.rerun()

    with corr:
        st.write(" ") # O corredor

    with c3:
        n = p_dir[0]
        if n <= total_lugares:
            if st.button(f"{n}", key=f"p{n}", type="primary" if n in st.session_state.ocupadas else "secondary"):
                if n in st.session_state.ocupadas: st.session_state.ocupadas.remove(n)
                else: st.session_state.ocupadas.add(n)
                st.rerun()
    with c4:
        n = p_dir[1]
        if n <= total_lugares:
            if st.button(f"{n}", key=f"p{n}", type="primary" if n in st.session_state.ocupadas else "secondary"):
                if n in st.session_state.ocupadas: st.session_state.ocupadas.remove(n)
                else: st.session_state.ocupadas.add(n)
                st.rerun()

st.divider()
if st.button("🗑️ Limpar Tudo", use_container_width=True):
    st.session_state.ocupadas = set()
    st.rerun()
