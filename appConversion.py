import streamlit as st

def main():
    st.title("Conversor de Unidades")

    # Lista de opciones de conversión
    opciones_conversion = [
        "Conversiones de temperatura",
        "Conversiones de longitud",
        "Conversiones de peso/masa",
        "Conversiones de volumen",
        "Conversiones de tiempo",
        "Conversiones de velocidad",
        "Conversiones de área",
        "Conversiones de energía",
        "Conversiones de presión",
        "Conversiones de tamaño de datos"
    ]

    # Menú desplegable para seleccionar el tipo de conversión
    seleccion_conversion = st.selectbox("Selecciona el tipo de conversión:", opciones_conversion)

    st.write(f"Has seleccionado: {seleccion_conversion}")

if __name__ == "__main__":
    main()

