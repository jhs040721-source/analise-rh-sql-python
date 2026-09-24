# Análise de RH com SQL e Python
## Mapeamento inicial das tabelas HR

### Consulta de salários por departamento e cargo
- `HR.EMPLOYEES` é a tabela principal.
- `EMPLOYEES.DEPARTMENT_ID` se relaciona com `DEPARTMENTS.DEPARTMENT_ID`.
- `EMPLOYEES.JOB_ID` se relaciona com `JOBS.JOB_ID`.

### Consulta de funcionários por região e localização
- `EMPLOYEES.DEPARTMENT_ID` → `DEPARTMENTS.DEPARTMENT_ID`
- `DEPARTMENTS.LOCATION_ID` → `LOCATIONS.LOCATION_ID`
- `LOCATIONS.COUNTRY_ID` → `COUNTRIES.COUNTRY_ID`
- `COUNTRIES.REGION_ID` → `REGIONS.REGION_ID`
## Origem e extração dos dados

Os dados são provenientes do esquema de exemplo Human Resources (HR),
consultado no Oracle FreeSQL, para fins educacionais.

As consultas SQL estão armazenadas em `sql/`. Seus resultados foram
exportados em CSV pelo FreeSQL e salvos em `data/raw/`.

## Arquivos disponíveis

| Consulta | Arquivo SQL | Resultado CSV | Registros | Colunas |
| --- | --- | --- | --- | --- |
| Query 1 | `sql/query_1.sql` | `data/raw/query_01.csv` | 19 | 7 |
| Query 2 | `sql/query_2.sql` | `data/raw/query_02.csv` | 107 | 8 |

As quantidades de registros não incluem a linha de cabeçalho.

### Query 1 — Salários, departamentos e cargos

Seleciona funcionários com salário maior ou igual a 10000.
Inclui departamento, cargo e limites salariais do cargo,
com ordenação por salário decrescente.

Esse resultado representa um recorte salarial e não deve ser
interpretado como o conjunto completo de funcionários.

### Query 2 — Localização dos departamentos dos funcionários

Seleciona funcionários com salário maior que zero.
Inclui departamento, cidade, estado, país e região.

A localização corresponde ao departamento ao qual o funcionário
está vinculado, não necessariamente ao seu local de residência.

## Preservação e uso dos dados

- Os CSVs em `data/raw/` são preservados sem limpeza ou edição manual dos dados.
- Campos vazios da exportação devem ser mantidos nos arquivos originais.
- Futuras versões tratadas serão armazenadas em `data/processed/`.
- Os dois resultados contêm funcionários em comum. Não devem ser
  simplesmente concatenados para calcular estatísticas gerais.
- A moeda dos salários não foi confirmada; os valores não são
  apresentados como reais (R$).

## Situação da etapa de extração

- Consultas SQL e CSVs publicados na branch `main`.
- CSVs abertos no VS Code para conferência de legibilidade.
- Commit de inclusão dos CSVs: `f9f881d`.
- Commit de integração dos CSVs à main: `2179e33`.
- Preparação do ambiente Python: concluída e documentada. Análise exploratória dos dados: próxima etapa.

## Preparação do ambiente Python

### Objetivo

Preparar um ambiente de desenvolvimento Python no VS Code para realizar a análise exploratória dos dados extraídos do FreeSQL.

O ambiente utiliza bibliotecas para manipulação de dados, cálculos estatísticos e geração de gráficos.

### Ferramentas utilizadas

- Python: linguagem de programação utilizada na análise.
- VS Code: editor de código e ambiente de desenvolvimento.
- Pandas: manipulação, organização e análise de dados.
- Matplotlib: criação de gráficos e visualizações.
- Seaborn: visualização estatística dos dados.
- Git e GitHub: controle de versões e publicação do projeto.

### Criação do ambiente virtual

O ambiente virtual permite instalar e utilizar bibliotecas específicas para o projeto, mantendo suas dependências separadas de outros projetos Python.

No terminal PowerShell, a partir da pasta raiz do projeto, executar:

```powershell
py -m venv .venv
```

Para ativar o ambiente virtual no Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Após a ativação, o terminal deverá apresentar o identificador `(.venv)`.

No VS Code, selecionar o interpretador Python localizado em:

`.venv\Scripts\python.exe`

### Instalação das dependências

As bibliotecas necessárias ao projeto estão registradas no arquivo `requirements.txt`.

Com o ambiente virtual ativado, executar:

```powershell
python -m pip install -r requirements.txt
```

O comando instala as dependências e suas respectivas versões, permitindo reproduzir o ambiente utilizado no desenvolvimento.

As principais bibliotecas instaladas são:

| Biblioteca | Versão |
| --- | --- |
| Pandas | 3.0.6 |
| Matplotlib | 3.11.2 |
| Seaborn | 0.13.2 |

### Teste de reprodução do ambiente

Para verificar se o ambiente poderia ser reconstruído a partir do arquivo `requirements.txt`, foi criado um ambiente virtual temporário denominado `.venv-teste`.

A instalação das dependências foi realizada utilizando diretamente o interpretador desse ambiente:

```powershell
.\.venv-teste\Scripts\python.exe -m pip install -r requirements.txt
```

Após a instalação, foram testadas as importações das bibliotecas Pandas, Matplotlib e Seaborn.

O teste confirmou o funcionamento das três bibliotecas e retornou as versões esperadas.

Depois da validação, o ambiente temporário foi removido, preservando o ambiente principal `.venv`.

### Controle de arquivos com .gitignore

O arquivo `.gitignore` contém regras para impedir o versionamento de ambientes virtuais, arquivos temporários e configurações locais.

Entre os diretórios e arquivos ignorados estão:

- `.venv/`: ambiente virtual principal.
- `.venv-teste/`: ambiente virtual temporário de teste.
- `__pycache__/`: arquivos temporários gerados pelo Python.
- `.env`: arquivo local de configuração.
- `.vscode/`: configurações locais do editor.

A verificação com o comando `git status --short` confirmou que os arquivos dos ambientes virtuais não apareciam entre as alterações identificadas pelo Git.

### Resultado da preparação

O ambiente Python foi configurado no VS Code e as dependências necessárias foram instaladas e testadas.

O teste em um ambiente temporário confirmou que a instalação das bibliotecas pode ser reproduzida a partir do arquivo `requirements.txt`.


## Verificação da qualidade dos dados

Foram realizadas verificações de valores ausentes, registros duplicados e consistência dos salários utilizando a biblioteca Pandas.

### Resultados

- Query 1: nenhum valor ausente ou registro duplicado.
- Query 2: nenhum registro duplicado. Foram identificados dois funcionários com informações geográficas incompletas.
- Os salários das duas consultas respeitam os filtros estabelecidos no SQL.

### Tratamento dos dados

Não foi necessário excluir ou corrigir registros.

A funcionária Susan Jacobs possui o campo ESTADO vazio, mas apresenta país e região identificados.

A funcionária Kimberely Grant não possui departamento nem informações geográficas preenchidos.

Os dois registros serão preservados. Nas análises por região, a localização desconhecida será considerada como "Não informado".

Os arquivos CSV originais permanecem inalterados.

### Limitações

A Query 1 contém somente funcionários com salário maior ou igual a 10.000, não representando todos os funcionários.

A Query 2 será utilizada para as análises geográficas. Os funcionários presentes nas duas consultas não serão contabilizados duas vezes.


