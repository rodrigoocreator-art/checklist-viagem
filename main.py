import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="BusCheck Pro", layout="centered")

st.title("🚌 BusCheck")

# Inicializa o estado das poltronas
if 'ocupadas' not in st.session_state:
    st.session_state.ocupadas = []

# Configuração da Frota
tipo_onibus = st.selectbox("Frota", ["42 Lugares", "46 Lugares", "50 Lugares"])
total_lugares = int(tipo_onibus.split()[0])

# --- LÓGICA DE CLIQUE ---
# O HTML vai enviar o número da poltrona para o Python
query_params = st.query_params
if "p" in query_params:
    polt = int(query_params["p"])
    if polt in st.session_state.ocupadas:
        st.session_state.ocupadas.remove(polt)
    else:
        st.session_state.ocupadas.append(polt)
    # Limpa o parâmetro da URL para não ficar em loop
    st.query_params.clear()
    st.rerun()

# --- CONSTRUÇÃO DO MAPA EM HTML ---
# Isso aqui força o navegador do iPhone a desenhar 4 colunas fixas
html_code = """
<style>
    .bus-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 40px 1fr 1fr;
        gap: 8px;
        max-width: 350px;
        margin: auto;
        font-family: sans-serif;
    }
    .seat {
        height: 45px;
        background-color: #f0f2f6;
        border: 1px solid #d1d5db;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-weight: bold;
        text-decoration: none;
        color: black;
    }
    .seat.occupied {
        background-color: #2e7d32;
        color: white;
        border: none;
    }
    .aisle { width: 40px; }
</style>
<div class="bus-grid">
"""

fileiras = (total_lugares // 4) + (1 if total_lugares % 4 != 0 else 0)

for f in range(fileiras):
    for c in range(5):
        if c == 2: # Corredor
            html_code += '<div class="aisle"></div>'
        else:
            # Lógica para pular o corredor no cálculo do número
            col_ajustada = c if c < 2 else c - 1
            num = f * 4 + col_ajustada + 1
            
            if num <= total_lugares:
                is_occ = "occupied" if num in st.session_state.ocupadas else ""
                # O link recarrega a página passando o número da poltrona
                html_code += f'<a href="?p={num}" target="_self" class="seat {is_occ}">{num}</a>'
            else:
                html_code += '<div></div>'

html_code += "</div>"

# Renderiza o HTML no App
components.html(html_code, height=fileiras * 55)

st.divider()
st.subheader(f"Total Ocupadas: {len(st.session_state.ocupadas)}")

if st.button("🗑️ Resetar Contagem"):
    st.session_state.ocupadas = []
    st.rerun()
