
# mlflow
`mlflow --help`

## Commande pour lancer ML Flow
`mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000`
`mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0`

`mlflow.set_tracking_uri("http://localhost:5000")`
## Création d'une variable d'environnement pour préciser l'URL
`export MLFLOW_TRACKING_URI=http://localhost:5000`

## Il faut avoir créer le model dans l'UI de ML Flow
### création du endpoint du modèle
`mlflow models serve -m "models:/MyNewModel/Staging" -p 5001`
`mlflow models serve -m runs:/<RUN_ID>/model`

https://mlflow.org/docs/latest/models.html#deploy-mlflow-models
`mlflow models serve -m runs:/a348ee0c74ca4ca6b835670c6e1260e1/model -p 5678`

To serve a MLflow model using MLServer, you can use the --enable-mlserver flag, such as:
`mlflow models serve -m my_model --enable-mlserver`

Similarly, to build a Docker image built with MLServer you can use the --enable-mlserver flag, such as:
`mlflow models build -m my_model --enable-mlserver -n my-model`


`mlflow models serve -m "models:/california_logement_V0.1/Staging" -p 5001`

`mlflow models serve -m runs::/59a7ca66895246f6922ac502b9915bb2/linearRegressionCalifornie --port 1234`
`mlflow models serve -m runs::/59a7ca66895246f6922ac502b9915bb2/model --port 1234`

```
mlflow models --help
mlflow models serve --help
mlflow models predict --help
mlflow models build-docker --help
mlflow deployments help -t azureml
```

Exemple
```
$ mlflow models serve -m runs:/my-run-id/model-path &

$ curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{
    "columns": ["a", "b", "c"],
    "data": [[1, 2, 3], [4, 5, 6]]
}'
```



> By default mlflow run installs all dependencies using conda. To run a project without using conda, you can provide the `--no-conda` option to mlflow run. In this case, you must ensure that the necessary dependencies are already installed in your Python environment.

## Lancer ML FLow
Dans le répertoire qui contient le modèle
`mlflow ui`

http://localhost:5000

# streamlit 
`streamlit run myfile.py`

http://localhost:8501/
http://localhost:8502/
...

curl -d '{"columns":["x"], "data":[[1], [-1]]}' -H 'Content-Type: application/json; format=pandas-split' -X POST localhost:5000/invocations