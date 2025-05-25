import streamlit as st
import pandas as pd
import plotly.express as px

# Cabeçalho do app
st.header("🚗 Análise de Carros Usados nos EUA")

# Leitura do dataset
df = pd.read_csv('vehicles_us.csv')

# Mostrar uma prévia dos dados
st.subheader("Prévia dos dados")
st.dataframe(df.dropna().head())

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

# Média de preço dos 10 modelos mais populares
st.subheader("💸 Preço médio dos 10 modelos mais anunciados")

# Seleciona os 10 modelos mais anunciados
top10_modelos = df['model'].value_counts().head(10).index

# Filtra o dataframe apenas para esses modelos
df_top10 = df[df['model'].isin(top10_modelos)]

# Agrupa e calcula média de preço
preco_medio_por_modelo = df_top10.groupby('model')['price'].mean().reset_index()
preco_medio_por_modelo = preco_medio_por_modelo.sort_values(by='price', ascending=False)

# Gráfico de barras
fig_precos = px.bar(
    preco_medio_por_modelo,
    x='model',
    y='price',
    title='💸 Preço médio dos 10 modelos mais anunciados',
    color='model',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

st.plotly_chart(fig_precos, use_container_width=True)
