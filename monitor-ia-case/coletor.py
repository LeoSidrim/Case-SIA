import requests
import xml.etree.ElementTree as ET
import pandas as pd
import re

def buscar_noticias_google_news():
    """
    Busca notícias no feed RSS do Google Notícias e extrai os dados.
    """
    url = 'https://news.google.com/rss/search?q="Inteligência+Artificial"+Piauí+OR+"SIA+Piauí"&hl=pt-BR&gl=BR&ceid=BR:pt-419'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lança um erro para respostas HTTP ruins

        root = ET.fromstring(response.content)
        noticias = []
        # Limita a 15 notícias
        for item in root.findall('.//item')[:15]:
            titulo = item.find('title').text
            link = item.find('link').text
            descricao = item.find('description').text if item.find('description') is not None else ""
            
            noticias.append({
                'titulo': titulo,
                'link': link,
                'descricao': descricao
            })
        
        if not noticias:
            print("Aviso: Nenhuma notícia foi encontrada no feed RSS.")
            return pd.DataFrame()

        return pd.DataFrame(noticias)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição HTTP: {e}")
        return pd.DataFrame()
    except ET.ParseError as e:
        print(f"Erro ao processar o XML: {e}")
        return pd.DataFrame()

# Exemplo de como chamar a função
# df_noticias = buscar_noticias_google_news()
# print(df_noticias.head())