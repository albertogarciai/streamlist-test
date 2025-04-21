import streamlit as st
import pandas as pd

st.title("🏠 Prediccion de precios de casas")

st.write("Tasador")

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

