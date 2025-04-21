import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Prediccion de precios",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.subheader("🏠 Prediccion de precios de casas")

tab1, tab2 = st.tabs(["Resumen", "Contacto"])

with tab1:
    st.subheader("Resumen del proyecto")
    st.write(
        """
        Este proyecto tiene como objetivo predecir el precio de una casa en función de sus características. 
        Utiliza un modelo de regresión entrenado con datos históricos de ventas de casas.
        """
    )

with tab2:
    st.subheader("Contacto")
    st.write(
        """
        Autor: Alberto Garcia

        Si tienes alguna pregunta o comentario, no dudes en contactarnos:
        - Email: alberto392g@gmail.com
        """
    )

