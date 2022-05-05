# -*- coding: utf-8 -*-
import pandas as pd
from api_logement_function import load_model
from os import getcwd
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('home.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    record = request.form
    print(record)

    revenu_median=record.get('revenu_median', 0)
    age_median=record.get('age_median', 0)
    nb_room_mean=record.get('nb_room_mean', 0)
    nb_bedroom_mean=record.get('nb_bedroom_mean', 0)
    population=record.get('population', 0)
    occupation_mean=record.get('occupation_mean', 0)
    latitude=record.get('latitude', 0)
    longitude=record.get('longitude', 0)

    print(revenu_median, age_median, nb_room_mean, nb_bedroom_mean, population, occupation_mean, latitude, longitude)

    predict_price = do_prediction(revenu_median, age_median, nb_room_mean, nb_bedroom_mean, population, occupation_mean, latitude, longitude)
    print(predict_price)

    return render_template('greeting.html', say=round(predict_price,2), to=predict_price,revenu_median=revenu_median, 
                        age_median=age_median, nb_room_mean=nb_room_mean, 
                        nb_bedroom_mean=nb_bedroom_mean, population=population, 
                        occupation_mean=occupation_mean, 
                        latitude=latitude, longitude=longitude)


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
    
    # Récupère le répertoire du programme
    file_path = getcwd() + "\\"
    print(f"Current execution path : {file_path}")
    # C:\Users\User\WORK\workspace-ia\PROJETS\projet_api_logement\static\Forest_2022-05-05-10_29_03.joblib
    model_path = file_path
    if "PROJETS" not in model_path:
        model_path = model_path + r'PROJETS\projet_api_logement'
    elif "projet_api_logement" not in model_path:
        model_path = model_path + r'projet_api_logement'
    model_path = model_path + r'/static/Forest_2022-05-05-10_29_03.joblib'
    # Chargement du model
    model = load_model(model_path)
    predict_price = model.predict(df_to_predict)
    # Attention, c'est n numpy.ndarray qui est retourné
    print(f"Prédiction : {predict_price}")
    return predict_price[0]


if __name__ == "__main__":
    app.run()