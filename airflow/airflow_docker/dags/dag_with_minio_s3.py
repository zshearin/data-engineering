from datetime import datetime, timedelta
from airflow import DAG

# from steps in readme:
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner': 'zshearin',
    'retry_delay': timedelta(minutes=10),
    'retries': 5
}

with DAG(
    dag_id='dag_with_minio_s3_v02',
    default_args=default_args,
    start_date=datetime(2024,6,8),
    schedule_interval='@daily'
) as dag:

    task1=S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow', #bucket we created in minio
        bucket_key='data.csv', #file we created in the bucket
        aws_conn_id='minio_conn', # connection created in airflow UI - see README for more details on configuring
        mode='poke',
        poke_interval=5, # 5 seconds - interval between "poking" for a check for the file
        timeout=30 #30 seconds
    )
    task1