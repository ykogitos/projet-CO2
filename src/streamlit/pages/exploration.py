import streamlit as st
from st_keyup import st_keyup
from assets.menu import menu
from assets.explore_raw_data import table_fields
import pandas as pd
# st.cache_data.clear()
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

if "page" in st.session_state:
    st.session_state["page"] = "Exploration"
    
menu()

st.title("Exploration du jeu de données")

# ANALYSE
st.header("Analyse", "Analyse")
st.write("""
La base de données de l’EEA contient toutes les données de tous les pays européens depuis
2010. 

Pour le projet, seules les données de l’année 2022 (qui sont les plus récentes) et
uniquement pour la France seront utilisées afin de limiter la taille du jeu de données (366Mb vs
2Gb).


Les données sont constituées via le protocole **WLTP** (**W**orldwide harmonized **L**ight vehicles
**T**est **P**rocedures) qui est la procédure d'essai mondiale harmonisée pour les véhicules légers.

Il est important de noter que depuis 2010, certaines colonnes ont été ajoutées et d’autres
abandonnées en raison de l’apparition de nouvelles spécifications ou de l'obsolescence de
certaines normes.
         """)
st.write("""
 **Champs inutilisées en 2022** (Voir l'[Annexe](#Annexe))
+ :red[MMS], :red[Enedc (g/km)], :red[Ernedc (g/km)], :red[Erwltp (g/km)], :red[De], :red[Vf]
         """)

# STRUCTURE
@st.cache_data
def get_df_head():
    return pd.read_csv("./assets/custom_data/df_raw_head_5.csv", index_col="ID")

st.header("Structure du jeu de données", "Structure")
st.write("### Aperçu des données")
st.dataframe(get_df_head(), use_container_width=True)

st.write("### Structure")
st.write("Le jeu de données brut contient **37 colonnes** et **1 638 878 lignes**, mais seuls les champs données en [annexe](#Annexe) sont utilisés pour l’année 2022")

@st.cache_data
def get_df_info():
    return pd.read_csv("./assets/custom_data/df_info_raw.csv", index_col="#")

st.dataframe(get_df_info(), use_container_width=True)

# VALEURS NULLES
st.header("Valeurs nulles", "Nulles")

@st.cache_data
def get_df_na():
    return pd.read_csv("./assets/custom_data/df_raw_na.csv", index_col=0)

st.dataframe(get_df_na(), use_container_width=True)
st.write("""
On remarque que certaines colonnes sont vides à 100%, ce qui correspond aux valeurs qui ne
sont plus utilisées pour le fichier 2022 (:red[MMS], :red[Ernedc (g/km)], :red[De] et :red[Vf])


Quant aux 2 colonnes :red[Enedc (g/km)] et :red[Erwltp (g/km)] pour lesquelles il manque 82% et 26%
des valeurs, cela correspond à des champs qui ne sont plus complétés depuis 2019.
[MS Guide 22 - Page 19](https://circabc.europa.eu/sd/a/d9cff59f-5117-48f4-9a37-07b94027110c/MS%20Guidelines%2022)         
         """)

# MODALITES
st.header("Modalités des variables catégorielles", "Modalites")

@st.cache_data
def get_df_modalite():
    return pd.read_csv("./assets/custom_data/df_raw_modalite.csv", index_col=0)

st.dataframe(get_df_modalite(), use_container_width=True)

# TARGET
st.header("Variable cible", "Cible")
st.write("La variable **Ewltp (g/km)** est définie comme étant la variable cible pour le projet.")

# CORRELATION VAR CAT
st.header("Corrélation des variables catégorielles", "Correlation_cat")
st.image("./assets/images/correlation_cat_raw_data.png")
st.write("""
    Variables fortement corrélées entre elles :      
    + Les variables **VFN**, **Mp**, **Mh**, **Man** qui représentent les différents noms des constructeurs
    + Les variables **Cr** et **Ct** qui correspondent à la catégorie du véhicule     
         """)

# CORRELATION VAR QUANTITATIVE
st.header("Corrélation des variables continues", "Correlation_quant")
st.image("./assets/images/correlation_quantitative_raw_data.png")
st.write("""
    Variables fortement corrélées à la variable cible **Ewltp (g/km)**: 
    + La variable **Fuel consumption** qui représentent la consommation du véhicule
    + Les variables **z** et **Electric range** qui correspondent respectivement à la consommation électrique et à l'autonomie     
         """)
st.write("""
    Variables fortement corrélées entre elles :
    + Les variables **m**, **Mt** qui représentent la masse et la masse normalisée Wltp
    + Les variables **At1**, **At2** qui représentent la largeur des essieux
    + Les variables **ec**, **ep** qui représentent la cylindrée et la puissance     
         """)

# EMISSION ET CONSOMMATION
st.header("CO2 en fonction de la consommation", "Emission")
st.image("./assets/images/emmission_consommation.png")

# EMISSION EN FONTION DU TYPE DE CARBURANT
st.header("Ewltp en fonction du type de carburant (Ft)", "ewltp_ft")
st.image("./assets/images/boxplot_ewltp_ft_raw_data.png")
st.write("Les valeurs extrêmes ne sont pas abérrantes, certains modèles sont des voitures puissantes")

# REPARTITION FUEL TYPE
st.header("Répartition des types de carburant", "rep_ft")
st.image("./assets/images/repartition_fuel_type.png")


# ANNEXE
st.header("Annexe", "Annexe")

if "field" not in st.session_state:
   st.session_state["field"] = "" 

fields = table_fields()

def custom_on_change():
    out=""
    index = 0
    search = ""
    
    if "field" in st.session_state:
        search = st.session_state.field
       
    for field in fields:
        if index > 2:
            if search != "":
                if field.find(search) != -1:
                    out += field + "\n"
            else:
                out += field + "\n"
        else:
            out += field + "\n"
        index += 1
        
    return out

# https://circabc.europa.eu/sd/a/d9cff59f-5117-48f4-9a37-07b94027110c/MS%20Guidelines%2022

value = st_keyup("Rechercher une variable", debounce=250, key="field")
st.markdown(custom_on_change(), unsafe_allow_html=True)

