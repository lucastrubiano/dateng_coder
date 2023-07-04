from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner': 'LucasT',
    'retries': 5,
    'retry_delay': timedelta(minutes=2) # 2 min de espera antes de cualquier re intento
}

with DAG(
    dag_id="mi_primer_dag_v3",
    default_args= default_args,
    description="DAG de ejemplo para imprimir en logs",
    start_date=datetime(2022,9,3,2),# esto dice que debemos iniciar el 1-Ago-2022 y a un intervalo diario
    schedule_interval='@daily' ) as dag:
    task1= BashOperator(task_id='primera_tarea',
    bash_command="echo 'Buen martes'"
    )

    task2 =BashOperator(
        task_id='segunda_tarea',
        bash_command="echo 'Hola Lucas'"
    )

    task3 =BashOperator(
        task_id= 'tercera_tarea',
        bash_command="echo 'Hola Fer'"
    )
    task1 >> task2
    task1 >> task3