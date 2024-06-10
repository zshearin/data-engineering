from datetime import datetime, timedelta
from airflow import DAG

#since we're using bash operator for our task in our dag:
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'zshearin',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2024, 6, 1, 2), # start on 29th of July and run at 2am
    schedule_interval='@daily' # how frequently to run 
) as dag:
    # pass
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo hello world from task1!'
    )
    task2 = BashOperator(
        task_id='task2',
        bash_command='echo I am the second task - runs after task1'
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo I am third task - running in parallel with task2'
    )

# Task dependency method 1:
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

# Task dependency method 2 ():
# task1 >> task2
# task1 >> task3
task1 >> [task2, task3] # is equivalent to the above 2 lines