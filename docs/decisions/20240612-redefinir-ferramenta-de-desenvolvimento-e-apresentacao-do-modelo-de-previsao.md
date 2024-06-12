# Define the provider and stack to delivery the project

- Status: superseded by [20240612-redefinir-ferramenta-de-desenvolvimento-e-apresentacao-do-modelo-de-previsao](20240612-redefinir-ferramenta-de-desenvolvimento-e-apresentacao-do-modelo-de-previsao.md) 
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
- Jupyter

## Considered Options

- AWS e Red Shift
- Azure e Databricks
- … <!-- numbers of options can vary -->

## Decision Outcome

Escolhemos utilizar GCP com BigQuery pois são as ferramenta mais utilizadas pelos integrantes e se integra bem com dbt

### Positive Consequences <!-- optional -->



### Negative Consequences <!-- optional -->
