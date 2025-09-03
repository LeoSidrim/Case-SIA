# Monitor IA Case - SIA

Um sistema de monitoramento em tempo real da percepção pública sobre Inteligência Artificial no estado do Piauí, desenvolvido para a **Secretaria de Inteligência Artificial do Piauí (SIA)**.

## 📋 Sobre o Projeto

Este projeto coleta automaticamente notícias sobre IA no Piauí através do Google News RSS, processa o conteúdo utilizando análise de sentimento e apresenta os resultados em um dashboard interativo desenvolvido com Streamlit.

## ✨ Funcionalidades

-  **Coleta Automática**: Busca notícias sobre IA no Piauí via Google News RSS
-  **Processamento de Texto**: Limpeza e normalização do conteúdo coletado
-  **Análise de Sentimento**: Classificação em Positivo, Negativo ou Neutro
-  **Dashboard Interativo**: Visualizações em tempo real com gráficos e tabelas
-  **Nuvem de Palavras**: Identificação dos termos mais frequentes
-  **Interface Responsiva**: Layout adaptável para diferentes dispositivos

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit** - Interface web interativa
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Gráficos interativos
- **WordCloud** - Geração de nuvem de palavras
- **Matplotlib** - Visualizações complementares
- **Requests** - Requisições HTTP
- **XML** - Processamento de feeds RSS

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/Case-SIA.git
cd Case-SIA/monitor-ia-case
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### Execução

1. **Execute o coletor de dados:**
```bash
python coletor.py
```
   Este comando irá:
   - Buscar as últimas notícias sobre IA no Piauí
   - Processar e analisar o sentimento
   - Salvar os dados em [`noticias.csv`](monitor-ia-case/noticias.csv)

2. **Inicie o dashboard:**
```bash
streamlit run app.py
```

3. **Acesse no navegador:**
   - O dashboard estará disponível em `http://localhost:8501`

## 📁 Estrutura do Projeto

|Pasta| Arquivo| Função |
|-|-|-|
|monitor-ia-case|[app.py](monitor-ia-case/app.py) | Dashboard Streamlit |
|monitor-ia-case| [coletor.py](monitor-ia-case/coletor.py)| Módulo de coleta e processamento |
|monitor-ia-case|[noticias.csv](monitor-ia-case/noticias.csv)| Dados gerados apartir do coletor.py|
monitor-ia-case|[requirements.txt](monitor-ia-case/requirements.txt)|Dependências do projeto|
## 📊 Componentes do Dashboard

### 1. Distribuição de Sentimentos
Gráfico de pizza mostrando a proporção de notícias classificadas como:
- 🟢 **Positivo**: Notícias com conotação favorável
- 🔴 **Negativo**: Notícias com conotação desfavorável  
- ⚫ **Neutro**: Notícias com conotação neutra

### 2. Nuvem de Palavras
Visualização das palavras mais frequentes nas notícias coletadas, destacando os principais temas e termos relacionados à IA no Piauí.

### 3. Tabela de Notícias
Lista interativa com:
- Títulos das notícias
- Classificação de sentimento
- Links para as fontes originais

## 🔧 Configurações

### Personalização da Busca

Para modificar os termos de busca, edite a URL no arquivo [`coletor.py`](monitor-ia-case/coletor.py):

```python
url = 'https://news.google.com/rss/search?q="Inteligência+Artificial"+Piauí+OR+"SIA+Piauí"&hl=pt-BR&gl=BR&ceid=BR:pt-419'
```

### Análise de Sentimento

As palavras-chave para análise podem ser personalizadas na função [`analisar_sentimento()`](monitor-ia-case/coletor.py):

```python
palavras_positivas = ['avanço', 'crescimento', 'inova', ...]
palavras_negativas = ['risco', 'ameaça', 'desemprego', ...]
```

## ⚠️ Limitações e Considerações Éticas

- A análise de sentimento é baseada em regras simples e pode não capturar nuances como sarcasmo ou contextos complexos
- Os dados são coletados de fontes públicas (Google News RSS)
- Recomenda-se validação manual para análises críticas
- O sistema respeita os termos de uso das APIs utilizadas




**Desenvolvido por Leonardo Sidrim para Case - SIA**