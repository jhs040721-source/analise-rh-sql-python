import pandas as pd
from pathlib import Path

PASTA_GRAFICOS = Path("outputs/graficos")
PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)

# Importar o primeiro conjunto de dados
df1 = pd.read_csv("data/raw/query_01.csv")

# Exibir os primeiros registros
print(df1.head())


# Importar o segundo conjunto de dados
df2 = pd.read_csv("data/raw/query_02.csv")

# Exibir os primeiros registros
print(df2.head())

# Verificar as dimensões dos conjuntos de dados
print("\nDimensões da Query 1:", df1.shape)
print("Dimensões da Query 2:", df2.shape)

# Identificar as colunas e seus tipos de dados
print("\nCOLUNAS E TIPOS — QUERY 1")
print(df1.dtypes)

print("\nCOLUNAS E TIPOS — QUERY 2")
print(df2.dtypes)
# Verificar valores ausentes

print("\nVALORES AUSENTES — QUERY 1")
print(df1.isna().sum())

print("\nVALORES AUSENTES — QUERY 2")
print(df2.isna().sum())

# Verificar registros duplicados

print("\nDUPLICIDADES — QUERY 1")
print("Linhas duplicadas:", df1.duplicated().sum())
print("Funcionários repetidos:", df1["EMPLOYEE_ID"].duplicated().sum())

print("\nDUPLICIDADES — QUERY 2")
print("Linhas duplicadas:", df2.duplicated().sum())
print("Funcionários repetidos:", df2["EMPLOYEE_ID"].duplicated().sum())

# Verificar a consistência dos salários

print("\nVERIFICAÇÃO DOS SALÁRIOS")

print("Query 1 - Salários abaixo de 10000:")
print((df1["SALARIO"] < 10000).sum())

print("Query 2 - Salários menores ou iguais a zero:")
print((df2["SALARIO"] <= 0).sum())

# Identificar funcionários com localização incompleta

colunas = ["DEPARTAMENTO", "CIDADE", "ESTADO", "PAIS", "REGIAO"]

incompletos = df2[df2[colunas].isna().any(axis=1)]

print("\nFUNCIONÁRIOS COM LOCALIZAÇÃO INCOMPLETA")
print(incompletos.to_string(index=False))

# Estatísticas salariais da Query 2


print("\nESTATÍSTICAS SALARIAIS — QUERY 2")

print("Quantidade de funcionários:", df2["SALARIO"].count())
print("Salário médio:", df2["SALARIO"].mean())
print("Salário mediano:", df2["SALARIO"].median())

# Identificar os salários mínimo e máximo

print("Menor salário:", df2["SALARIO"].min())
print("Maior salário:", df2["SALARIO"].max())


# Calcular os quartis salariais da Query 2

print("\nQUARTIS SALARIAIS — QUERY 2")

print("Primeiro quartil (25%):", df2["SALARIO"].quantile(0.25))
print("Segundo quartil (50%):", df2["SALARIO"].quantile(0.50))
print("Terceiro quartil (75%):", df2["SALARIO"].quantile(0.75))

# Estatísticas salariais da Query 1

print("\nESTATÍSTICAS SALARIAIS — QUERY 1")

print("Quantidade de funcionários:", df1["SALARIO"].count())
print("Salário médio:", df1["SALARIO"].mean())
print("Salário mediano:", df1["SALARIO"].median())
print("Menor salário:", df1["SALARIO"].min())
print("Maior salário:", df1["SALARIO"].max())
# Conferir as colunas disponíveis para as perguntas analíticas

print("\nCOLUNAS DA QUERY 1")
print(df1.columns.tolist())

print("\nCOLUNAS DA QUERY 2")
print(df2.columns.tolist())
# Verificar salários em relação às faixas previstas para os cargos

print("\nSALÁRIOS E FAIXAS DOS CARGOS — QUERY 1")

print(
    df1[
        ["CARGO", "SALARIO", "SALARIO_MINIMO_CARGO", "SALARIO_MAXIMO_CARGO"]
    ].head(10).to_string(index=False)
)

print(
    "Salários abaixo do mínimo do cargo:",
    (df1["SALARIO"] < df1["SALARIO_MINIMO_CARGO"]).sum()
)

print(
    "Salários acima do máximo do cargo:",
    (df1["SALARIO"] > df1["SALARIO_MAXIMO_CARGO"]).sum()
)
# Quantidade de funcionários por região — Query 2

