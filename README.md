# Tech Mack Crazy - Sales Predicton
 
![Texto Alternativo](https://seeklogo.com/images/U/Universidade_Presbiteriana_Mackenzie-logo-EE4C00D51D-seeklogo.com.png)
 
## Visão Geral
Este projeto tem como objetivo [descrição do objetivo do projeto]. Utilizamos log4brains para gerenciar ADRs, Airflow para orquestrar o pipeline de ingestão e dbt para transformar os dados.
 
## Tecnologias Utilizadas
 
- **WSL (versão 2)**: É uma camada de compatibilidade desenvolvida pela Microsoft que permite rodar um ambiente GNU/Linux diretamente no Windows, sem a necessidade de máquinas virtuais ou configuração de dual-boot. Com o WSL, os usuários podem executar binários Linux nativos em uma interface de linha de comando Windows.
 
- **git**: Versionamento do projeto.
 
- **git flow extension**: É um conjunto de scripts e práticas que facilitam a implementação de um modelo de ramificação (branching) bem estruturado no Git.
 
- **ssh-keygen**: Uma ferramenta de linha de comando usada para gerar, gerenciar e converter chaves de autenticação SSH (Secure Shell). SSH é um protocolo que permite a comunicação segura entre dispositivos na rede, e as chaves SSH são usadas para autenticação baseada em chave pública, uma forma mais segura e conveniente de autenticação comparada ao uso de senhas.
 
- **log4brains**: Ferramenta para gerenciar registros de decisões arquiteturais (ADRs).
 
- **Airflow**: Plataforma para orquestração de workflows que utilizamos para gerenciar o pipeline de ingestão de dados.
 
- **dbt**: Ferramenta para transformação de dados que permite modelar, transformar e documentar os dados de forma eficiente.
 
## Estrutura do Projeto
- `/dags`: Contém os DAGs do Airflow para orquestração dos workflows.
- `/dbt`: Contém os modelos, testes e documentação do dbt.
- `/adrs`: Contém os registros de decisões arquiteturais gerenciados pelo log4brains.
 
## Configuração do Ambiente
 
### Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas:
- Python 3.8+
- Apache Airflow
- dbt
- log4brains
 
### Passo a Passo
 
1. **Clone o Repositório**
   ``` bash
   git clone https://github.com/usuario/projeto-de-dados.git
   cd projeto-de-dados
   ```
 
2. **Configuração do log4brains**
 
 - Para utilizar o log4brains será necessário a instalação do npm (Node Package Manager) que é o gerenciador de pacotes padrão para o ambiente de execução JavaScript Node.js. Ele permite que os desenvolvedores instalem, compartilhem e gerenciem bibliotecas e ferramentas JavaScript.