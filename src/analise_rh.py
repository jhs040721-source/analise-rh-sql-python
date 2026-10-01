# Projeto: Análise de RH com SQL e Python
# Etapa: Análise exploratória, estatísticas e visualizações

# Bibliotecas utilizadas no projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 1. CONFIGURAÇÃO DAS PASTAS
# Pasta onde os gráficos serão salvos.

PASTA_GRAFICOS = Path("outputs/graficos")
PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)

# 2. CARREGAMENTO DAS BASES DE DADOS

# Query 1:
# funcionários, departamentos, cargos e faixas salariais.
df1 = pd.read_csv("data/raw/query_01.csv")

# Query 2:
# funcionários, departamentos e informações geográficas.
df2 = pd.read_csv("data/raw/query_02.csv")

print("\n================ AMOSTRA DOS DADOS ================")

print("\nPrimeiros registros da Query 1:")
print(df1.head())

print("\nPrimeiros registros da Query 2:")
print(df2.head())

# 3. CONFERÊNCIA INICIAL DAS BASES

print("\n================ ESTRUTURA DAS BASES ================")

print("\nDimensões da Query 1:", df1.shape)
print("Dimensões da Query 2:", df2.shape)

print("\nCOLUNAS E TIPOS — QUERY 1")
print(df1.dtypes)

print("\nCOLUNAS E TIPOS — QUERY 2")
print(df2.dtypes)

# 4. QUALIDADE DOS DADOS

# 4.1 Valores ausentes
print("\n================ VALORES AUSENTES ================")

print("\nQUERY 1")
print(df1.isna().sum())

print("\nQUERY 2")
print(df2.isna().sum())


# 4.2 Registros duplicados
print("\n================ DUPLICIDADES ================")

print("\nQUERY 1")
print("Linhas duplicadas:", df1.duplicated().sum())
print("Funcionários repetidos:", df1["EMPLOYEE_ID"].duplicated().sum())

print("\nQUERY 2")
print("Linhas duplicadas:", df2.duplicated().sum())
print("Funcionários repetidos:", df2["EMPLOYEE_ID"].duplicated().sum())


# 4.3 Consistência dos salários
print("\n================ CONSISTÊNCIA DOS SALÁRIOS ================")

print(
    "Query 1 - salários menores ou iguais a zero:",
    (df1["SALARIO"] <= 0).sum()
)

print(
    "Query 2 - salários menores ou iguais a zero:",
    (df2["SALARIO"] <= 0).sum()
)


# 4.4 Funcionários com localização incompleta
colunas_localizacao = [
    "DEPARTAMENTO",
    "CIDADE",
    "ESTADO",
    "PAIS",
    "REGIAO"
]

incompletos = df2[
    df2[colunas_localizacao].isna().any(axis=1)
]

print("\nFUNCIONÁRIOS COM LOCALIZAÇÃO INCOMPLETA")
print(incompletos.to_string(index=False))

# 5. ESTATÍSTICAS SALARIAIS GERAIS

# 5.1 Query 2 — visão geral dos 107 funcionários
print("\n================ ESTATÍSTICAS — QUERY 2 ================")

print("Quantidade de funcionários:", df2["SALARIO"].count())
print("Salário médio:", df2["SALARIO"].mean())
print("Salário mediano:", df2["SALARIO"].median())
print("Menor salário:", df2["SALARIO"].min())
print("Maior salário:", df2["SALARIO"].max())

print("\nQUARTIS SALARIAIS — QUERY 2")
print("Primeiro quartil (25%):", df2["SALARIO"].quantile(0.25))
print("Segundo quartil (50%):", df2["SALARIO"].quantile(0.50))
print("Terceiro quartil (75%):", df2["SALARIO"].quantile(0.75))


# 5.2 Query 1 — visão salarial com informação de cargos
print("\n================ ESTATÍSTICAS — QUERY 1 ================")

print("Quantidade de funcionários:", df1["SALARIO"].count())
print("Salário médio:", df1["SALARIO"].mean())
print("Salário mediano:", df1["SALARIO"].median())
print("Menor salário:", df1["SALARIO"].min())
print("Maior salário:", df1["SALARIO"].max())

# 6. CONFERÊNCIA DAS COLUNAS DISPONÍVEIS

print("\n================ COLUNAS DISPONÍVEIS ================")

print("\nQUERY 1")
print(df1.columns.tolist())

print("\nQUERY 2")
print(df2.columns.tolist())

# 7. SALÁRIOS EM RELAÇÃO À FAIXA CADASTRADA DO CARGO

