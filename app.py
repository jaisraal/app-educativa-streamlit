# app.py
import streamlit as st
import openai

# Configura tu clave de API de OpenAI
openai.api_key = st.secrets["openai_api_key"]

# Función para generar respuestas usando GPT
def generar_respuesta(prompt):
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
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