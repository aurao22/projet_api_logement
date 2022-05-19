# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:46:11 2022

@author: utilisateur
"""
#Importation des librairies
from joblib import dump, load
import streamlit as st
from sklearn.linear_model import ElasticNet
import pandas as pd
import requests


#importation du modèle
reg_loaded = load('regression.joblib')


st.title("Prix des logements en californie")
with st.form("my_form"):
    MedInc=st.number_input(label='Median income')
    HouseAge=st.number_input(label='House Age')
    AveRooms=st.number_input(label='Average Rooms')
    AveBedrms=st.number_input(label='Average Bedrooms')
    Population=st.number_input(label='Population')
    AveOccup=st.number_input(label='Average Occupation')
    Latitude=st.number_input(label='Latitude')
    Longitude=st.number_input(label='Longitude')
    submitted = st.form_submit_button("Submit")
    if submitted:
        col=["MedInc", "HouseAge" ,"AveRooms","AveBedrms","Population" ,"AveOccup" ,"Latitude","Longitude"]
        X_te=pd.DataFrame([(MedInc, HouseAge ,AveRooms,AveBedrms,Population ,AveOccup ,Latitude,Longitude)], columns=col )
        st.write("Avec les valeurs suivantes :",X_te)
        
        #st.write("La prédiction :",reg_loaded.predict(X_te)[0])

        url = 'http://localhost:1234/invocations'
        data = {"MedInc": MedInc , "HouseAge" : HouseAge , "AveRooms" : AveRooms,"AveBedrms" : AveBedrms,"Population" : Population ,"AveOccup" : AveOccup ,"Latitude" : Latitude,"Longitude" : Longitude}
        headers = {'Content-Type': 'application/json',}
        http_data = X_te.to_json(orient='split')
        response = requests.post(url,headers=headers, data=http_data)

        st.write("La prédiction :", response.json())