print("\n================ FAIXAS SALARIAIS DOS CARGOS ================")

print(
    df1[
        [
            "CARGO",
            "SALARIO",
            "SALARIO_MINIMO_CARGO",
            "SALARIO_MAXIMO_CARGO"
        ]
    ]
    .head(10)
    .to_string(index=False)
)

print(
    "\nSalários abaixo do mínimo do cargo:",
    (df1["SALARIO"] < df1["SALARIO_MINIMO_CARGO"]).sum()
)

print(
    "Salários acima do máximo do cargo:",
    (df1["SALARIO"] > df1["SALARIO_MAXIMO_CARGO"]).sum()
)

# 8. ANÁLISE POR REGIÃO E DEPARTAMENTO — QUERY 2

# 8.1 Quantidade de funcionários por região
print("\n================ FUNCIONÁRIOS POR REGIÃO ================")

funcionarios_por_regiao = (
    df2["REGIAO"]
    .fillna("Não informado")
    .value_counts()
)

print(funcionarios_por_regiao)
print("Total de funcionários:", funcionarios_por_regiao.sum())


# 8.2 Estatísticas salariais por região
print("\n================ SALÁRIOS POR REGIÃO ================")

salarios_por_regiao = (
    df2
    .assign(REGIAO=df2["REGIAO"].fillna("Não informado"))
    .groupby("REGIAO")["SALARIO"]
    .agg(
        funcionarios="count",
        media="mean",
        mediana="median"
    )
    .round(2)
)

print(salarios_por_regiao)


# 8.3 Estatísticas salariais por departamento
print("\n================ SALÁRIOS POR DEPARTAMENTO ================")

salarios_por_departamento = (
    df2
    .assign(
        DEPARTAMENTO=df2["DEPARTAMENTO"].fillna("Não informado")
    )
    .groupby("DEPARTAMENTO")["SALARIO"]
    .agg(
        funcionarios="count",
        media="mean",
        mediana="median"
    )
    .round(2)
    .sort_values("media", ascending=False)
)

print(salarios_por_departamento.to_string())


# 8.4 Exemplo de composição dos departamentos por região
# Essa conferência ajuda a interpretar diferenças salariais regionais.
print("\n================ SALES E SHIPPING POR REGIÃO ================")

sales_shipping = df2[
    df2["DEPARTAMENTO"].isin(["Sales", "Shipping"])
].copy()

print(
    pd.crosstab(
        sales_shipping["DEPARTAMENTO"],
        sales_shipping["REGIAO"].fillna("Não informado")
    ).to_string()
)

# 9. GRÁFICO S4.1 — DISTRIBUIÇÃO SALARIAL GERAL

media_salario = df2["SALARIO"].mean()
mediana_salario = df2["SALARIO"].median()

print("\n================ GRÁFICO S4.1 ================")
print("Média usada no gráfico:", media_salario)
print("Mediana usada no gráfico:", mediana_salario)

plt.figure(figsize=(10, 6))

plt.hist(
    df2["SALARIO"],
    bins=10,
    rwidth=0.9,
    edgecolor="black"
)

plt.axvline(
    x=media_salario,
    color="red",
    linestyle="--",
    linewidth=3,
    label=f"Média: {media_salario:.2f}"
)

plt.axvline(
    x=mediana_salario,
    color="green",
    linestyle=":",
    linewidth=3,
    label=f"Mediana: {mediana_salario:.2f}"
)

