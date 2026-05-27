# ============================================================
# MINI PROJETO AVALIATIVO - SCTEC
# Análise de Dados com Python [T1]
# Mini-Projeto Avaliativo - Módulo 1 - Semana 07
#
# Aluno: Victor Hugo
# Turma: Analise_de_Dados_T1
#
# Objetivo:
# Realizar uma Análise Exploratória de Dados aplicada à base Varejo.csv,
# contemplando importação, diagnóstico, limpeza, estatística descritiva,
# agrupamentos e conclusões.
# ============================================================

import pandas as pd
import numpy as np
import re
import csv


# ------------------------------------------------------------
# FUNÇÃO 1 - Limpeza de textos
# ------------------------------------------------------------
def limpar_texto(valor):
    """
    Recebe um valor textual, remove espaços extras e caracteres especiais
    indesejados usando expressão regular.

    Caso o valor esteja vazio ou nulo, retorna 'Sem Categoria'.
    """
    if pd.isna(valor):
        return "Sem Categoria"

    valor = str(valor).strip()

    if valor == "":
        return "Sem Categoria"

    # Mantém letras, números, acentos, espaços e alguns sinais simples.
    valor = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s\-/]", "", valor)

    # Remove espaços duplicados.
    valor = re.sub(r"\s+", " ", valor)

    return valor


# ------------------------------------------------------------
# FUNÇÃO 2 - Conversão para número inteiro
# ------------------------------------------------------------
def converter_inteiro(serie):
    """
    Converte uma série para valores numéricos inteiros.
    Valores inválidos são transformados em NaN para posterior tratamento.
    """
    return pd.to_numeric(serie, errors="coerce")


# ------------------------------------------------------------
# FUNÇÃO 3 - Conversão para número decimal
# ------------------------------------------------------------
def converter_decimal(serie):
    """
    Converte uma série para valores numéricos decimais.
    Também trata possíveis vírgulas usadas como separador decimal.
    """
    serie = serie.astype(str).str.replace(",", ".", regex=False)
    serie = serie.str.replace(r"[^0-9.\-]", "", regex=True)
    return pd.to_numeric(serie, errors="coerce")


# ------------------------------------------------------------
# 1. IMPORTAÇÃO DOS DADOS
# ------------------------------------------------------------

# A base Varejo.csv foi disponibilizada no Kaggle e importada para execução
# local no VSCode ou no Google Colab.
df = pd.read_csv("Varejo.csv", sep=";")

# Demonstração complementar de leitura estruturada usando csv.DictReader,
# conforme critério da rúbrica de avaliação.
# A análise principal será realizada com pandas, mas este bloco valida
# a leitura nativa do CSV em formato de dicionário.
with open("Varejo.csv", mode="r", encoding="utf-8") as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv, delimiter=";")
    amostra_dictreader = []

    for indice, linha in enumerate(leitor_csv):
        amostra_dictreader.append(linha)
        if indice == 2:
            break

print("=" * 70)
print("1. IMPORTAÇÃO DOS DADOS")
print("=" * 70)

print("Leitura estruturada com csv.DictReader realizada com sucesso.")
print(f"Quantidade de registros lidos na amostra DictReader: {len(amostra_dictreader)}")

print(f"Número de registros: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")

print("\nColunas da base:")
print(df.columns.tolist())

print("\nTipos de dados originais:")
print(df.dtypes)


# ------------------------------------------------------------
# 2. VERIFICAÇÃO DE PROBLEMAS BÁSICOS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("2. VERIFICAÇÃO DE PROBLEMAS BÁSICOS")
print("=" * 70)

print("\nValores nulos por coluna:")
print(df.isnull().sum())

duplicatas_antes = df.duplicated().sum()
print(f"\nRegistros duplicados encontrados: {duplicatas_antes}")

# Verificação inicial de datas inválidas
datas_teste = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
datas_invalidas = datas_teste.isnull().sum()
print(f"\nDatas inválidas encontradas na coluna DATA: {datas_invalidas}")

# Verificação de categorias vazias
categorias_vazias = (
    df["PR_CAT"].isnull().sum()
    + (df["PR_CAT"].astype(str).str.strip() == "").sum()
)
print(f"Categorias vazias ou nulas encontradas em PR_CAT: {categorias_vazias}")

# Validação da regra de negócio do identificador da compra.
# O campo CO_ID é essencial para rastrear as compras, portanto não deve estar vazio.
compras_sem_identificador = df["CO_ID"].isnull().sum()
compras_identificador_vazio = (df["CO_ID"].astype(str).str.strip() == "").sum()
total_compras_invalidas = compras_sem_identificador + compras_identificador_vazio

print(f"Compras com identificador CO_ID nulo ou vazio: {total_compras_invalidas}")


# ------------------------------------------------------------
# 3. LIMPEZA E TRANSFORMAÇÃO DOS DADOS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("3. LIMPEZA E TRANSFORMAÇÃO DOS DADOS")
print("=" * 70)

# 3.1 Remoção de colunas vazias ou desnecessárias criadas no CSV
colunas_vazias = [col for col in df.columns if "Unnamed" in col]
df = df.drop(columns=colunas_vazias, errors="ignore")

print("\nColunas vazias removidas:")
print(colunas_vazias)

# 3.2 Validação e tratamento da regra de negócio do identificador da compra
# Como CO_ID identifica a compra, registros sem esse identificador não são confiáveis
# para contagens e agrupamentos. Por isso, eles são removidos da base limpa.
linhas_antes_co_id = df.shape[0]
df["CO_ID"] = df["CO_ID"].astype(str).str.strip()
df = df[df["CO_ID"] != ""]
registros_sem_co_id_removidos = linhas_antes_co_id - df.shape[0]

