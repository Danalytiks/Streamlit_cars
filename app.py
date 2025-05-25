import streamlit as st
import pandas as pd
import plotly.express as px

# Cabeçalho do app
st.header("🚗 Análise de Carros Usados nos EUA")

# Leitura do dataset
df = pd.read_csv('vehicle.csv')

# Mostrar uma prévia dos dados
st.subheader("Prévia dos dados")
st.dataframe(df.head())

# Caixa para histograma
if st.checkbox("Mostrar Histograma"):
    st.write("Criando um histograma para a coluna 'odometer'")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Caixa para gráfico de dispersão
if st.checkbox("Mostrar Gráfico de Dispersão"):
    st.write("Gráfico de dispersão entre preço e quilometragem")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)