import streamlit as st

st.title("🧮 Mi Calculadora")

num1 = st.number_input("Primer número", value=0.0)
operacion = st.selectbox("Operación", ["+", "-", "×", "÷"])
num2 = st.number_input("Segundo número", value=0.0)

if st.button("Calcular"):
    if operacion == "+":
        st.success(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        st.success(f"Resultado: {num1 - num2}")
    elif operacion == "×":
        st.success(f"Resultado: {num1 * num2}")
    elif operacion == "÷":
        if num2 != 0:
            st.success(f"Resultado: {num1 / num2}")
        else:
            st.error("No se puede dividir entre cero")