print(f"Registros removidos por CO_ID vazio: {registros_sem_co_id_removidos}")

# 3.3 Limpeza de strings usando função e expressão regular
# A escolha foi preencher categorias nulas ou vazias com "Sem Categoria"
# para não eliminar compras válidas apenas por ausência de classificação.
df["PR_CAT"] = df["PR_CAT"].apply(limpar_texto)

# Quando existir coluna de produto, também aplica limpeza textual.
if "PR_NOME" in df.columns:
    df["PR_NOME"] = df["PR_NOME"].apply(limpar_texto)

# 3.3 Conversão da coluna DATA para datetime
df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")

# Como DATA é essencial para análises temporais, registros com data inválida
# são removidos da base limpa.
qtd_datas_invalidas = df["DATA"].isnull().sum()
df = df.dropna(subset=["DATA"])

print(f"\nRegistros removidos por data inválida: {qtd_datas_invalidas}")

# 3.4 Conversão da coluna número de filhos para numérico
df["CL_FHL"] = converter_inteiro(df["CL_FHL"])

# Para CL_FHL, foi escolhida a imputação pela mediana porque é uma medida
# menos sensível a valores extremos do que a média.
nulos_filhos_antes = df["CL_FHL"].isnull().sum()
mediana_filhos = df["CL_FHL"].median()
df["CL_FHL"] = df["CL_FHL"].fillna(mediana_filhos).astype(int)

print(f"Nulos tratados em CL_FHL pela mediana: {nulos_filhos_antes}")

# 3.5 Conversão de possíveis colunas numéricas de valores/preços
# O tratamento é feito somente se essas colunas existirem na base.
possiveis_colunas_decimais = [
    "VALOR",
    "VALOR_TOTAL",
    "PRECO",
    "PR_PRECO",
    "CO_VALOR",
    "VL_TOTAL",
    "TOTAL"
]

for coluna in possiveis_colunas_decimais:
    if coluna in df.columns:
        df[coluna] = converter_decimal(df[coluna])

# 3.6 Remoção de duplicatas
linhas_antes = df.shape[0]
df = df.drop_duplicates()
duplicatas_removidas = linhas_antes - df.shape[0]

print(f"Duplicatas removidas: {duplicatas_removidas}")
print(f"Total de registros após limpeza: {df.shape[0]}")

print("\nTipos de dados após tratamento:")
print(df.dtypes)


# ------------------------------------------------------------
# 4. ESTATÍSTICA DESCRITIVA - NÚMERO DE FILHOS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("4. ESTATÍSTICA DESCRITIVA - NÚMERO DE FILHOS DO CLIENTE")
print("=" * 70)

media = df["CL_FHL"].mean()
mediana = df["CL_FHL"].median()
desvio_padrao = df["CL_FHL"].std()
moda = df["CL_FHL"].mode()[0]
maximo = df["CL_FHL"].max()
minimo = df["CL_FHL"].min()
contagem = df["CL_FHL"].count()
quartis = df["CL_FHL"].quantile([0.25, 0.50, 0.75])

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Moda: {moda}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Contagem: {contagem}")

print("\nQuartis:")
print(quartis)


# ------------------------------------------------------------
# 5. PADRÕES DE AGRUPAMENTO
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("5. PADRÕES DE AGRUPAMENTO")
print("=" * 70)

# Agrupamento 1: compras por gênero do cliente
compras_por_genero = (
    df.groupby("CL_GENERO")["CO_ID"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nAgrupamento 1 - Quantidade de compras por gênero:")
print(compras_por_genero)

# Agrupamento 2: categorias mais vendidas
categorias_mais_vendidas = (
    df.groupby("PR_CAT")["CO_ID"]
    .count()
    .sort_values(ascending=False)
)

print("\nAgrupamento 2 - Categorias mais vendidas:")
print(categorias_mais_vendidas)

# Agrupamento adicional: média de filhos por gênero
media_filhos_genero = (
    df.groupby("CL_GENERO")["CL_FHL"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAgrupamento adicional - Média de filhos por gênero:")
print(media_filhos_genero)


# ------------------------------------------------------------
# 6. EXPORTAÇÃO DA BASE LIMPA
# ------------------------------------------------------------

df.to_csv("df_limpo.csv", index=False)

print("\n" + "=" * 70)
print("6. EXPORTAÇÃO")
print("=" * 70)

print("Arquivo df_limpo.csv exportado com sucesso.")


# ------------------------------------------------------------
# 7. CONCLUSÕES
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("7. CONCLUSÕES")
print("=" * 70)

print("""
1. A base de varejo possui grande volume de registros e permite observar padrões relevantes de compras.

2. Foram identificados problemas básicos de qualidade, como colunas vazias, possíveis categorias sem preenchimento,
   datas inválidas e registros duplicados.

3. As categorias vazias foram preenchidas com "Sem Categoria" para preservar os registros de compra e evitar perda
   de informação operacional.

4. A coluna DATA foi convertida para o tipo datetime, permitindo análises temporais mais confiáveis.

5. A coluna CL_FHL foi convertida para formato numérico e os valores ausentes foram imputados pela mediana,
   reduzindo o impacto de valores extremos.

6. Os agrupamentos por gênero e categoria ajudaram a identificar padrões de comportamento de compra e categorias
   com maior volume de vendas.
""")
