from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'zshearin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import matplotlib 
    print("matplotlib with version: {matplotlib.__version__}")

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_dependencies_v01',
    description='first dag with python operator',
    start_date=datetime(2024, 6, 7),
    schedule_interval='@daily'
) as dag:
    get_sklearn_task = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )

    get_sklearn_task

