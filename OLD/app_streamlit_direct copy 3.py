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

st.title('Estimation du prix des logements en Californie')

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

df_default_values = pd.DataFrame(default_values)

img_path = get_img_path()+'illustration-california-color2.png'
image = Image.open(img_path)
st.image(image, caption='California')

st.text('Données par défaut tableau interactif')
st.dataframe(df_default_values, width=1500, height=1000)

# Surligne les valeurs maximales
# st.dataframe(df_default_values.style.highlight_max(axis=0))
st.text('Merci de renseigner les valeurs pour la prédiction')
for key, las in labels.items():
    step = 1.0
    if isinstance(default_values.get(key, [0])[0], int):
        step = 1
    # création dynamique des variables qui contiendront la valeur du champs
    vars()[key] = st.number_input(las[0],value=default_values.get(key, [0])[0], step=step, format=None, key=key, help=las[1], on_change=None)
    # st.text_input(labels[0], key=key, value=default_values.get(key, [0])[0])

for key in labels.keys():
    st.write(f'The current {key} is {vars()[key]}')

if st.button("Prédire le prix moyen", key="button_submit", help='Cliquez sur le bouton pour estimer le prix du logement.'):
   # TODO faire la prédiction avec l'API
   pred = do_prediction(revenu_median=vars()['MedInc'], 
                    age_median=vars()['HouseAge'], 
                    nb_room_mean=vars()['AveRooms'], 
                    nb_bedroom_mean=vars()['AveBedrms'], 
                    population=vars()['Population'], 
                    occupation_mean=vars()['AveOccup'],
                    latitude=vars()['Latitude'], 
                    longitude=vars()['Longitude'])
   st.title(f'Le prix du logement est estimé à {round(pred,2)} (en 10K $ dollars)' )

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)