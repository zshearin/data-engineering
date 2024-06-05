URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

build:
	docker build -t taxi_ingest:v001 .
run:
	docker run -it taxi_ingest:v001 \
	  --user=root \
	  --password=root \
	  --host=localhost \
	  --port=5432 \
	  --db=ny_taxi \
	  --table_name=yellow_taxi_trips \
	  --url=${URL}

# run postgres database using `ny_taxi_postgres_data` as volume mount
run-db:
	docker run -it \
	  -e POSTGRES_USER="root" \
	  -e POSTGRES_PASSWORD="root" \
	  -e POSTGRES_DB="ny_taxi" \
	  -v $(shell pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
	  -p 5432:5432 \
	  postgres:13

# exec into container using pgcli tool:
run-cli:
	pgcli -h localhost -p 5432 -u root -d ny_taxi

run-pgadmin:
	docker run -it \
	  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
	  -e PGADMIN_DEFAULT_PASSWORD="root" \
	  -p 8080:80 \
	  --network=pg-network \
	  --name pg-admin \
	  dpage/pgadmin4

run-create-network:
	docker network create pg-network

run-script:
	python3 ingest_data.py \
	  --user=root \
	  --password=root \
	  --host=localhost \
	  --port=5432 \
	  --db=ny_taxi \
	  --table_name=yellow_taxi_trips \
	  --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-01.csv.gz