import pandas as pd
from joblib import load
from os import getcwd,path

def do_prediction(revenu_median, age_median, nb_room_mean, nb_bedroom_mean, population, occupation_mean, latitude, longitude):
    
    # "MedInc	HouseAge	AveRooms	AveBedrms	Population	AveOccup	Latitude	Longitude"
    input_datas = {
        "MedInc":[revenu_median],
        "HouseAge":[age_median],
        "AveRooms":[nb_room_mean],
        "AveBedrms":[nb_bedroom_mean],
        "Population":[population],
        "AveOccup":[occupation_mean],
        "Latitude":[latitude],
        "Longitude":[longitude]
    }
    df_to_predict = pd.DataFrame(input_datas)

    model_path = _get_model_path()
    # Chargement du model
    model = load_model(model_path)
    predict_price = model.predict(df_to_predict)
    # Attention, c'est n numpy.ndarray qui est retourné
    print(f"Prédiction : {predict_price}")
    return predict_price[0]


def load_model(model_save_path):
    if path.exists(model_save_path) and path.isfile(model_save_path):
        # Chargement du modèle pré-entrainer
        return load(model_save_path)


def _get_model_path():
    # Récupère le répertoire du programme
    file_path = getcwd() + "\\"
    print(f"Current execution path : {file_path}")
    # C:\Users\User\WORK\workspace-ia\PROJETS\projet_api_logement\static\Forest_2022-05-05-10_29_03.joblib
    model_path = file_path
    if "PROJETS" not in model_path:
        model_path = model_path + r'PROJETS\projet_api_logement'
    elif "projet_api_logement" not in model_path:
        model_path = model_path + r'projet_api_logement'
    model_path = model_path + r'/Forest_2022-05-05-10_29_03.joblib'
    return model_path