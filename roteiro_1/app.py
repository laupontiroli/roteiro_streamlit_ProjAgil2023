import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")

frase = st.text_input("escreva uma frase aqui")

if st.button("Veja sua frase!"):
    st.write(frase)
