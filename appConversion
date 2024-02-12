import streamlit as st

def temperatura():
    st.subheader("Conversión de Temperatura")
    opciones_temperatura = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    seleccion_temperatura = st.selectbox("Selecciona el tipo de conversión", opciones_temperatura)

    if seleccion_temperatura == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingresa la temperatura en Celsius", value=0.0)
        fahrenheit = (celsius * 9/5) + 32
        st.write(f"{celsius} grados Celsius son equivalentes a {fahrenheit:.2f} grados Fahrenheit")

    # Resto de las conversiones de temperatura, similar al ejemplo anterior

def longitud():
    # Función para la conversión de longitud
    # Implementa lógica similar a la de la función temperatura

def peso_masa():
    # Función para la conversión de peso/masa
    # Implementa lógica similar a la de la función temperatura

# Repite el proceso para las demás categorías de conversión

# Categorías disponibles
categorias = {
    "Temperatura": temperatura,
    "Longitud": longitud,
    "Peso/Masa": peso_masa,
    # Agrega más categorías según sea necesario
}

# Configuración de la app
st.title("Conversor Universal")
st.sidebar.subheader("Selecciona una categoría")
categoria_seleccionada = st.sidebar.selectbox("", list(categorias.keys()))

# Llama a la función correspondiente a la categoría seleccionada
categorias[categoria_seleccionada]()
