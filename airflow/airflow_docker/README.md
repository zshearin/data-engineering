All the examples in this folder follow [this](https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=1435s&ab_channel=coder2j) youtube video.

Each module in the video corresponds to a python file in the `dags` directory, demonstrating a new concept to learn with dags, airflow and connecting to external services

Data used for this (only a couple dags use it) is located in `data` folder

I created my own make targets to run several of the things in 
To get started, run:
```
make init
make start

```
To do examples with s3 (ie minio as replacement interface), run:
```
make run-minio
```

## s3 example
1. Run minio with `make run-minio`
- This runs a web UI on port 9001 and the api on port 9000

2. Exec into airflow scheduler container and run pip list | grep amazon to find out python package version
```
docker ps -a | grep scheduler
docker exec -it <container id from last command> bash
pip list | grep amazon
```

3. Go [here](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html), select right version from the previous command, and click `Python API` in the left-hand column.

4. Find `sensor s3` in the documentation and import the one that references sensing a file

5. Modifications to video:

S3 was chosen as the connection type, which is no longer an option.  Choose `Amazon Web Services` instead (see [this](https://stackoverflow.com/questions/75465865/airflow-s3-connection-type-is-missing) stack overflow conversation for explanation why). Also username and password for minio container were added to the extras in the video.  Instead, there is now the `AWS Access Key ID` - which is for the username and `AWS Secret Access Key` which is for the password. Also needed to use this json as the `extras` field:
```
{
  "service_config": {
    "s3": {
      "bucket_name": "airflow"
    }
  },
  "endpoint_url": "http://host.docker.internal:9000"
}
```
## Minio:
https://min.io/docs/minio/container/index.html


## Postgres with s3 example

1. Create postrgreSQL database named `test` with dbeaver

2. Create table in it, then upload data to it (see `data/Orders.csv` - use this and import, fields should map directly - Next > Next > Proceed): 

```
create table if not exists public.orders (
    order_id character varying,
    date date,
    product_name character varying,
    quantity integer,
    primary key (order_id)
)
```

3. Verify data is in the database created:
`select * from public.orders limit 100;`

4. Exec into airflow scheduler container and run `pip list | grep postgres` to find out python package version
```
docker ps -a | grep scheduler
docker exec -it <container id from last command> bash
pip list | grep postgres 
```

5. Go to documentation located [here](https://airflow.apache.org/docs/).

6. Click `PostgreSQL`, select version that was output from the pip command and select `Python API` from the left column.  Then click `hooks` subpackage. Grab package with the documentation and paste into python code to import.

7. Do the same thing except with amazon and s3 package to find s3 hook and required parameters (in this case was `S3Hook` object and `load_file` function)
