# -*- coding: utf-8 -*-
import pandas as pd
import json
from flask import Flask, render_template, jsonify, request, make_response
from api_logement_function import load_model
from os import getcwd

app = Flask(__name__)

NEWS_API_KEY = 'do_prediction'

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/predict/', methods=['GET'])
def predict():
    return render_template('predict.html')

@app.route('/predict/', methods=['POST'])
def do_prediction_via_record():
    
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

    # Attention, c'est n numpy.ndarray qui est retourné
    predict_price = do_prediction(revenu_median, age_median, nb_room_mean, nb_bedroom_mean, population, occupation_mean, latitude, longitude)
    msg=f"{predict_price[0]} 10 K$."
    dic ={'message':msg , 'data':predict_price[0], 'status':200}
    res = json.dumps(dic)
    print(res)
    # return res

    # response = make_response(render_template('predict.html', prediction=predict_price))
    # response.headers['prediction'] = predict_price
    # return response
    return render_template('resultat.html', prediction=predict_price)



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
    print(f"Prédiction : {predict_price}")
    return predict_price


if __name__ == "__main__":
    app.run(debug=True)