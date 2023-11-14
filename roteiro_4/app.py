import streamlit as st
import requests 

st.title("Roteiro 4: Integração com APIs")

pais = st.text_input("escreva o nome de um país")

if pais:
    try:
        response = requests.get(f'https://restcountries.com/v3.1/name/{pais}')
        response.raise_for_status()
        message = response.json()
        st.write(message)
    except Exception as e : 
        st.warning(e)

