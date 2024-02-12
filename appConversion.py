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

    # Diccionario con las opciones de conversión
    opciones_por_conversion = {
        "Conversiones de temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
        "Conversiones de longitud": ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"],
        "Conversiones de peso/masa": ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"],
        "Conversiones de volumen": ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"],
        "Conversiones de tiempo": ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"],
        "Conversiones de velocidad": ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"],
        "Conversiones de área": ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"],
        "Conversiones de energía": ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"],
        "Conversiones de presión": ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"],
        "Conversiones de tamaño de datos": ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    }

    # Desplegar las opciones de conversión correspondientes
    opciones_seleccionadas = opciones_por_conversion.get(seleccion_conversion, [])
    seleccion_conversion_secundaria = st.selectbox("Selecciona la conversión específica:", opciones_seleccionadas)

    st.write(f"Has seleccionado: {seleccion_conversion_secundaria}")

    # Entrada de datos
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    # Botón para realizar la conversión
    if st.button("Realizar Conversión"):
        resultado = realizar_conversion(seleccion_conversion_secundaria, valor_original)
        st.write(f"Resultado de la conversión: {resultado}")

def realizar_conversion(tipo_conversion, valor_original):
    # Lógica para realizar la conversión
    # Puedes expandir esta función según sea necesario
    
    # Ejemplo de conversión de temperatura: Celsius a Fahrenheit
    if tipo_conversion == "Celsius a Fahrenheit":
        resultado = (valor_original * 9/5) + 32
        return resultado
    
    # Ejemplo de conversión de longitud: Pies a Metros
    elif tipo_conversion == "Pies a metros":
        resultado = valor_original * 0.3048
        return resultado

    # Agrega más casos según sea necesario

if __name__ == "__main__":
    main()

