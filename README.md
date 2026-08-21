# 🛒 Análise de Dados de Varejo

**Python · Pandas · Limpeza de Dados · Análise Exploratória de Dados**

[🇺🇸 English](README.md) | 🇧🇷 **Português**

> Transformando uma grande base de dados de varejo em dados limpos, estruturados e prontos para análise utilizando Python e Pandas.

> Este projeto foi originalmente desenvolvido como parte de um **programa de formação em Análise de Dados com Python** e posteriormente reorganizado para apresentação em portfólio profissional.

---

## 📌 Visão Geral do Projeto

O projeto **Análise de Dados de Varejo** explora uma grande base de dados contendo informações sobre clientes, compras e produtos.

A base original possui aproximadamente **830.000 registros** e apresenta desafios comuns de qualidade de dados encontrados em cenários reais, incluindo:

- colunas vazias;
- registros duplicados;
- tipos de dados inconsistentes;
- variáveis categóricas que precisam ser validadas;
- campos de data que precisam ser convertidos.

O projeto implementa um fluxo completo de preparação e análise exploratória utilizando **Python e Pandas**, transformando os dados brutos em uma base limpa e estruturada, pronta para análises posteriores.

O fluxo geral do projeto é:

```text
Base de Varejo Bruta
        │
        ▼
Inspeção dos Dados
        │
        ▼
Avaliação da Qualidade
        │
        ▼
Limpeza e Transformação
        │
        ▼
Análise Exploratória
        │
        ▼
Base Processada
        │
        ▼
Insights de Negócio
```

---

## 🗂️ Base de Dados

O projeto utiliza uma base de varejo contendo informações sobre clientes, compras e produtos.

A base original contém:

```text
830.000 linhas
14 colunas
```

Os principais atributos incluem:

| Coluna | Descrição |
|---|---|
| `DATA` | Data da compra |
| `CO_ID` | Identificador da compra |
| `CL_ID` | Identificador do cliente |
| `CL_GENERO` | Gênero do cliente |
| `CL_EC` | Estado civil do cliente |
| `CL_FHL` | Número de filhos |
| `CL_SEG` | Segmento do cliente |
| `PR_ID` | Identificador do produto |
| `PR_CAT` | Categoria do produto |
| `PR_NOME` | Nome do produto |

A base bruta também continha quatro colunas completamente vazias:

```text
Unnamed: 10
Unnamed: 11
Unnamed: 12
Unnamed: 13
```

Essas colunas foram identificadas durante a avaliação de qualidade e removidas durante o processamento.

---

## 🔎 Avaliação da Qualidade dos Dados

Antes da análise, a base foi inspecionada em busca de problemas comuns de qualidade de dados.

A avaliação incluiu:

- valores ausentes;
- registros duplicados;
- datas inválidas;
- categorias de produtos vazias;
- identificadores de compra ausentes;
- colunas vazias desnecessárias;
- consistência dos tipos de dados.

A análise identificou **96.553 registros duplicados** na base original.

Após a limpeza e remoção das duplicidades, a base final passou a conter:

```text
733.447 registros
```

Isso representa aproximadamente **88% da base original**, preservando a maior parte das informações enquanto elimina observações duplicadas.

---

## 🧹 Limpeza e Transformação dos Dados

A etapa de processamento prepara os dados brutos para uma análise mais confiável.

As principais transformações incluem:

```text
Dados brutos
   │
   ├── Remoção de colunas vazias
   │
   ├── Validação dos identificadores de compra
   │
   ├── Conversão das datas
   │
   ├── Normalização dos tipos de dados
   │
   ├── Tratamento de valores ausentes
   │
   ├── Validação das categorias de produtos
   │
   └── Remoção de registros duplicados
   │
   ▼
Base limpa
```

### Conversão de datas

A coluna `DATA` é convertida para um formato datetime adequado, permitindo análises temporais mais confiáveis.

### Identificadores de compra

O campo `CO_ID` é tratado como identificador, e não como uma medida numérica.

### Valores ausentes

O projeto verifica o campo `CL_FHL` e aplica imputação pela mediana quando existem valores ausentes.

### Remoção de duplicidades

Observações duplicadas são removidas antes da realização das análises exploratórias.

### Colunas vazias

Colunas contendo apenas valores nulos são removidas automaticamente.

---

## 📊 Análise Exploratória de Dados

Após a limpeza da base, são realizadas estatísticas descritivas e análises agrupadas para identificar padrões relacionados aos clientes e às compras.

### Número de filhos

A variável `CL_FHL` apresenta as seguintes estatísticas descritivas:

| Métrica | Valor |
|---|---:|
| Média | 1,15 |
| Mediana | 0 |
| Desvio padrão | 1,42 |
| Moda | 0 |
| Mínimo | 0 |
| Máximo | 4 |

Quartis:

```text
25% → 0 filhos
50% → 0 filhos
75% → 2 filhos
```

Os resultados indicam que uma parcela significativa dos clientes presentes na base não possui filhos.

---

## 🛍️ Análise das Categorias de Produtos

