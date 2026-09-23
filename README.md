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
- Preparação do ambiente Python e análise dos dados: próximas etapas.
