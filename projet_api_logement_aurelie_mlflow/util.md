`mlflow --help`

# Commande pour lancer ML Flow
`mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000`

# Création d'une variable d'environnement pour préciser l'URL
`export MLFLOW_TRACKING_URI=http://localhost:5000`

# Il faut avoir créer le model dans l'UI de ML Flow
# création du endpoint du modèle
`mlflow models serve -m "models:/MyNewModel/Staging" -p 5001`
`mlflow models serve -m runs:/<RUN_ID>/model`

> By default mlflow run installs all dependencies using conda. To run a project without using conda, you can provide the `--no-conda` option to mlflow run. In this case, you must ensure that the necessary dependencies are already installed in your Python environment.

# Lancer ML FLow
`mlflow ui`

http://localhost:5000