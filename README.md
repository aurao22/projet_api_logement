# projet_api_logement_aurelie WITH ML FLOW

`mlflow --help`

# Version simple

## 1. En python
### 1.1. Créer le model en python, et le sauvegarder dans ML Flow 

Créer la signature :

```python
from mlflow.models.signature import infer_signature
signature = infer_signature(X_train, y_train)

```

### 1.2. Ajout du modèle dans ML Flow

```python
import mlflow.sklearn
nom_model = 'mlfow_model'
mlflow.sklearn.save_model(pipeline, nom_model, signature=signature)
print(f"mlflow models serve -m {nom_model}/") # avec conda
print(f"mlflow models serve -m {nom_model}/ --env-manager=local") # Sans conda
```

## 2. Lancer le serveur ML Flow

Se positionner dans le répertoire du projet

```python
# avec conda
print(f"mlflow models serve -m {nom_model}/") 
# Sans conda
print(f"mlflow models serve -m {nom_model}/ --env-manager=local") 
```

## 3. Lancer le serveur avec l'UI

Se positionner dans le répertoire du projet

```python
print('streamlit run myfile.py')
```

# ML Flow avec suivi des environnements et version de modèles
## 1. Création d'une variable d'environnement pour préciser l'URL
`export MLFLOW_TRACKING_URI=http://localhost:5000`
ou 
`mlflow.set_tracking_uri("http://localhost:5000")`

## 2. Commande pour lancer ML Flow
`mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000`
`mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0`


## 3. Lancer l'UI ML FLow
Dans le répertoire qui contient le modèle
`mlflow ui`
`mlflow ui --backend-store-uri sqlite:///mlflow.db`

Accéder à l'UI ML Flow :

http://localhost:5000/


## 4. Créer le model dans l'UI de ML Flow

Dans l'onglet `models` créer un model, ex: `mlfow_model`.

## 5. Register the modèle (en python)

```python
# Using the Tracking API
import warnings
import numpy as np
import mlflow
import mlflow.sklearn
import logging
import sys
sys.path.append("C:\\Users\\User\\WORK\\workspace-ia\\PROJETS\\")
from projet_api_logement.api_logement_commons import load_model, get_model_path
from urllib.parse import urlparse

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    with mlflow.start_run():
        model_path = get_model_path()
        print(f"Model path : {model_path}")
        # Chargement du model
        model = load_model(model_path)
        
        model_name = "mlfow_model"
        
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        print(mlflow.get_tracking_uri())
        
        # Model registry does not work with file store
        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(model, model_name, registered_model_name=model_name)
        else:
            mlflow.sklearn.log_model(model, model_name)

        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)

```

Dans une console :

```python
python app_ml_flow.py
```

`http://localhost:5000
Registered model 'mlfow_model' already exists. Creating a new version of this model...
2022/05/19 11:11:55 INFO mlflow.tracking._model_registry.client: Waiting up to 300 seconds for model version to finish creation.                     Model name: mlfow_model, version 1
Created version '1' of model 'mlfow_model'.Model saved in run 8b70b678645b4488ac0516bf5acee93c`


## X. Démarrer le modèle côté serveur

```python
# avec conda
print(f'mlflow models serve -m "models:/{nom_model}/Staging" -p 5001') 
# Sans conda
print(f'mlflow models serve -m "models:/{nom_model}/Staging" -p 5001 --env-manager=local') 
```

`mlflow models serve -m "models:/mlfow_model/Staging" --env-manager=local -p 5001 --env-manager=local`

Autres exemples :
`mlflow models serve -m "models:/MyNewModel/Staging" -p 5001`
`mlflow models serve -m "models:/mon_model_ui/Staging" -p 5001`
`mlflow models serve -m runs:/<RUN_ID>/model`
`mlflow models serve -m "models:/mlfow_model/Staging" -p 5001`

## 3. Lancer le serveur avec l'UI

Se positionner dans le répertoire du projet

```python
print('streamlit run myfile.py')
```


# Compléments

> By default mlflow run installs all dependencies using conda. To run a project without using conda, you can provide the `--env-manager=local` option to mlflow run. In this case, you must ensure that the necessary dependencies are already installed in your Python environment.

https://www.mlflow.org/docs/latest/quickstart.html



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




http://localhost:5000

# streamlit 
`streamlit run myfile.py`

http://localhost:8501/
http://localhost:8502/
...

curl -d '{"columns":["x"], "data":[[1], [-1]]}' -H 'Content-Type: application/json; format=pandas-split' -X POST localhost:5000/invocations