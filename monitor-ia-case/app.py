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

with col1:
    # Gráfico de Pizza com distribuição de sentimentos
    st.subheader("Distribuição de Sentimentos")
    sentimento_counts = df['sentimento'].value_counts()
    fig_pie = px.pie(
        sentimento_counts, 
        values=sentimento_counts.values, 
        names=sentimento_counts.index,
        title='Sentimentos nas Notícias',
        color=sentimento_counts.index,
        color_discrete_map={'Positivo':'green', 'Negativo':'red', 'Neutro':'grey'}
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    # Nuvem de Palavras
    st.subheader("Nuvem de Palavras Frequentes")
    texto_completo = " ".join(review for review in df.texto_limpo.astype(str))
    
    if texto_completo.strip():
        wordcloud = WordCloud(
            background_color="white",
            width=800,
            height=400,
            max_words=100
        ).generate(texto_completo)
        
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("Não há texto suficiente para gerar a nuvem de palavras.")

# Tabela interativa com os dados
st.subheader("Notícias Coletadas")
st.dataframe(df[['titulo', 'sentimento', 'link']])

# Rodapé com aviso sobre limitações, conforme requisito de Ética 
st.markdown("---")
st.write(
    """
    **Aviso de Limitações:** Esta análise de sentimento é baseada em regras simples
    e pode não capturar sarcasmo ou contextos complexos.
    """
)