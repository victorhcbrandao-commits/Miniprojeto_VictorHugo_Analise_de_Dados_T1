# Miniprojeto_VictorHugo_Analise_de_Dados_T1

## Mini Projeto Avaliativo - SCTEC

**Curso:** Análise de Dados com Python [T1]  
**Módulo:** Módulo 1 - Semana 07  
**Aluno:** Victor Hugo  
**Turma:** Analise_de_Dados_T1  

---

## Objetivo do Projeto

O objetivo deste mini projeto é realizar uma Análise Exploratória de Dados (AED) aplicada à base `Varejo.csv`, utilizando Python e a biblioteca pandas.

A atividade contempla as principais etapas de preparação e análise de uma base real de varejo, incluindo importação, verificação de problemas, limpeza dos dados, transformação de tipos, estatísticas descritivas, agrupamentos e geração de conclusões.

---

## Base de Dados

A base utilizada foi a `Varejo.csv`, sugerida no Kaggle pelo curso da SCTEC.

Ela contém registros de compras no varejo, com informações como:

- Data da compra
- Cliente
- Gênero do cliente
- Número de filhos
- Produto
- Categoria do produto
- Identificador da compra

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Regex / expressões regulares
- Biblioteca csv / csv.DictReader
- VSCode ou Google Colab
- Git e GitHub

---

## Estrutura dos Arquivos

```text
Miniprojeto_VictorHugo_Analise_de_Dados_T1/
│
├── mini_projeto.py
├── Varejo.csv
├── df_limpo.csv
├── README.md
└── README_VictorHugo_Analise_de_Dados_T1.md
```

---

## Sprints Desenvolvidas

### Sprint 1 - Importação dos Dados

Foi realizada a importação da base `Varejo.csv` com pandas, utilizando o método `read_csv`. Também foi incluída uma demonstração complementar com `csv.DictReader`, conforme previsto na rúbrica de avaliação.

Também foram exibidos:

- Número de registros
- Número de colunas
- Nome das colunas
- Tipos de dados originais

---

### Sprint 2 - Transformação de Strings, Integer, Float e Datetime

Foram criadas funções para tratamento de dados:

- Limpeza de textos com `strip()` e expressões regulares
- Conversão de valores inteiros com `pd.to_numeric`
- Conversão de valores decimais com tratamento de vírgulas e caracteres inválidos
- Conversão da coluna `DATA` para o tipo `datetime`

---

### Sprint 3 - Limpeza de Nulos e Duplicatas

Foram aplicadas rotinas de limpeza para:

- Identificar valores nulos por coluna
- Identificar duplicatas
- Validar o identificador de compra `CO_ID`
- Remover registros sem identificador de compra
- Substituir categorias vazias por `"Sem Categoria"`
- Imputar valores ausentes da coluna `CL_FHL` pela mediana
- Remover registros com datas inválidas
- Remover registros duplicados

A escolha de imputar `CL_FHL` pela mediana foi feita porque a mediana é menos sensível a valores extremos do que a média.

---

### Sprint 4 - Estatística Descritiva

Foram calculadas estatísticas da coluna `CL_FHL`, referente ao número de filhos do cliente:

- Média
- Mediana
- Desvio padrão
- Moda
- Máximo
- Mínimo
- Contagem
- Quartis

---

### Sprint 5 - Relatório e Documentação

O script gera um relatório no terminal contendo:

- Estrutura da base
- Problemas encontrados
- Dados tratados
- Estatísticas descritivas
- Agrupamentos
- Conclusões finais

Este README apresenta a documentação do projeto e a reflexão teórica sobre a importância da qualidade dos dados.

---

### Sprint 6 - Versionamento

Os arquivos do projeto devem ser enviados para um repositório público no GitHub com o nome:

```text
Miniprojeto_VictorHugo_Analise_de_Dados_T1
```

Arquivos esperados no repositório:

- `mini_projeto.py`
- `Varejo.csv`
- `df_limpo.csv`
- `README.md`
- `README_VictorHugo_Analise_de_Dados_T1.md`

---

## Agrupamentos Realizados

### 1. Compras por Gênero

Foi utilizado `groupby()` para identificar a quantidade de compras por gênero do cliente.

### 2. Categorias Mais Vendidas

Foi utilizado `groupby()` para identificar as categorias com maior quantidade de registros de venda.

### 3. Média de Filhos por Gênero

Foi incluído um agrupamento adicional para observar a média de filhos dos clientes por gênero.

---

## Principais Insights

1. A base possui grande volume de registros e permite análises relevantes para o varejo.
2. Foram encontrados problemas de qualidade, como possíveis categorias vazias, datas inválidas e duplicatas.
3. A limpeza dos dados foi necessária para aumentar a confiabilidade da análise.
4. A conversão da coluna `DATA` para `datetime` permite futuras análises temporais.
5. A validação do identificador de compra `CO_ID` reforça a confiabilidade das contagens e agrupamentos.
6. A coluna `CL_FHL` foi tratada e analisada com estatísticas descritivas.
7. Os agrupamentos por gênero e categoria ajudam a identificar padrões de comportamento de compra.

---

## Reflexão Teórica

A Análise Exploratória de Dados é uma etapa fundamental em projetos de dados, pois permite compreender a estrutura da base, identificar problemas de qualidade e encontrar padrões iniciais antes de análises mais avançadas.

Bases reais geralmente possuem inconsistências, como valores nulos, duplicatas, tipos incorretos e campos textuais mal preenchidos. Por isso, a etapa de limpeza é essencial para que os resultados obtidos sejam confiáveis.

Neste projeto, o uso do pandas facilitou a importação, transformação e sumarização dos dados. A aplicação de funções, condicionais e expressões regulares contribuiu para padronizar as informações e preparar a base para análises futuras.

---

## Como Executar

### Opção 1 - VSCode

1. Abra a pasta do projeto no VSCode.
2. Confirme que o arquivo `Varejo.csv` está na mesma pasta do script.
3. Execute no terminal:

```bash
python mini_projeto.py
```

### Opção 2 - Google Colab

1. Abra o Google Colab.
2. Faça upload do arquivo `Varejo.csv`.
3. Copie o conteúdo do script `mini_projeto.py`.
4. Execute todas as células.

---

## Comandos Sugeridos para GitHub

```bash
git init
git add Varejo.csv
git commit -m "Importa base de dados do projeto"

git add mini_projeto.py
git commit -m "Adiciona script inicial de analise exploratoria"

git add mini_projeto.py df_limpo.csv
git commit -m "Implementa limpeza estatisticas e agrupamentos"

git add README.md README_VictorHugo_Analise_de_Dados_T1.md
git commit -m "Finaliza documentacao do mini projeto"

git branch -M main
git remote add origin https://github.com/victorhcbrandao-commits/Miniprojeto_VictorHugo_Analise_de_Dados_T1.git
git push -u origin main
```

---

## Arquivo de Saída

Após a execução do script, é gerado o arquivo:

```text
df_limpo.csv
```

Esse arquivo contém a base tratada e pronta para análises posteriores.
