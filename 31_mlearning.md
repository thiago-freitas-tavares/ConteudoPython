# Machine Learning

- Execução no Jupyter - Salvo no Repositório MachineLearning do GitHub.

- dependendo da aplicação, utilizar técnicas de programação antiga (linhas de programação tratando exceções)
pode tornar o código extremamente complexo ou até impossível.

- machine learning é uma técnica na qual contruímos um modelo ou engine e fornecemos milhares e milhares de dados.
- com estes dados, o modelo irá procurar padrões que o ajudarão a resolver os problemas. Quanto maior a qtd de dados,
mais preciso será o nosso modelo.

# Passos para o Desenvolvimento de uma Machine Learning

1. importar os dados exportados por um banco de dados no formato csv (comma-separated values).
2. limpar os dados (Data Cleaning) - remover dados duplicados, incorretos, incompletos, irrelevantes.
   se os dados forem em formato de texto, devem ser convertidos para valores numéricos.
3. dividir os dados em dois grupos, um para treinar o modelo (Training) e outro para testar o modelo (Test Sets).
4. criar o modelo, selecionando o algoritmo (decision trees, neural networks, etc) para analisar os dados.
   o algoritmos ideal vai depender do tipo de problema e dados de entrada (veremos o Scikit-Learn).
5. treinar o modelo - alimentá-lo com nossos dados de treinamento.
6. testar o modelo - pedi-lo para fazer previsões.
7. avaliar as previsões do modelo (precisão) e aprimorar (testar novos algoritmos ou cailbrar parâmetros).

# Bibliotecas

- Numpy - matriz multidimensional.
- Pandas - biblioteca de análise de dados em data frame (estrutura de dados em 2D).
- MatPlotLib - biblioteca de plotagem 2D para criar gráficos e plotagem.
- Scikit-Learn - decision tree, neural nwtwork, etc.

# Jupyter.org

- Utilizamos um ambiente chamado Jupyter para codar. Seria possível codar uma Machine Learning no PyCharm,
mas este ambiente não seria o ideal, pela dificuldade para inspecionar dados (faremos bastante).
- Ao abrir o Jupyter Notebook, uma aba no navegador é aberta em localhost:8888/tree (Jupyter Dashboard).
- Em uma pasta: clicar New + Python 3 (ipykernel), que vai te jogar para uma aba do projeto (notebook) criado.

# Importar Dados de um Arquivo csv

1. entrar no site kaggle.com (local para trabalhar com projetos de ciências de dados).
2. logar e pesquisar pelos data sets disponíveis (baixamos o vgsales.csv - Video Game Sales Study).
3. salvar o arquivo csv baixado na mesma pasta do projeto para simplificar o path (xis/documents).
4. de volta no notebook codar:
   import pandas as pd              -> para facilitar as chamadas de métodos.
   df = pd.read_csv('vgsales.csv')  -> retorna um data frame object (tipo uma planilha excel).
   df                               -> inspeciona df (output = tabela de dados).
   df.shape                         -> retorna o formato do conjunto de dados, nesse caso 2D (linhas e colunas)
   df.describe                      -> retorna tabela com infos dos dados (qtd, média, desvio padrão, min, 25%, 50%, 75%, máx).
   df.values                        -> retorna os dados em um array 2D (matriz). Cada Array Interior é um elemento do Array Exterior.

# Atalhos de Teclado do Jupyter

- Célula Verde - Edit Mode (pressionar enter).
- Célula Azul - Command Mode (pressionar esc).
- H em Command Mode abre um pop-up com a lista de todos os atalhos em ambos os modos.
- A em Command Mode insere uma nova célula acima da célula atual.
- B em Command Mode insere uma nova célula abaixo da célula atual.
- D+D em Command Mode deleta a célula atual.
- Tab após . em Edit Mode apresenta todos os atributos e objetos do objeto.
- Shift + Tab (cursor no nome do método) em Edit Mode apresenta um tooltip que descreve o que o método faz e quais parâmetros ele possui.
- Ctrl + / em Edit Mode transforma a linha atual em comentário.

- O arquivo (notebook) da aplicação criada possui extensão .ipynb e inclui o código fonte organizado em células
e a saída (output) de cada célula. Um arquivo .py inclui apenas o código fonte.
