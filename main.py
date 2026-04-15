# No lugar do loop antigo, use este:
for f in range(fileiras):
    # Criamos as colunas com larguras fixas para não deixar o celular empilhar
    c1, c2, corr, c3, c4 = st.columns([1, 1, 0.4, 1, 1]) 
    
    # Poltrona 1 e 2 (Lado Esquerdo)
    with c1:
        n1 = f * 4 + 1
        if n1 <= total_lugares:
            is_sel = n1 in st.session_state.ocupadas
            if st.button(f"{n1}", key=f"p{n1}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(n1)
                else: st.session_state.ocupadas.add(n1)
                st.rerun()
    with c2:
        n2 = f * 4 + 2
        if n2 <= total_lugares:
            is_sel = n2 in st.session_state.ocupadas
            if st.button(f"{n2}", key=f"p{n2}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(n2)
                else: st.session_state.ocupadas.add(n2)
                st.rerun()

    # Coluna corr (Corredor) fica vazia
    with corr:
        st.write("")

    # Poltrona 3 e 4 (Lado Direito)
    with c3:
        n3 = f * 4 + 3
        if n3 <= total_lugares:
            is_sel = n3 in st.session_state.ocupadas
            if st.button(f"{n3}", key=f"p{n3}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(n3)
                else: st.session_state.ocupadas.add(n3)
                st.rerun()
    with c4:
        n4 = f * 4 + 4
        if n4 <= total_lugares:
            is_sel = n4 in st.session_state.ocupadas
            if st.button(f"{n4}", key=f"p{n4}", type="primary" if is_sel else "secondary"):
                if is_sel: st.session_state.ocupadas.remove(n4)
                else: st.session_state.ocupadas.add(n4)
                st.rerun()
