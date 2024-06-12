# Define the provider and stack to delivery the project

- Status: accepted 
- Tags: arquitetura, stack

Technical Story: [Issue #1](https://github.com/techmackcrazy/ml-sales-prediction/issues/1)

## Context and Problem Statement

Definir qual provedor de nuvem escolher para executar o projeto, bem como a stack que utilizaremos para desenvolver os processos de ingestão, transformação, modelo de previsão de vendas e ferramenta de dataviz que estejam de acordo com todos os integrantes.

## Decision Makers

- Carolina Attili - Governança
- Henrique Arduinni -  Devops
- Matheus Vieger - Engenheiro de Dados
- Rafael Medeiros - Product Owner / Engenheiro de Dados


## Decision Drivers <!-- optional -->

- GCP - Ferramenta mais utilizada pelos integrantes e se integra bem com dbt
- BigQuery - É um dos três principais data warehouses modernos e se integra nativamente com o dbt
- Notebook(Jupyter) - Posteriormente poderá ser utilizado o Tableau, mas será usado a princípio o Jupyter para
plotagem de gráficos

## Considered Options

- AWS e Red Shift
- Azure e Databricks
- … <!-- numbers of options can vary -->

## Decision Outcome

Escolhemos utilizar GCP com BigQuery pois são as ferramenta mais utilizadas pelos integrantes e se integra bem com dbt

### Positive Consequences <!-- optional -->

- [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
- …

### Negative Consequences <!-- optional -->

- [e.g., compromising quality attribute, follow-up decisions required, …]
- …

## Pros and Cons of the Options <!-- optional -->

### [option 1]

[example | description | pointer to more information | …] <!-- optional -->

- Good, because [argument a]
- Good, because [argument b]
- Bad, because [argument c]
- … <!-- numbers of pros and cons can vary -->

### [option 2]

[example | description | pointer to more information | …] <!-- optional -->

- Good, because [argument a]
- Good, because [argument b]
- Bad, because [argument c]
- … <!-- numbers of pros and cons can vary -->

### [option 3]

[example | description | pointer to more information | …] <!-- optional -->

- Good, because [argument a]
- Good, because [argument b]
- Bad, because [argument c]
- … <!-- numbers of pros and cons can vary -->

## Links <!-- optional -->

- [Link type](link to adr) <!-- example: Refined by [xxx](yyyymmdd-xxx.md) -->
- … <!-- numbers of links can vary -->
