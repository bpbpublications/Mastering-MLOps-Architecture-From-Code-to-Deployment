# Adding MLFlow client to the training code
# We will cover how to add MLflow client to the training code which will start tracking the changes. Let us assume we are using the LightGBM algorithm for our model:

# Other imports for the script
import mlflow
import mlflow.lightgbm

# Enable auto logging
mlflow.set_tracking_uri('http://yourdomain.com/mlflow')
mlflow.lightgbm.autolog()


# Load training data
mlflow.set_experiment('LightGBMClassifier')


def main():
    with mlflow.start_run() as run:
        # Train model
        
        # Let's log some custom parameter to the MLflow run
        mlflow.log_params({
            "model_name": "LGBMClassifier",
            "max_depth": 5
            })
        
        # Let's also log custom metrics which is outside the auto logging
        mlflow.log_metrics({
            key1: value1,
            key2: value2
            })
        
        print("Run ID:", run.info.run_id)


if __name__ == "__main__":
    main()