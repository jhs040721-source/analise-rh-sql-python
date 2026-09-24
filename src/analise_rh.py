import pandas as pd

import pandas as pd

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
