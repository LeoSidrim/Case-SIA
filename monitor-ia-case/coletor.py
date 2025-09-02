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
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        noticias = []
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

def limpar_texto(texto):
    """
    Remove tags HTML e caracteres especiais de um texto.
    """
    if not isinstance(texto, str):
        return ""
    texto_limpo = re.sub(r'<.*?>', '', texto)
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto_limpo)
    return texto_limpo.lower()

def analisar_sentimento(texto):
    """
    Analisa o sentimento de um texto com base em listas de palavras.
    """
    palavras_positivas = ['avanço', 'crescimento', 'inova', 'oportunidade', 'desenvolve', 'melhora', 'beneficia', 'impulsiona', 'investimento', 'qualidade']
    palavras_negativas = ['risco', 'ameaça', 'desemprego', 'problema', 'preocupação', 'desafio', 'impacto negativo', 'perigo', 'crise', 'dificuldade']
    
    score = 0
    texto_lower = texto.lower()
    for palavra in palavras_positivas:
        if palavra in texto_lower:
            score += 1
    for palavra in palavras_negativas:
        if palavra in texto_lower:
            score -= 1
            
    if score > 0:
        return 'Positivo'
    elif score < 0:
        return 'Negativo'
    else:
        return 'Neutro'

def processar_dados():
    """
    Pipeline completo: busca, limpa, analisa e salva os dados.
    """
    print("Iniciando a coleta de notícias...")
    df = buscar_noticias_google_news()
    
    if not df.empty:
        print("Processando os dados coletados...")
        df['texto_completo'] = df['titulo'] + ' ' + df['descricao']
        df['texto_limpo'] = df['texto_completo'].apply(limpar_texto)
        df['sentimento'] = df['texto_limpo'].apply(analisar_sentimento)
        
        df.to_csv('noticias.csv', index=False)
        print("Dados coletados e processados com sucesso! Salvo em noticias.csv")
    else:
        print("Nenhum dado para processar. O arquivo noticias.csv não foi criado.")

# --- PONTO DE PARTIDA DO SCRIPT ---
# Este bloco verifica se o script está sendo executado diretamente
# e, em caso afirmativo, chama a função principal para iniciar o processo.
if __name__ == "__main__":
    processar_dados()