A base processada permite identificar as categorias com maior volume de registros de compra.

| Categoria | Registros |
|---|---:|
| ALIMENTOS | 384.197 |
| HIGIENE | 137.702 |
| LIMPEZA | 128.632 |
| BEBIDAS | 38.264 |
| PET | 28.553 |
| ACESSORIOS | 12.871 |
| N/D | 3.228 |

A categoria **ALIMENTOS** representa, com ampla diferença, o maior volume de registros da base.

---

## 👥 Análise dos Clientes

O projeto também avalia a atividade de compra de acordo com o gênero dos clientes.

Identificadores únicos de compra por gênero:

| Gênero | Compras |
|---|---:|
| Feminino | 9.615 |
| Masculino | 8.856 |

Média do número de filhos:

| Gênero | Média |
|---|---:|
| Masculino | 1,21 |
| Feminino | 1,09 |

Essas agregações fornecem uma visão inicial das características dos clientes e dos padrões de compra presentes na base.

---

## 💡 Principais Resultados

A análise destaca algumas características relevantes da base de varejo:

- A base original possui **830.000 registros**, demonstrando o processamento de um volume significativo de dados utilizando Pandas.
- Foram identificados e removidos **96.553 registros duplicados**.
- A base final processada contém **733.447 registros**.
- `ALIMENTOS` é a categoria dominante em quantidade de registros.
- A mediana do número de filhos dos clientes é **0**.
- Clientes do gênero feminino apresentam uma quantidade ligeiramente maior de identificadores únicos de compra do que clientes do gênero masculino.
- A conversão adequada de datas e identificadores melhora a confiabilidade das análises posteriores.

O projeto demonstra como um processo estruturado de limpeza pode transformar dados operacionais brutos em uma base mais confiável para exploração analítica.

---

## 🛠️ Tecnologias Utilizadas

### Processamento de Dados

`Python` · `Pandas`

### Manipulação de Dados

`CSV` · `csv.DictReader`

### Análise

`Estatística Descritiva` · `Agregação de Dados` · `Limpeza de Dados`

### Desenvolvimento

`Git` · `GitHub` · `VS Code`

---

## 📁 Estrutura do Projeto

```text
retail-data-analysis/
│
├── data/
│   │
│   ├── raw/
│   │   └── Varejo.csv
│   │
│   └── processed/
│       └── df_limpo.csv
│
├── src/
│   └── retail_analysis.py
│
├── .gitignore
├── README.md
├── README.pt-BR.md
└── requirements.txt
```

---

## 🚀 Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/victorhcbrandao/retail-data-analysis.git
```

### 2. Acessar a pasta do projeto

```bash
cd retail-data-analysis
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a Análise

Certifique-se de que a base original esteja disponível em:

```text
data/raw/Varejo.csv
```

Depois execute:

```bash
python src/retail_analysis.py
```

O script executa todo o fluxo:

```text
Importação
   ↓
Avaliação da Qualidade
   ↓
Limpeza
   ↓
Transformação
   ↓
Estatística Descritiva
   ↓
Análises Agrupadas
   ↓
Exportação
```

---

## 📤 Base Processada

Após o processamento, a base limpa é exportada para:

```text
data/processed/df_limpo.csv
```

A base processada contém **733.447 registros** após a remoção das observações duplicadas e das colunas desnecessárias.

---

## 🔬 Fluxo da Análise

O projeto demonstra um fluxo reproduzível de análise de dados:

```text
                ┌───────────────────┐
                │   Varejo.csv      │
                │ 830 mil registros │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Inspeção dos      │
                │ Dados             │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Verificações de   │
                │ Qualidade         │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Limpeza e         │
                │ Transformação     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ 733 mil Registros │
                │ Limpos            │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Análise           │
                │ Exploratória      │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Insights de       │
                │ Negócio           │
                └───────────────────┘
```

---

## 📈 Possíveis Melhorias

Possíveis evoluções futuras do projeto incluem:

- visualizações exploratórias adicionais;
- análise de segmentação de clientes;
- análise temporal das compras;
- análise de afinidade entre produtos;
- testes automatizados de qualidade dos dados;
- implementação de logs e monitoramento;
- maior modularização do pipeline de análise;
- dashboard interativo utilizando Streamlit ou Power BI.

---

## 🎯 Sobre o Projeto

Este projeto demonstra experiência prática com **limpeza, transformação, validação, estatística descritiva e análise exploratória de dados utilizando Python**.

Foi originalmente desenvolvido durante minha **formação em Análise de Dados com Python** e posteriormente reorganizado para apresentação em portfólio profissional.

O projeto complementa projetos analíticos mais avançados ao demonstrar fundamentos sólidos em:

**Python · Pandas · Limpeza de Dados · Qualidade de Dados · Análise Exploratória de Dados**

---

## 👨‍💻 Autor

**Victor Hugo de Castro Brandão**

Finanças | Análise de Dados | Tecnologia Financeira

[GitHub](https://github.com/victorhcbrandao) · [LinkedIn](https://www.linkedin.com/in/victorhugodecastro/)