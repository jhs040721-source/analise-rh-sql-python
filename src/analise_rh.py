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