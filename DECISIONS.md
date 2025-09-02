# Documento de Decisões Técnicas

Este arquivo documenta as principais decisões técnicas tomadas durante o desenvolvimento do projeto de Monitoramento de Percepção Pública sobre IA no Piauí, conforme solicitado nos critérios do case.

## 1. Escolha da Abordagem para Análise de Sentimento

**Pergunta:** *Por que você escolheu a abordagem de regras para análise de sentimento (em vez de um modelo de ML)?* 

A decisão de utilizar uma abordagem baseada em regras foi estratégica baseado na velocidade de entrega e alinhada aos objetivos e ao escopo deste projeto, pelos seguintes motivos:

* **Simplicidade, Prazo e Rapidez na Implementação:** Para um projeto com o objetivo de entregar um pipeline funcional (coleta → processamento → visualização), a abordagem de regras é significativamente mais rápida de implementar do que um pipeline de Machine Learning, que exigiria coleta de dados, treinamento, validação e deploy do modelo.

* **Transparência e Interpretabilidade:** As regras, baseadas em listas de palavras-chave positivas e negativas, são totalmente transparentes. É fácil entender por que uma notícia foi classificada de uma certa maneira, o que está em sintonia com o critério de "Ética e Transparência" do case. Modelos de ML podem funcionar como "caixas-pretas", dificultando a justificativa de uma classificação.

* **Adequação ao Escopo do Case:** A tarefa testa habilidades fundamentais de manipulação de dados, lógica de programação e uso de bibliotecas como Pandas e Streamlit. Uma abordagem de regras permite focar e demonstrar proficiência nessas habilidades essenciais sem adicionar a complexidade de bibliotecas de ML, que poderiam desviar o foco do objetivo central.

* **Customização e Controle:** O léxico de palavras positivas e negativas pode ser facilmente editado e customizado para o contexto específico de notícias sobre tecnologia e políticas públicas no Piauí, oferecendo um controle fino e direto sobre o resultado da análise.

## 2. Tratamento de Erros e Falta de Dados

**Pergunta:** *Como você lidou com possíveis erros ou falta de notícias no feed RSS?* 

A robustez do script foi uma prioridade. Para lidar com falhas, a estratégia foi implementada em várias camadas no arquivo `coletor.py`:

* **Falhas de Conexão (Erros HTTP):** A requisição ao feed RSS do Google Notícias é feita dentro de um bloco `try...except`. Especificamente, `except requests.exceptions.RequestException` captura qualquer erro relacionado à conexão com a internet ou resposta do servidor (ex: site fora do ar, erro 500). Em caso de falha, uma mensagem de erro é exibida no terminal e o script encerra a execução de forma controlada, retornando um DataFrame vazio.

* **Erros de Formato de Dados (Parsing de XML):** O conteúdo do feed pode, eventualmente, não ser um XML válido. Para prevenir isso, o processamento do XML também está protegido por um `try...except ET.ParseError`. Se o parsing falhar, uma mensagem de erro é mostrada e o script também retorna um DataFrame vazio.

* **Falta de Notícias no Feed:** É possível que a busca por "Inteligência Artificial Piauí" não retorne nenhuma notícia. O código lida com isso de duas formas:
    1.  Após tentar extrair os itens, o script verifica se a lista de notícias está vazia (`if not noticias:`). Se estiver, ele exibe um aviso claro ("Aviso: Nenhuma notícia foi encontrada...") e retorna um DataFrame vazio.
    2.  A função principal (`processar_dados`) verifica se o DataFrame recebido está vazio (`if not df.empty:`). Se estiver, ela informa ao usuário que "Nenhum dado foi processado" e não tenta executar as etapas de limpeza ou salvamento, evitando erros subsequentes.

Essa abordagem garante que o script seja resiliente, forneça feedback claro ao usuário em caso de falhas e nunca quebre de forma inesperada.

## 3. Uso de Inteligência Artificial no Desenvolvimento

Conforme solicitado pelo critério de "Ética e Transparência", detalho abaixo como a Inteligência Artificial foi utilizada como ferramenta de apoio durante o desenvolvimento deste projeto.

Utilizei um modelo de linguagem avançado (Google Gemini) como um "programador em par" (pair programmer) e assistente de desenvolvimento para acelerar e aprimorar diversas etapas do processo:

1. **Geração de Código Base (Boilerplate):** A estrutura inicial das funções em Python, como a lógica para fazer requisições HTTP com a biblioteca requests e o processamento inicial de XML, foi gerada com o auxílio da IA com base nos requisitos do case.

2. **Consultoria e Boas Práticas:** Utilizei a IA como uma ferramenta de aprendizado para tirar dúvidas conceituais importantes, como a configuração de ambientes virtuais, a explicação detalhada do funcionamento do código gerado e a formulação de boas práticas de versionamento com Git, incluindo a estruturação de mensagens de commit.

3. **Depuração Assistida (Debugging):** Durante o desenvolvimento, ao encontrar erros (como ModuleNotFoundError e falhas na execução dos scripts), os logs e mensagens de erro foram apresentados à IA para obter uma análise e possíveis caminhos para a solução, o que agilizou significativamente o processo de depuração.

É importante ressaltar que todo o código gerado foi revisado, entendido, testado e integrado por mim. Fui responsável pela direção estratégica do projeto, pela depuração final e implementação das soluções, pela configuração completa do ambiente de desenvolvimento e pela estruturação final do repositório, garantindo que todos os requisitos funcionais e de documentação do case fossem atendidos. A IA atuou como uma poderosa ferramenta de suporte, mas a responsabilidade e a autoria da solução final são minhas.