plt.title("Distribuição salarial dos 107 funcionários — Query 2")
plt.xlabel("Salário")
plt.ylabel("Quantidade de funcionários")
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig(
    PASTA_GRAFICOS / "s4_1_distribuicao_salarial.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# 10. ANÁLISE SALARIAL POR CARGO — QUERY 1

# 10.1 Quantidade de funcionários por cargo
print("\n================ FUNCIONÁRIOS POR CARGO ================")

funcionarios_por_cargo = df1["CARGO"].value_counts()

print(funcionarios_por_cargo)
print("Total de funcionários:", funcionarios_por_cargo.sum())


# 10.2 Mediana salarial por cargo
print("\n================ MEDIANA SALARIAL POR CARGO ================")

salarios_por_cargo = (
    df1
    .groupby("CARGO")["SALARIO"]
    .agg(
        funcionarios="count",
        mediana="median"
    )
    .sort_values("mediana", ascending=False)
)

print(salarios_por_cargo.to_string())

# 11. GRÁFICO S4.2 — MEDIANA SALARIAL POR CARGO

salarios_por_cargo_grafico = (
    df1
    .groupby("CARGO")["SALARIO"]
    .agg(
        funcionarios="count",
        mediana="median"
    )
    .sort_values("mediana")
)

rotulos_cargos_mediana = [
    f"{cargo} (n={int(funcionarios)})"
    for cargo, funcionarios in zip(
        salarios_por_cargo_grafico.index,
        salarios_por_cargo_grafico["funcionarios"]
    )
]

plt.figure(figsize=(11, 7))

plt.barh(
    rotulos_cargos_mediana,
    salarios_por_cargo_grafico["mediana"]
)

for indice, valor in enumerate(
    salarios_por_cargo_grafico["mediana"]
):
    plt.text(
        valor + 300,
        indice,
        f"{valor:.0f}",
        va="center"
    )

plt.title(
    "Mediana salarial por cargo — Query 1 "
    "(todos os salários válidos)"
)
plt.xlabel("Salário mediano")
plt.ylabel("Cargo")

plt.xlim(
    0,
    salarios_por_cargo_grafico["mediana"].max() * 1.12
)

plt.tight_layout()

plt.savefig(
    PASTA_GRAFICOS / "s4_2_salarios_por_cargo.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# 12. S4.3 — DISTRIBUIÇÃO SALARIAL POR PAÍS E REGIÃO

print("\n================ S4.3 — PAÍS E REGIÃO ================")

americas = df2[
    df2["REGIAO"] == "Americas"
].copy()

europe = df2[
    df2["REGIAO"] == "Europe"
].copy()

print("\nFuncionários por país — Americas:")
print(
    americas
    .groupby("PAIS")
    .size()
    .sort_values(ascending=False)
)

print("\nFuncionários por país — Europe:")
print(
    europe
    .groupby("PAIS")
    .size()
    .sort_values(ascending=False)
)


# Pequena dispersão horizontal nos pontos para facilitar
# a visualização de salários repetidos.
np.random.seed(42)


# 12.1 Gráfico — Americas
paises_americas = americas["PAIS"].dropna().unique()

plt.figure(figsize=(8, 5))

for posicao, pais in enumerate(paises_americas):

    dados_pais = americas[
        americas["PAIS"] == pais
    ]["SALARIO"]

    jitter = np.random.uniform(
        posicao - 0.12,
        posicao + 0.12,
        size=len(dados_pais)
    )

    plt.scatter(
        jitter,
        dados_pais,
        alpha=0.65,
        s=55
    )

    mediana = dados_pais.median()

    plt.hlines(
        mediana,
        posicao - 0.22,
        posicao + 0.22,
        linewidth=3
    )

plt.xticks(
    range(len(paises_americas)),
    paises_americas
)

plt.title("Distribuição salarial por país — Americas")
plt.xlabel("País")
plt.ylabel("Salário")
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()

plt.savefig(
    PASTA_GRAFICOS / "s4_3_salarios_pais_americas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 12.2 Gráfico — Europe
paises_europe = europe["PAIS"].dropna().unique()

plt.figure(figsize=(8, 5))

for posicao, pais in enumerate(paises_europe):

    dados_pais = europe[
        europe["PAIS"] == pais
    ]["SALARIO"]

    jitter = np.random.uniform(
        posicao - 0.12,
        posicao + 0.12,
        size=len(dados_pais)
    )

    plt.scatter(
        jitter,
        dados_pais,
        alpha=0.65,
        s=55
    )

    mediana = dados_pais.median()

    plt.hlines(
        mediana,
        posicao - 0.22,
        posicao + 0.22,
        linewidth=3
    )

plt.xticks(
    range(len(paises_europe)),
    paises_europe
)

plt.title("Distribuição salarial por país — Europe")
plt.xlabel("País")
plt.ylabel("Salário")
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()

plt.savefig(
    PASTA_GRAFICOS / "s4_3_salarios_pais_europe.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# 13. CRUZAMENTO DAS DUAS QUERIES

# O EMPLOYEE_ID é utilizado como chave para juntar as informações
# de cargo da Query 1 com as informações geográficas da Query 2.
dados_integrados = df1.merge(
    df2[
        [
            "EMPLOYEE_ID",
            "REGIAO",
            "SALARIO"
        ]
    ],
    on="EMPLOYEE_ID",
    how="outer",
    validate="one_to_one",
    indicator=True,
    suffixes=("_Q1", "_Q2")
)

print("\n================ VALIDAÇÃO DO CRUZAMENTO ================")

print("Total de registros:", len(dados_integrados))

print("\nCorrespondência entre as consultas:")
print(dados_integrados["_merge"].value_counts())

print(
    "\nSalários divergentes:",
    (
        dados_integrados["SALARIO_Q1"]
        != dados_integrados["SALARIO_Q2"]
    ).sum()
)

print(
    "Funcionários sem região informada:",
    dados_integrados["REGIAO"].isna().sum()
)


# 14. ANÁLISE INTEGRADA — CARGOS E SALÁRIOS POR REGIÃO

print("\n================ CARGOS E SALÁRIOS POR REGIÃO ================")

tabela_cargos_regiao = (
    dados_integrados
    .assign(
        REGIAO=lambda x:
        x["REGIAO"].fillna("Não informado")
    )
    .groupby(
        [
            "REGIAO",
            "CARGO"
        ]
    )["SALARIO_Q1"]
    .agg(
        funcionarios="count",
        media="mean",
        mediana="median",
        minimo="min",
        maximo="max"
    )
    .round(2)
    .reset_index()
    .sort_values(
        ["REGIAO", "mediana"],
        ascending=[True, False]
    )
)

print(
    tabela_cargos_regiao.to_string(index=False)
)

# 15. ANÁLISE EXPLORATÓRIA — FAIXAS SALARIAIS POR REGIÃO

# Essas faixas foram criadas somente para uma análise exploratória
# e não representam faixas oficiais da organização.
dados_integrados["FAIXA_SALARIAL"] = pd.cut(
    dados_integrados["SALARIO_Q1"],
    bins=[
        0,
        3500,
        6000,
        10000,
        float("inf")
    ],
    labels=[
        "Até 3.500",
        "3.501 a 6.000",
        "6.001 a 10.000",
        "Acima de 10.000"
    ]
)

tabela_faixas = pd.crosstab(
    dados_integrados["REGIAO"].fillna("Não informado"),
    dados_integrados["FAIXA_SALARIAL"]
)

print("\nFUNCIONÁRIOS POR FAIXA SALARIAL E REGIÃO")
print(tabela_faixas.to_string())


tabela_percentual = (
    tabela_faixas
    .div(
        tabela_faixas.sum(axis=1),
        axis=0
    )
    * 100
).round(1)

print("\nDISTRIBUIÇÃO PERCENTUAL POR REGIÃO")
print(tabela_percentual.to_string())

# 16. GRÁFICO COMPLEMENTAR —
#     MÉDIA E AMPLITUDE SALARIAL OBSERVADA POR CARGO

# Este gráfico complementa o gráfico da mediana.
# A barra mostra a média salarial observada em cada cargo.
# A linha com hastes mostra o menor e o maior salário
# efetivamente encontrados naquele grupo.

print(
    "\n================ MÉDIA, MÍNIMO E MÁXIMO POR CARGO ================"
)

resumo_cargos_media = (
    df1
    .groupby("CARGO")["SALARIO"]
    .agg(
        funcionarios="count",
        media="mean",
        minimo="min",
        maximo="max"
    )
    .round(2)
    .sort_values("media")
)

print(resumo_cargos_media.to_string())


rotulos_cargos_media = [
    f"{cargo} (n={int(funcionarios)})"
    for cargo, funcionarios in zip(
        resumo_cargos_media.index,
        resumo_cargos_media["funcionarios"]
    )
]


# Distância da média até o menor salário observado.
erro_inferior = (
    resumo_cargos_media["media"]
    - resumo_cargos_media["minimo"]
)

# Distância da média até o maior salário observado.
erro_superior = (
    resumo_cargos_media["maximo"]
    - resumo_cargos_media["media"]
)


fig, ax = plt.subplots(figsize=(12, 10))

# Barra cheia = salário médio observado.
ax.barh(
    rotulos_cargos_media,
    resumo_cargos_media["media"],
    color="steelblue",
    label="Salário médio"
)

# Linha com hastes = mínimo e máximo observados.
ax.errorbar(
    resumo_cargos_media["media"],
    range(len(resumo_cargos_media)),
    xerr=[
        erro_inferior,
        erro_superior
    ],
    fmt="none",
    ecolor="darkorange",
    elinewidth=2,
    capsize=5,
    capthick=2,
    label="Mínimo–máximo observado"
)

ax.set_title(
    "Salário médio e amplitude salarial observada por cargo"
)
ax.set_xlabel("Salário")
ax.set_ylabel("Cargo")
ax.legend()

plt.tight_layout()

plt.savefig(
    PASTA_GRAFICOS / "s4_2b_media_minimo_maximo_por_cargo.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
