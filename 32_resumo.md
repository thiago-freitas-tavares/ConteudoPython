# Resumo

01. Funções Gerais: print, input.
    Tipos primitivos de dados: integer, float, complex, string, boolean.
02. Conversão de Dados: int(), float(), complex(), str(), bool().
03. Tipo Complexo de Dado: list[item1, item2, item3].
04. Variável com string se torna um objeto e ganha funções (métodos).
    Strings em Python são imutáveis.
05. Operadores Aritméticos: +, -, *, /, //, %, **.
    Funções Aritméticas: import math.
06. Operador de Condição: if, elif, else.
07. Operadores de Lógica: and, or, not.
08. Operadores de Comparação: >, >=, <, <=, ==, !=.
09. Operador de Loop/Iteração: while.
    while True -> até encontrar um break.
10. Operador de Loop/Iteração: for.
11. Função range(): não conta o 2° argumento e 3° argumento é o passo.
12. Operador de Loop Aninhado: for dentro de for.
13. Lista 2D: list dentro de list (matriz).
14. Métodos (funções) do objeto list.
15. Tipo Complexo de Dado: tuple(item1, item2, item3).
16. Unpacking: atribuição simplificada de valores a listas ou tuples.
17. Tipo Complexo de Dado: dictionary = {"key1": "value1", "key2": "value2"}
    dictionary.get(n1, n2): busca n1 no dicionário, se não encontrar, retorna n2.
18. Funções(parâmetros). Código em funções para poder reutilizá-las.
19. Positional Arguments e Keyword Arguments. função(n1, sobrenome=n2).
20. Funções(): return.
21. Tratando Erros: try, except.
22. Classe para definir novos tipos de dados.
    Funções das classes são métodos para os objetos do novo tipo de dado.
    função(self) aponta para o objeto sendo criado.
23. Constructor: método chamado qdo o objeto de uma classe é criado.
    __init__(self, parâmetro1, parâmetro2).
24. Inheritage (herança): mecanismo de reutilização de código.
    Class n1(n2) -> n1 herda todos métodos de n2.
25. Módulo: arquivo.py com código Python (pode ser importado em qqr módulo)
    Organização do código: funções -> classes -> módulos -> pacotes.
26. Package (Pacote): container para múltiplos módulos.
    Possui um __init__.py (indicando que é um pacote) + módulos.
27. Biblioteca de built-in módulos em python. Ex: random.
28. Built-in módulo pathlib fornece classes com métodos que podem ser utilizados para manipular pastas e arquivos através de Generator Objects.
29. Python Package Index (pypi) pypi.org: repositório de pacotes desenvolvidos por qualquer programador Python.
30. import openpyxl para manipular planilhas de excel e Barchart/Reference para criar gráficos.
31. Machine Learning: fornecemos dados para um modelo procurar padrões que o ajudarão a resolver problemas. Jupyter Notebook.
    Bibliotecas: numpy, pandas, matplotlib, scikit-learn.

# Convenção de Nomeação Pascal
- classe    -> ConvencaoDeNomeacaoPascal
- função    -> convencao_de_nomeacao_pascal
- variáveis -> convencao_de_nomeacao_pascal

# Google Python Style Guide

- module_name
- package_name
- ClassName
- method_name
- ExceptionName
- function_name
- GLOBAL_CONSTANT_NAME
- CLASS_CONSTANT_NAME
- global_var_name
- instance_var_name
- function_parameter_name
- local_var_name

# Atividades Avançadas
- Acessar informação do yeld.com através do programa desenvolvido.
- Web Scraping - engine (web crawler) que navega um site e extrai informação de arquivos HDML.
- Browser Automation - automatiza o teste de compatibilidade das aplicações web com todos os browsers (pyp selenium).