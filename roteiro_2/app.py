import streamlit as st

st.title("Roteiro 2: Widgets Interativos")

value_slider = st.slider("Escolha um valor", 0, 100)
value_selectbox = st.selectbox("Escolha seu gênero",options=("feminino","masculino","outro"),index=None,placeholder="Selecione seu gênero",)
value_checkbox = st. checkbox('Eu sou uma pessoa não um computador')
value_radio = st.radio("Escolha sua escolaridade do momento",("fundamental","médio","superior",'não estou estudando'))
value_toggle = st.toggle('Streamlit é legal')
if st.button("Mostrar valores"):
    st.write(f'''
Valor escolhido: {value_slider},
é humano : {value_checkbox},
escoliradade do momento : {value_radio},
streamlit é legal : {value_toggle},
gênero selecionado :
''',value_selectbox)
