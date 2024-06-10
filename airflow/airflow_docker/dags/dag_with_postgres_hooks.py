import csv
import logging
from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile

from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow.providers.postgres.hooks.postgres import PostgresHook

from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
    'owner': 'zshearin',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

def postgres_to_s3(ds_nodash, next_ds_nodash):

    # step 1 - read from db and save to text file
    hook = PostgresHook(
        postgres_conn_id="postgres_localhost" #comes from postgres connection in admin page on airflow UI already set up
    )
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from public.orders where date >= %s and date < %s",
                   (ds_nodash, next_ds_nodash))

    with NamedTemporaryFile(mode='w',suffix=f'{ds_nodash}') as f:
    # with open(f"dags/get_orders_{ds_nodash}.txt", 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
        cursor.close()
        conn.close()
        logging.info("Saved orders data in text file: %s", f"dags/get_orders_{ds_nodash}.txt")

    # step 2 - upload text file to s3
        s3_hook = S3Hook(
            aws_conn_id="minio_conn" # from admin connections in airflow
        )
        s3_hook.load_file(
            filename=f.name, #f"dags/get_orders_{ds_nodash}.txt",
            key=f"orders/{ds_nodash}.txt", 
            bucket_name="airflow", # bucket we created in minio
            replace=True # replace the file if it already exists
        )
        logging.info("Orders file %s has been pushed to S3!", f.name)

with DAG(
    dag_id='dag_with_postgres_hooks_v05',
    default_args=default_args,
    # NOTE: I added a a start and end date to limit the dags from running like 700 times and creating a bunch of junk files
    start_date=datetime(2022,4,29),
    end_date=datetime(2022,5,5),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id="postgres_to_s3",
        python_callable=postgres_to_s3
    )
    task1