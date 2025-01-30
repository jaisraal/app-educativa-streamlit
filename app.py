# app.py (versión compatible con openai>=1.0.0)
import streamlit as st
from openai import OpenAI

# Configura el cliente de OpenAI con tu clave
client = OpenAI(api_key=st.secrets["openai_api_key"])

def generar_respuesta(prompt):
    respuesta = client.completions.create(
        model="text-davinci-003",  # Usa "model" en lugar de "engine"
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    return respuesta.choices[0].text.strip()

# Interfaz de la aplicación
st.title("Aplicación Educativa Interactiva")
st.write("Resuelve problemas universitarios con la ayuda de IA")

# Campo de entrada para la pregunta
pregunta = st.text_area("Escribe tu pregunta o problema:")

# Botón para obtener la respuesta
if st.button("Obtener respuesta"):
    if pregunta:
        respuesta = generar_respuesta(pregunta)
        st.write("Respuesta:")
        st.write(respuesta)
    else:
        st.write("Por favor, ingresa una pregunta.")

# Generación de ejercicios
tema = st.text_input("Ingresa un tema para generar ejercicios:")
if st.button("Generar ejercicios"):
    if tema:
        prompt = f"Genera 3 ejercicios prácticos sobre {tema}"
        ejercicios = generar_respuesta(prompt)
        st.write("Ejercicios generados:")
        st.write(ejercicios)
    else:
        st.write("Por favor, ingresa un tema.")

# Evaluación de respuestas
respuesta_usuario = st.text_area("Escribe tu respuesta para evaluar:")
if st.button("Evaluar respuesta"):
    if respuesta_usuario:
        prompt = f"Evalúa la siguiente respuesta y proporciona retroalimentación: {respuesta_usuario}"
        feedback = generar_respuesta(prompt)
        st.write("Retroalimentación:")
        st.write(feedback)
    else:
        st.write("Por favor, ingresa una respuesta.")
