import streamlit as st
from brl import brl
from gtts import gTTS
import os

# Título de la aplicación
st.title("Aplicación de Apoyo para Niños Ciegos")

# Función para convertir texto a braille
def texto_a_braille(texto):
    return brl.text_to_braille(texto)

# Función para convertir braille a texto
def braille_a_texto(braille):
    return brl.braille_to_text(braille)

# Función para convertir texto a audio
def texto_a_audio(texto, archivo_audio="salida.mp3"):
    tts = gTTS(text=texto, lang="es")
    tts.save(archivo_audio)
    return archivo_audio

# Interfaz de la aplicación
st.sidebar.title("Opciones")
opcion = st.sidebar.selectbox(
    "Selecciona una funcionalidad:",
    ["Texto a Braille", "Braille a Texto", "Texto a Audio"]
)

if opcion == "Texto a Braille":
    st.header("Texto a Braille")
    texto = st.text_area("Ingresa el texto que deseas convertir a braille:")
    if texto:
        braille = texto_a_braille(texto)
        st.write("Código Braille:")
        st.code(braille)

elif opcion == "Braille a Texto":
    st.header("Braille a Texto")
    braille = st.text_area("Ingresa el código braille que deseas convertir a texto:")
    if braille:
        texto = braille_a_texto(braille)
        st.write("Texto:")
        st.write(texto)

elif opcion == "Texto a Audio":
    st.header("Texto a Audio")
    texto = st.text_area("Ingresa el texto que deseas convertir a audio:")
    if texto:
        archivo_audio = texto_a_audio(texto)
        st.audio(archivo_audio, format="audio/mp3")
        os.remove(archivo_audio)  # Eliminar el archivo temporal
