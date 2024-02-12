# Importar el módulo de Streamlit
import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor de la app
st.write("Esta app fue elaborada por SANTI")

# Preguntar al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Verificar si se ingresó un nombre
if nombre_usuario:
    # Mostrar mensaje de bienvenida
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
