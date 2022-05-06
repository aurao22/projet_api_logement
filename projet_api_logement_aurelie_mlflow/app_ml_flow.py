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
        
        model_name = "california_logement_V0.2"
        
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
