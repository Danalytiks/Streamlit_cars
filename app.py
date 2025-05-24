import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho
st.header("🚗 Used Car Listings — Interactive Dashboard")

# Carregando os dados
car_data = pd.read_csv('vehicles.csv')  # ou 'vehicles_us.csv' dependendo do nome

# Checkbox para histograma
if st.checkbox('Mostrar histograma de odômetro'):
    st.write('📊 Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para scatter plot
if st.checkbox('Mostrar gráfico de dispersão preço vs odômetro'):
    st.write('📉 Criando gráfico de dispersão entre preço e odômetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)