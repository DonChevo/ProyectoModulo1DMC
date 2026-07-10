import streamlit as st
st.title("Proyecto Módulo I Fundamentals")
st.sidebar.title("Parámetros")
st.image("Image20260709220523.png")
st.sidebar.image("Image20260709220550.png")
valor_inicial = st.number_input("Ingrese el valor inicial", value = 0)
valor_final = st.number_input("Ingrese el valor final", value = 1)

lista_numerica = list(range(valor_inicial, valor_final))

st.write(lista_numerica)
