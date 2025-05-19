import streamlit as st
import pandas as pd
import plotly.express as px

# Cabeçalho do app
st.header('📊 Análise de Carros Usados nos EUA')

# Leitura do CSV
car_data = pd.read_csv(r'/Users/dglotzbach/Library/CloudStorage/OneDrive-Persönlich/Documents/Data Science/Projeto Sprint_5/vehicles.csv')

# Mostrar as 5 primeiras linhas da tabela
st.write(car_data.head())

hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado

    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    import streamlit as st

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
  st.write('Criando um histograma para a coluna odometer')