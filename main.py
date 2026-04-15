import streamlit as st

# Configuração da página para parecer um App
st.set_page_config(page_title="Checklist de Frota", layout="centered")

st.title("🚌 Conferência de Poltronas")
st.write("Selecione as poltronas ocupadas conforme a inspeção:")

# 1. Seleção do tipo de ônibus
tipo_onibus = st.selectbox("Tipo de Frota", ["42 Lugares", "46 Lugares", "50 Lugares"])
total_lugares = int(tipo_onibus.split()[0])

# 2. Criando o Mapa de Poltronas
# Usamos o estado da sessão para manter os cliques salvos
if 'ocupadas' not in st.session_state:
    st.session_state.ocupadas = set()

cols = st.columns(4) # Simula o corredor do ônibus (2 poltronas de cada lado)

for i in range(1, total_lugares + 1):
    col_idx = (i-1) % 4
    with cols[col_idx]:
        # Botão para cada poltrona
        label = f"P{i}"
        is_selected = i in st.session_state.ocupadas
        
        if st.button(label, key=f"btn_{i}", type="primary" if is_selected else "secondary"):
            if is_selected:
                st.session_state.ocupadas.remove(i)
            else:
                st.session_state.ocupadas.add(i)
            st.rerun()

st.divider()

# 3. Resumo e Contador
contagem_atual = len(st.session_state.ocupadas)
st.metric("Total de Ocupadas", contagem_atual)

# 4. Validação
manifesto = st.number_input("Qtd. no Manifesto (Papel)", min_value=0, step=1)

if st.button("Finalizar Conferência"):
    if contagem_atual == manifesto:
        st.success(f"Conferência batida! {contagem_atual} passageiros.")
        # Aqui no futuro enviamos para o seu banco de dados
    else:
        st.error(f"Divergência detectada! No App: {contagem_atual} | No Manifesto: {manifesto}")

if st.button("Limpar Tudo"):
    st.session_state.ocupadas = set()
    st.rerun()
