# Análise de RH com SQL e Python

**Aluno:** José Humberto de Souza
**Turma:** VISUALIZAÇÃO DE DADOS E BUSINESS INTELLIGENCE [T3]

## Objetivo do projeto

Este projeto tem como objetivo analisar dados de Recursos Humanos com foco em funcionários, cargos, departamentos, salários e distribuição geográfica. O trabalho utiliza consultas SQL para extração dos dados e Python para realizar análise exploratória, cálculos estatísticos e visualizações.

A análise busca compreender principalmente:

- a distribuição dos salários;
- a relação entre cargos, departamentos e remuneração;
- os padrões salariais observados entre regiões e países;
- as diferenças entre média e mediana na interpretação dos salários.

## Ferramentas utilizadas

- **FreeSQL — schema Human Resources (HR):** consulta e extração dos dados;
- **SQL:** construção das consultas e relacionamentos entre as tabelas;
- **Python:** análise exploratória e estatística;
- **Pandas:** manipulação e análise dos dados;
- **Matplotlib:** criação e exportação dos gráficos;
- **VS Code:** desenvolvimento e execução do projeto;
- **Git e GitHub:** controle de versão e publicação do repositório.

## Consultas utilizadas

### Query 1 — Salários por departamento e cargo

A Query 1 relaciona as tabelas de funcionários, departamentos e cargos. O objetivo é analisar salários por departamento e cargo e comparar os salários observados com as faixas mínima e máxima cadastradas para cada cargo.

Foi utilizado o filtro:

`SALARIO >= 10000`

O resultado contém **19 funcionários** e é utilizado principalmente nas análises relacionadas a cargos e faixas salariais.

### Query 2 — Funcionários por região e localização

A Query 2 relaciona funcionários, departamentos, localizações, países e regiões. Seu objetivo é permitir uma análise mais ampla dos salários e de sua distribuição geográfica.

Foi utilizado o filtro:

`SALARIO > 0`

O resultado contém **107 funcionários** e permite analisar salário, departamento, cidade, estado, país e região.

## Estrutura do repositório

O projeto está organizado da seguinte forma:

```text
projeto-rh-sql-python/
├── data/
│   └── raw/
│       ├── query_01.csv
│       └── query_02.csv
├── outputs/
│   └── graficos/
│       ├── s4_1_distribuicao_salarial.png
│       ├── s4_2_salarios_por_cargo.png
│       ├── s4_3_salarios_pais_americas.png
│       └── s4_3_salarios_pais_europe.png
├── sql/
│   ├── query_1.sql
│   └── query_2.sql
├── src/
│   └── analise_rh.py
├── README.md
└── requirements.txt
```

### Função das principais pastas

