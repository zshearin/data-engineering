from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'zshearin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# def greet(taskName):
    # print('Hello world from ' + taskName)

def greet(ti):
    # name = ti.xcom_pull(task_ids='get_name')
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello world! My name is {first_name} {last_name} and I am {age} years old")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_name', value='Seinfeld')

def get_age(ti):
    ti.xcom_push(key='age', value=20)

with DAG(
    default_args=default_args,
    dag_id='python_operator_dag_v06',
    description='first dag with python operator',
    start_date=datetime(2024, 6, 7),
    schedule_interval='@daily'
) as dag:
    greetTask = PythonOperator(
        task_id="greet",
        python_callable=greet
    )
    
    getNameTask = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    getAgeTask = PythonOperator(
        task_id="get_age",
        python_callable=get_age
    )

    [getNameTask, getAgeTask] >> greetTask 
