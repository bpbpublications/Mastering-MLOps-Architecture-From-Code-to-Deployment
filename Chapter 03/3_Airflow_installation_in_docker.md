## Airflow installation in Docker

### First of all, we will need to fetch the docker-compose file. 
We can either download the file using curl or manually by visiting Airflow documentation. The command to download the file is:
```bash
curl -Lf0 'https://airflow.apache.org/docs/apache-airflow/2.5.3/docker-compose.yaml'

```


### To run Airflow in Docker
Once we are ready to initialize airflow, we need to follow the commands below, this command first spins up the airflow-init docker container which sets up the prerequisites for airflow.
```bash
docker compose up airflow-init

```

Now once the init container is ready, it is time to spin up all other containers
```bash
docker compose up

```

The web server will be available on the development machine at http:localhost:8000. The default account has the login airflow and password airflow.