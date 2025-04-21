import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.subheader("Exploracion interactiva")

df = pd.read_csv("data/pisos.csv")

st.dataframe(df)

st.sidebar.header("Filtros")
# 1. Input
barrios = st.sidebar.multiselect("Barrio", df["barrio"].unique())

precio_min, precio_max = df["precio"].min(), df["precio"].max()
precio = st.sidebar.slider("Precio", precio_min, precio_max, (precio_min, precio_max))

habitaciones = st.sidebar.slider("Habitaciones", df["habitaciones"].min(), df["habitaciones"].max(), (df["habitaciones"].min(), df["habitaciones"].max()))

# 2. Filter
df_filtrado = df[
    (df["barrio"].isin(barrios)) &
    (df["precio"].between(precio[0], precio[1])) &
    (df["habitaciones"].between(habitaciones[0], habitaciones[1]))
]

st.write("Tus resultados:")
st.dataframe(df_filtrado)

st.subheader("Histograma de precios")
st.plotly_chart(px.histogram(df_filtrado, x="precio"))

st.subheader("Boxplot de precios por barrio")
st.plotly_chart(px.box(df_filtrado, x="barrio", y="precio"))


