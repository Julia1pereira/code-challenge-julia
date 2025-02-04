# Desafio engenharia de dados Incidium
O objetivo do desafio era implementar um pipeline de dados, desde a extração até o carregamento das informações em um destino final.
Para a realização do desafio, utilizei ferramentas para engenharia de dados Meltano, Apache Airflow, PostgreSQL e DBearver. 

# Instruções para execução do pipeline

Os requisitos básicos para instalação são ter o Python 3, Git e Docker instalados na máquina.
- Instalar arquivos e ferramentas
Os arquivos do projeto estão disponíveis no link. Para clonar, abra o terminal e execute os comando (é importante clonar os arquivos em /home/usuário):
```
git clone https://github.com/Julia1pereira/code-challenge-julia.git
```
Para instalar as ferramentas execute os comandos:
Terminal 1:
```
python3 -m venv meltano-venv
source meltano-venv/bin/activate
pip install meltano
```
Terminal 2:
```
python3 -m venv airflow-venv
source airflow-venv/bin/activate
pip install apache-airflow
```
Para mais informações sobre como instalar o Airflow, acesse o [link](https://medium.com/orchestras-data-release-pipeline-blog/installing-and-configuring-apache-airflow-a-step-by-step-guide-5ff602c47a36).

- Configurando o ambiente 
Em um novo terminal, execute o comando para adicionar o arquivo com a DAG a lista de DAGs do Airflow:
```
mv ~/code-challenge-julia/airflow/dags/pipeline_northwind.py ~/airflow/dags
```
Também suba os container Docker disponíveis para a criação dos bancos de dados.
No terminal 1, execute os comandos para instalar os plugins do meltano:
```
cd code-challenge-julia/meltano
meltano install
```

- Executando o pipeline
Acesse o webserver do Apache Airflow em localhost:8080, procure pela DAG chamada pipeline_northwind e a ative.
O resultado deve aparecer dentro da pasta code-challenge-julia/data/extract/csv e code-challenge-julia/data/extract/postgres, como a imagem abaixo:

- Executando as consultas no banco
Para essa etapa, sugiro usar a ferramenta DBeaver para executar as consultas ([documentação](https://dbeaver.com/docs/dbeaver/Create-Connection/)). Execute primeiro o arquivo fix_table.sql para garantir a integridade do banco. Depois, execute as consultas orders_period.sql, order-per-customer.sql e most-ordered.sql.