- **data/raw/** — contém os arquivos CSV exportados a partir das consultas SQL.
- **sql/** — contém as duas consultas executadas para extração dos dados.
- **src/** — contém o script Python responsável pela análise exploratória, cálculos estatísticos e geração dos gráficos.
- **outputs/graficos/** — contém as visualizações finais exportadas pelo script Python.
- **requirements.txt** — registra as principais bibliotecas utilizadas no projeto.
- **README.md** — documenta o objetivo, metodologia, resultados e instruções para execução do projeto.


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


## Preparação do ambiente Python

### Objetivo

Preparar um ambiente de desenvolvimento Python no VS Code para realizar a análise exploratória dos dados extraídos do FreeSQL.

O ambiente utiliza bibliotecas para manipulação de dados, cálculos estatísticos e geração de gráficos.


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
| NumPy | 2.5.3 |
O arquivo `requirements.txt` contém também as demais dependências instaladas no ambiente utilizado no desenvolvimento.

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

### Decisões de Tratamento

Não foi necessário excluir ou corrigir registros.

A funcionária Susan Jacobs possui o campo ESTADO vazio, mas apresenta país e região identificados.

A funcionária Kimberely Grant não possui departamento nem informações geográficas preenchidos.

Os dois registros serão preservados. Nas análises por região, a localização desconhecida será considerada como "Não informado".

Os arquivos CSV originais permanecem inalterados.

### Limitações

A Query 1 contém somente funcionários com salário maior ou igual a 10.000, não representando todos os funcionários.

A Query 2 será utilizada para as análises geográficas. Os funcionários presentes nas duas consultas não serão contabilizados duas vezes.

## Análise estatística dos salários

Foram calculadas estatísticas descritivas com a biblioteca Pandas para compreender a distribuição salarial dos funcionários.

### Resultados da Query 2 — Panorama salarial

A Query 2 apresenta 107 funcionários com salários maiores que zero.

| Indicador | Resultado |
| --- | ---: |
| Quantidade de funcionários | 107 |
| Salário médio | 6.461,83 |
| Salário mediano | 6.200,00 |
| Menor salário | 2.100,00 |
| Maior salário | 24.000,00 |
| Primeiro quartil (25%) | 3.100,00 |
| Terceiro quartil (75%) | 8.900,00 |

A metade central dos salários está entre 3.100,00 e 8.900,00. A média é ligeiramente superior à mediana, indicando uma possível influência dos salários mais elevados sobre o valor médio.

### Resultados da Query 1 — Recorte salarial

A Query 1 apresenta os 19 funcionários com salários iguais ou superiores a 10.000.

| Indicador | Resultado |
| --- | ---: |
| Quantidade de funcionários | 19 |
| Salário médio | 12.632,42 |
| Salário mediano | 11.500,00 |
| Menor salário | 10.000,00 |
| Maior salário | 24.000,00 |

### Influência dos filtros SQL

A Query 1 apresenta média salarial superior à Query 2 porque seleciona apenas os funcionários com salários iguais ou superiores a 10.000.

Como as duas consultas utilizam a mesma base de dados, essa diferença é uma consequência esperada do filtro aplicado, não uma descoberta sobre dois grupos independentes.

A Query 2 oferece uma visão mais abrangente da distribuição salarial dos funcionários.

As comparações por departamento, cargo e região foram realizadas nas etapas seguintes da análise, permitindo identificar diferenças na distribuição salarial e padrões relevantes para a interpretação dos dados de RH.

Os valores salariais são apresentados sem símbolo de moeda, pois a moeda não foi confirmada na documentação da base.

## Perguntas analíticas e principais achados

### 1. Os salários estão dentro das faixas cadastradas para os cargos?

Na Query 1, foram analisados 19 funcionários com salários iguais ou superiores a 10.000. Nenhum deles apresentou salário abaixo do mínimo ou acima do máximo cadastrado para seu respectivo cargo.

Esse resultado se limita aos 19 funcionários selecionados e não permite afirmar que todos os 107 funcionários da base estejam dentro das faixas salariais.

### 2. Como os salários se distribuem pelas regiões dos departamentos?

Na Query 2, foram identificados 70 funcionários associados a departamentos nas Américas, com média salarial de 5.191,66 e mediana de 3.300,00. Na Europa, foram identificados 36 funcionários, com média de 8.916,67 e mediana de 8.900,00. Um funcionário não possui região informada.

Os salários associados aos departamentos europeus são mais elevados tanto pela média quanto pela mediana. Entretanto, esse resultado não demonstra que a localização geográfica seja a causa da diferença.

### 3. A composição dos departamentos ajuda a interpretar as diferenças salariais entre as regiões?

A análise mostrou que o departamento Sales possui 34 funcionários, com mediana salarial de 8.900, enquanto Shipping possui 45 funcionários, com mediana de 3.100.

Todos os funcionários de Sales estão associados à Europe, enquanto os funcionários de Shipping estão associados às Americas.

Esse resultado ajuda a interpretar parte da diferença salarial observada entre as regiões, mas não permite concluir que a localização geográfica seja a causa dessas diferenças, pois a composição dos departamentos também varia entre elas.

### Limitações da análise

- A Query 1 contém somente funcionários com salários iguais ou superiores a 10.000.
- A região registrada representa a localização do departamento, não necessariamente a residência do funcionário.
- Departamentos com poucos funcionários exigem cautela na interpretação das médias.
- As diferenças observadas são descritivas e não demonstram relações de causa e efeito.

## Visualizações finais

As visualizações foram construídas para complementar as estatísticas descritivas e facilitar a interpretação dos principais padrões encontrados nos dados.

### 1. Distribuição salarial — Query 2

![Distribuição salarial](outputs/graficos/s4_1_distribuicao_salarial.png)

O histograma apresenta a distribuição salarial dos 107 funcionários da Query 2. Observa-se maior concentração de funcionários nas faixas salariais inferiores e intermediárias, com uma extensão da distribuição em direção aos salários mais elevados.

A média salarial de 6.461,83 é ligeiramente superior à mediana de 6.200, indicando influência dos valores mais altos sobre a média.

### 2. Mediana salarial por cargo — Query 1

![Mediana salarial por cargo](outputs/graficos/s4_2_salarios_por_cargo.png)

A Query 1 contém 19 funcionários com salários iguais ou superiores a 10.000. Para comparar os cargos foi utilizada a mediana salarial, acompanhada da quantidade de funcionários em cada grupo.

Entre os cargos com mais de um funcionário, Administration Vice President apresenta mediana de 17.000, Sales Manager de 12.000 e Sales Representative de 10.250.

Alguns cargos possuem somente um funcionário no recorte. Nesses casos, a mediana corresponde ao próprio salário individual e não deve ser considerada representativa de um grupo.

### 3. Distribuição salarial por país — Americas

![Distribuição salarial por país — Americas](outputs/graficos/s4_3_salarios_pais_americas.png)

Na região Americas, observa-se forte concentração de funcionários nos Estados Unidos, com predominância de salários nas faixas inferiores e presença de valores mais elevados que ampliam a dispersão.

O Canadá possui poucos registros, portanto sua mediana deve ser interpretada com cautela.

### 4. Distribuição salarial por país — Europe

![Distribuição salarial por país — Europe](outputs/graficos/s4_3_salarios_pais_europe.png)

Na região Europe, a maior parte dos funcionários está concentrada no Reino Unido, onde os salários apresentam distribuição mais concentrada em níveis intermediários e superiores.

A Alemanha possui quantidade muito reduzida de registros e, portanto, seus valores não devem ser interpretados como representativos de um padrão salarial do país.

### Síntese das visualizações

Os gráficos mostram diferenças na distribuição dos salários entre cargos, países e regiões e complementam os resultados estatísticos obtidos na análise.

Essas diferenças são descritivas e não permitem concluir que cargo, departamento, país ou região sejam isoladamente responsáveis pelos níveis salariais observados. Além disso, a variável REGIAO representa a localização do departamento ao qual o funcionário está associado, e não necessariamente seu local de residência.

## Limitações e melhorias futuras

### Limitações

- A Query 1 considera somente funcionários com salários iguais ou superiores a 10.000 e, portanto, não representa o conjunto completo de funcionários.
- A variável REGIAO representa a localização do departamento ao qual o funcionário está associado, e não necessariamente sua residência.
- Alguns cargos, países e departamentos possuem poucos registros, o que exige cautela na interpretação de médias e medianas.
- As diferenças observadas são descritivas e não permitem estabelecer relações de causa e efeito.
- A moeda associada aos valores salariais não foi confirmada na documentação da base.

### Melhorias futuras

Como evolução do projeto, poderiam ser incorporadas novas análises, como:

- incluir cargo na análise geográfica para comparar remuneração de funções semelhantes entre regiões;
- ampliar as visualizações para relacionar cargos, departamentos e localização;
- criar indicadores adicionais de dispersão salarial;
- estruturar um painel interativo em ferramenta de Business Intelligence.

## Limitações e melhorias futuras

### Limitações

- A Query 1 considera somente funcionários com salários iguais ou superiores a 10.000 e, portanto, não representa o conjunto completo de funcionários.
- A variável REGIAO representa a localização do departamento ao qual o funcionário está associado, e não necessariamente sua residência.
- Alguns cargos, países e departamentos possuem poucos registros, o que exige cautela na interpretação de médias e medianas.
- As diferenças observadas são descritivas e não permitem estabelecer relações de causa e efeito.
- A moeda associada aos valores salariais não foi confirmada na documentação da base.

### Melhorias futuras

Como evolução do projeto, poderiam ser incorporadas novas análises, como:

- incluir cargo na análise geográfica para comparar remuneração de funções semelhantes entre regiões;
- ampliar as visualizações para relacionar cargos, departamentos e localização;
- criar indicadores adicionais de dispersão salarial;
- estruturar um painel interativo em ferramenta de Business Intelligence.

## Como executar o projeto

A execução deve ser realizada a partir da pasta raiz do repositório.

### 1. Criar o ambiente virtual

```powershell
py -m venv .venv
```

### 2. Ativar o ambiente virtual no Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 4. Executar a análise

```powershell
python src/analise_rh.py
```

O script carrega os arquivos `data/raw/query_01.csv` e `data/raw/query_02.csv`, executa a análise exploratória e estatística e gera os gráficos finais na pasta:

```text
outputs/graficos/
```

Os arquivos CSV originais devem permanecer em `data/raw/`, pois representam os resultados exportados das consultas SQL.