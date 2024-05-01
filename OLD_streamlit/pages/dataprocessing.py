import streamlit as st
import pandas as pd
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

if "page" in st.session_state:
    st.session_state["page"] = "Dataprocessing"
    
menu()
st.title("Préparation des données")

st.header("Pré-processing", "Preprocessing")
st.write("""
    À partir de l'exploration des données, les actions suivantes sont réalisées :
    + Suppression des variables obsoblètes (:red[MMS], :red[Enedc (g/km)], :red[Ernedc (g/km)], :red[Erwltp (g/km)], :red[De], :red[Vf])
    + Suppression des variables à cardinalité unique (**Country**, **Status**, **Year**, **r**)
    + Suppression de la variable corrélée à la cible **Fuel consumption**
    
    Pour les variables corrélées en elles :
    | Supprimée | Conservée |
    | ------- | ------ |
    | **m (kg)** | **Mt (kg)** |
    | **At2 (mm)** | **At1 (mm)** |
    | **ec** | **ep** |
    | **Ct** | **Cr** |
    | **z (Wh/km)** | **Electric range (km)** |

    Pour les variables n'ayant pas d'impact sur la variable cible (Test ANOVA) :
    + Suppressions des variables **VFN**, **Mp**, **Mh**, **Man**, **Tan**, **T**, **Va**, **Ve**, **IT**, **Mk**, **Cn**, **Date of registration**
    """, unsafe_allow_html=True)

st.write("### Suppression des lignes")
st.write("""
         Supression des lignes pour les véhicules à énergie électrique ou à hydrogène (pas d'émission CO2)\n
         En conséquence, il est inutile de garder la variable **Electric range (km)**\n
         Suppression des lignes duppliquées
         """)

st.write("### Valeurs nulles")
# @st.cache_data
def get_df_na():
    return pd.read_csv("./assets/custom_data/df_clean_1_2022_na.csv", index_col=0)

st.dataframe(get_df_na(), use_container_width=True)

st.header("Feature engineering", "FeatureProcessing")
st.write("""
         *Remarque* : Une PCA a été effectuée pour réduire le nombre de features mais 
         n'a pas donné de bons résultats concernant la part de variance 
         expliquée et a été abandonnée.
         """)
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("./assets/images/PCA.png")

st.write("""
        Le jeu de données est finalisé avec les dernières étapes suivantes :
        + Encodage des variables catégorielles (**Cr**, **Ft**, **Fm**)
        + Suppression des unités dans le nom des colonnes
        + Application d'un MinMaxScaler 
         """)

st.header("Jeu de données final", "FinalDataset")
st.write("""
        + Sauvegarde du dataframe
         """)
st.write("Au final, le dataset contient **16 colonnes** et **82 284 lignes**")
# @st.cache_data
def get_df_info():
    return pd.read_csv("./assets/custom_data/df_dummie_2022.csv", index_col="#")
st.dataframe(get_df_info(), use_container_width=True)
