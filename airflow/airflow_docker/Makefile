
init:
	docker compose up airflow-init

start:
	docker compose up -d

stop:
	docker compose down

destroy:
	docker compose donw -v

extend-airflow-image:
	docker build . --tag extending-airflow:latest

redeploy-airflow:
	docker compose up -d --no-deps --build airflow-webserver airflow-scheduler

run-minio:
	mkdir -p ~/minio/data

	docker run \
	   -p 9000:9000 \
	   -p 9001:9001 \
	   --name minio \
	   -v ~/minio/data:/data \
	   -e "MINIO_ROOT_USER=ROOTNAME" \
	   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
	   quay.io/minio/minio server /data --console-address ":9001"