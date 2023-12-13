from ml_performance_monitoring.monitor import wrap_model

metadata = {"environment": "aws", "dataset": "Example Dataset", "version": "1.0"}

features_columns, labels_columns = (LIST_OF_FETURES_COLUMNS, LABELS_COLUMN)

# This returns the instance of MLPerformanceMonitoring
ml_performance_monitor_model = wrap_model(
    insert_key=NEW_RELIC_KEY,
    model=MODEL_BEING_USED,
    model_name=NAME_OF_THE_MODEL,
    metadata=metadata,
    send_data_metrics=True,
    features_columns=features_columns,
    labels_columns="categorical"
)

# Calling the predict on the wrap function will run the predict function followed by automatically recording the inference data
Y_pred = ml_performance_monitor_model.predict(X=X_test,)

rmse = round(np.sqrt(mean_squared_error(y_test, y_pred)), 3)
metrics = {"RMSE": rmse,}

# Send the model metrics as a dictionary to NewRelic
ml_performance_monitor_model.record_metrics(metrics=metrics)