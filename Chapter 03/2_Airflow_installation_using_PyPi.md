## Airflow installation using PyPi

### Assuming we already have Python and Pip installed in the environment, installing Airflow becomes easier. Following is the command to install Airflow
```bash
pip install "apache-airflow[celery]==2.5.3" –constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.3/constraints-3.7.txt"

```


### Upon successfully installing Airflow, we can execute the following command:
The standalone command will initialize the database, make a user, and start all components for us.
```bash
airflow standalone

```

Once it is up and running, the terminal will display the login user and password we can use to login to the UI. Visit localhost:8000 in the browser and login with the provided credentials.