import streamlit as st
import pandas as pd
from PIL import Image
import sys
sys.path.append("C:\\Users\\User\\WORK\\workspace-ia\\PROJETS\\")
from projet_api_logement.api_logement_commons import do_prediction, get_img_path

st.set_page_config(
     layout="wide",
     page_title="Californie",
     page_icon = "🌴"
 )

labels = {
        'MedInc':['Revenu médian dans le secteur', '(en 10K $ dollars)'],
        'HouseAge':['Age médian des logements dans le secteur', 'ans'],
        'AveRooms':['Nombre moyen de pièces','pièces'],
        'AveBedrms':['Nombre moyen de chambres', 'chambres'],
        'Population':['Population dans le secteur','habitants'],
        'AveOccup':['Occupation moyenne des logements', 'habitants / logement'],
        'Latitude':['Latitude', '° degré'],
        'Longitude':['Longitude', '° degré'],
        }

default_values = {
        'MedInc':[9.87],
        'HouseAge':[150],
        'AveRooms':[7],
        'AveBedrms':[3],
        'Population':[1425],
        'AveOccup':[3],
        'Latitude':[35],
        'Longitude':[-119],
        }

st.title('Estimation du prix des logements en Californie')
col1, col2 = st.columns([1, 1])

img_path = get_img_path()+'illustration-california-color2.png'
image = Image.open(img_path)
col1.image(image, caption='California')

col2.subheader("Merci de renseigner les valeurs pour la prédiction")

for key, las in labels.items():
    step = 1.0
    if isinstance(default_values.get(key, [0])[0], int):
        step = 1
    # création dynamique des variables qui contiendront la valeur du champs
    vars()[key] = col2.number_input(las[0],value=default_values.get(key, [0])[0], step=step, format=None, key=key, help=las[1], on_change=None)

if col2.button("Prédire le prix moyen", key="button_submit", help='Cliquez sur le bouton pour estimer le prix du logement.'):
   # Lancement du traitement directement (sans passer par une API)
   pred = do_prediction(revenu_median=vars()['MedInc'], 
                    age_median=vars()['HouseAge'], 
                    nb_room_mean=vars()['AveRooms'], 
                    nb_bedroom_mean=vars()['AveBedrms'], 
                    population=vars()['Population'], 
                    occupation_mean=vars()['AveOccup'],
                    latitude=vars()['Latitude'], 
                    longitude=vars()['Longitude'])
   col1.title(f'Le prix du logement est estimé à {round(pred,2)} (en 10K $ dollars)' )