print("\nFUNCIONÁRIOS POR REGIÃO — QUERY 2")

funcionarios_por_regiao = (
    df2["REGIAO"]
    .fillna("Não informado")
    .value_counts()
)

print(funcionarios_por_regiao)
print("Total de funcionários:", funcionarios_por_regiao.sum())
# Estatísticas salariais por região — Query 2

print("\nESTATÍSTICAS SALARIAIS POR REGIÃO — QUERY 2")

salarios_por_regiao = (
    df2.assign(REGIAO=df2["REGIAO"].fillna("Não informado"))
    .groupby("REGIAO")["SALARIO"]
    .agg(
        funcionarios="count",
        media="mean",
        mediana="median"
    )
    .round(2)
)

print(salarios_por_regiao)
# Estatísticas salariais por departamento — Query 2

print("\nESTATÍSTICAS SALARIAIS POR DEPARTAMENTO — QUERY 2")

salarios_por_departamento = (
    df2.assign(
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
# Verificar onde estão os funcionários de Sales e Shipping

print("\nSALES E SHIPPING POR REGIÃO — QUERY 2")

sales_shipping = df2[
    df2["DEPARTAMENTO"].isin(["Sales", "Shipping"])
].copy()

print(
    pd.crosstab(
        sales_shipping["DEPARTAMENTO"],
        sales_shipping["REGIAO"].fillna("Não informado")
    ).to_string()
)
import matplotlib.pyplot as plt

# Histograma da distribuição salarial — Query 2

media_salario = df2["SALARIO"].mean()
mediana_salario = df2["SALARIO"].median()

print("\nTESTE DO GRÁFICO")
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

# Quantidade de funcionários por cargo — Query 1

print("\nFUNCIONÁRIOS POR CARGO — QUERY 1")

funcionarios_por_cargo = df1["CARGO"].value_counts()

print(funcionarios_por_cargo)
print("Total de funcionários:", funcionarios_por_cargo.sum())

# Mediana salarial por cargo — Query 1

print("\nMEDIANA SALARIAL POR CARGO — QUERY 1")

salarios_por_cargo = (
    df1.groupby("CARGO")["SALARIO"]
    .agg(
        funcionarios="count",
        mediana="median"
    )
    .sort_values("mediana", ascending=False)
)

print(salarios_por_cargo.to_string())
# Gráfico da mediana salarial por cargo — Query 1

salarios_por_cargo_grafico = (
    df1.groupby("CARGO")["SALARIO"]
    .agg(
        funcionarios="count",
        mediana="median"
    )
    .sort_values("mediana")
)

rotulos_cargos = [
    f"{cargo} (n={int(funcionarios)})"
    for cargo, funcionarios in zip(
        salarios_por_cargo_grafico.index,
        salarios_por_cargo_grafico["funcionarios"]
    )
]

plt.figure(figsize=(11, 7))

plt.barh(
    rotulos_cargos,
    salarios_por_cargo_grafico["mediana"]
)
for indice, valor in enumerate(salarios_por_cargo_grafico["mediana"]):
    plt.text(
        valor + 300,
        indice,
        f"{valor:.0f}",
        va="center"
    )

plt.title("Mediana salarial por cargo — Query 1 (salários ≥ 10.000)")
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

# ============================================================
# S4.3 — Distribuição dos salários por país e região
# ============================================================

print("\nS4.3 — FUNCIONÁRIOS POR PAÍS E REGIÃO")

# Separação das duas regiões analisadas
americas = df2[df2["REGIAO"] == "Americas"].copy()
europe = df2[df2["REGIAO"] == "Europe"].copy()

# Quantidade de funcionários por país
print("\nAmericas:")
print(americas.groupby("PAIS").size().sort_values(ascending=False))

print("\nEurope:")
print(europe.groupby("PAIS").size().sort_values(ascending=False))

# ------------------------------------------------------------
# Gráfico 1 — Americas
# ------------------------------------------------------------

import numpy as np
np.random.seed(42)

paises_americas = americas["PAIS"].dropna().unique()

plt.figure(figsize=(8, 5))

for posicao, pais in enumerate(paises_americas):
    dados_pais = americas[
        americas["PAIS"] == pais
    ]["SALARIO"]

    # Pequena dispersão horizontal para visualizar pontos repetidos
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

    # Mediana salarial do país
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


# ------------------------------------------------------------
# Gráfico 2 — Europe
# ------------------------------------------------------------

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

