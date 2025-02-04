from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import date, datetime

root = "$HOME/"

# Criando o pipeline
with DAG(
    dag_id="pipeline",
    start_date=datetime(2021, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    starting_1 = BashOperator(
        task_id="starting_1",
        bash_command="echo Iniciando o step 1..."
    )

    extract_csv = BashOperator(
        task_id="extract_csv",
        bash_command=f"source {root}meltano-venv/bin/activate && export CURRENT_DATE=$(date +%F) && cd {root}LD_ED_JULIAPEREIRA/meltano && meltano run tap-csv-details target-csv-details"
    )

    extract_postgres = BashOperator(
        task_id="extract_postgres",
        bash_command=f"source {root}meltano-venv/bin/activate && export CURRENT_DATE=$(date +%F) && cd {root}LD_ED_JULIAPEREIRA/meltano && meltano run tap-postgres target-csv-tables"
    )
    
    starting_2 = BashOperator(
        task_id="starting_2",
        bash_command="echo Step 1 finalizado! Iniciando o step 2..."
    )
    
    loader = BashOperator(
        task_id="loader",
        bash_command=f"source {root}meltano-venv/bin/activate && export CURRENT_DATE=$(date +%F) && cd {root}LD_ED_JULIAPEREIRA/meltano && meltano run tap-csv-all target-postgres"
    )

    starting_1 >> [extract_csv, extract_postgres] >> starting_2 >> loader
