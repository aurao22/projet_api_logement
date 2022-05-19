import mlflow
import mlflow.sklearn
import sys
sys.path.append("C:\\Users\\User\\WORK\\workspace-ia\\PROJETS\\")
from projet_api_logement.api_logement_commons import load_model, get_model_path

if __name__ == "__main__":
    model_path = get_model_path()
    print(f"Model path : {model_path}")
    # Chargement du model
    model = load_model(model_path)
    mlflow.sklearn.log_model(model, "Aurelie_Forest_Californie")
    print(mlflow.get_tracking_uri())
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)