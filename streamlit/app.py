import streamlit as st
from assets.menu import menu

st.set_page_config(
        page_title="Emission de CO2",
        page_icon="favicon.png",
    )

@st.cache_data
def load_css(file_name = "./assets/css/app.css"):
    with open(file_name) as f:
        css = f'<style>{f.read()}</style>'
    return css

css = load_css()
st.markdown(css, unsafe_allow_html=True)



if "page" not in st.session_state:
    st.session_state["page"] = ""

if "page" in st.session_state:
    st.session_state["page"] = "Présentation"

menu()   
st.title("Émissions de CO2")

# PRESENTATION
st.header("Présentation", "Présentation")   
st.write("+ Identifier les véhicules qui émettent le plus de CO2 pour déterminer les caractéristiques techniques qui jouent un rôle important dans les émisssions de CO2")
st.write("+ Prédire à l’avance cette émission pour les nouveaux véhicules")

# DONNEE
st.header("Données", "Données")
st.write("Pour ce projet, deux liens étaient proposés pour choisir le jeu de données.")
st.image("./assets/images/ADEME.png", width=300)
st.write("""
Depuis le site de l’[ADEME](https://www.ademe.fr/) :
[emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_)  
         """)
st.write(" ")
st.image("./assets/images/european_environnement_agency.png", width=300)
st.write("""
  Depuis le site de l'[European Environment Agency](https://www.eea.europa.eu/en) (EEA) : 
[co2-cars-emission-2022](https://co2cars.apps.eea.europa.eu/?source=%7B%22track_total_hits%22%3Atrue%2C%22query%22%3A%7B%22bool%22%3A%7B%22must%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22constant_score%22%3A%7B%22filter%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22year%22%3A2022%7D%7D%5D%7D%7D%2C%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22scStatus%22%3A%22Final%22%7D%7D%5D%7D%7D%5D%7D%7D%7D%7D%5D%7D%7D%2C%22filter%22%3A%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22MS%22%3A%22FR%22%7D%7D%5D%7D%7D%7D%7D%2C%22display_type%22%3A%22tabular%22%7D)   
         """)
st.write(" ")
st.write("**Le jeu de donnée provenant de l’EEA est choisi car plus récent et complet.**")

# CONTEXTE
st.header("Contexte et périmètre", "Contexte")
st.write("""
Le règlement (UE) n° 2019/631 impose aux pays d'enregistrer des informations pour chaque
nouvelle voiture particulière immatriculée sur leur territoire. Chaque année, chaque État
membre soumet à la Commission toutes les informations relatives à ses nouvelles
immatriculations.
Les objectifs d'émissions de CO2 pour l'ensemble du parc automobile de l'UE fixés dans le
règlement sont les suivants :
         """)

# https://climate.ec.europa.eu/eu-action/transport/road-transport-reducing-co2-emissions-vehicles/co2-emission-performance-standards-cars-and-vans_en?prefLang=fr

st.write("""
**2020 à 2024**
+ Voitures : 95 g CO2/km
+ Camionnettes : 147 g CO2/km      
         """)
st.write("""
**2025 à 2029**
+ Voitures : 93,6 g CO2/km
+ Camionnettes : 153,9 g CO2/km      
         """)
st.write("""
**2030 à 2034**
+ Voitures : 49,5 g CO2/km
+ Camionnettes : 90,6 g CO2/km      
         """)
st.write("""
À partir de **2035**, l'objectif de réduction des émissions de CO2 pour l'ensemble du parc
automobile de l'UE, qu'il s'agisse de voitures ou de camionnettes, est de 100 %, soit **0 g de
CO2/km**.     
         """)

