from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args= {
    'owner': 'zshearin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# with the dag decorator
@dag(dag_id='dag_with_taskflow_api_v02',
     default_args=default_args,
     start_date=datetime(2024,6,7),
     schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'Seinfeld'
        }
    
    @task()
    def get_age():
        return 25
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello my name is {first_name} {last_name} "
              f"and I am {age} years old")
    
    name_dict=get_name()
    age=get_age()
    greet(first_name=name_dict['first_name'], 
          last_name=name_dict['last_name'], 
          age=age)

greet_dag=hello_world_etl()
        