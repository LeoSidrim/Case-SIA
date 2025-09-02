import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Configuração da página, define o texto no layout
st.set_page_config(layout="wide")
st.title("Painel de Monitoramento de Percepção sobre IA no Piauí")

# Carregar os dados do arquivo noticias gerado pelo código coletor que processa os dados
try:
    df = pd.read_csv('noticias.csv')
except FileNotFoundError:
    st.error("Arquivo 'noticias.csv' não encontrado. Execute o script 'coletor.py' primeiro para gerar os dados.")
    st.stop()

# --- Dashboard ---
col1, col2 = st.columns(2)

