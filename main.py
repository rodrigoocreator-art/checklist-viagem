import streamlit as st

# Configuração para aproveitar melhor a tela do celular
st.set_page_config(page_title="Checklist Bus", layout="centered")

# CSS para deixar os botões menores e quadrados (estilo poltrona)
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 45px;
        padding: 0px;
        margin: 0px;
        font-size: 14px;
    }
    [data-testid="column"] {
        padding: 1px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚌 Conferência")

if 'ocupadas' not in st.session_state:
    st.session_state.ocupadas = set()

# Configuração da Frota
tipo_onibus = st.selectbox("Frota", ["42 Lugares", "46 Lugares", "50 Lugares"])
total_lugares = int(tipo_onibus.split()[0])

st.write(f"**Ocupadas: {len(st.session_state.ocupadas)}**")

# Criando o layout do ônibus (Janela | Corredor | Janela)
# Usamos 5 colunas: Janela(1), Corredor(2), Janela(4), Janela(5)
# A coluna 3 (índice 2) será o corredor vazio

st.caption("Frente do Ônibus")

# Calcula quantas fileiras são necessárias
fileiras = (total_lugares // 4) + (1 if total_lugares % 4 != 0 else 0)

for f in range(fileiras):
    cols = st.columns([1, 1, 0.5, 1, 1]) # Coluna do meio é o corredor
    
    # Mapeamento das poltronas para o layout 2x2
    posicoes = [0, 1, 3, 4] # Pula o índice 2 (corredor)
    
    for i, pos in enumerate(posicoes):
        num_poltrona = f * 4 + i + 1
        
        if num_poltrona <= total_lugares:
            with cols[pos]:
                is_selected = num_poltrona in st.session_state.ocupadas
                label = f"{num_poltrona}"
                
                if st.button(label, key=f"p_{num_poltrona}", type="primary" if is_selected else "secondary"):
                    if is_selected:
                        st.session_state.ocupadas.remove(num_poltrona)
                    else:
                        st.session_state.ocupadas.add(num_poltrona)
                    st.rerun()

st.divider()

# Finalização
manifesto = st.number_input("Qtd. no Manifesto", min_value=0, step=1)

c1, c2 = st.columns(2)
with c1:
    if st.button("✅ Finalizar"):
        if len(st.session_state.ocupadas) == manifesto:
            st.success("Conferência OK!")
        else:
            st.error(f"Erro: {len(st.session_state.ocupadas)} no App vs {manifesto} no Papel")

with c2:
    if st.button("🗑️ Limpar"):
        st.session_state.ocupadas = set()
        st.rerun()
