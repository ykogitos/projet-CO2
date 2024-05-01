Projet: Émissions de CO2
==============================

## Résumé  
Estimation des émissions de CO2 des véhicules en France pour l'année 2022  
+ Extraction des données
+ Pré-processing et Feature engineering
+ Modèles de regression linéaire
    + Machine Learning avec Scikit-learn
    + Deep Learning avec Keras

## Installation
     
`mkdir VOTRE_DOSSIER`          
`cd  VOTRE_DOSSIER`              
`git clone https://github.com/ykogitos/projet-CO2.git .`      

Ajouter l'environnement avec **Conda**     
`conda env create -f environment.yml`    


## Streamlit

`cd ./src/streamlit`   
`streamlit run --client.showSidebarNavigation=False app.py`

# Organisation du projet

--------
VOTRE_DOSSIER
    │
    ├── LICENSE
    │
    ├── README.md          
    │
    ├── notebooks 
    │   ├── 01-exploration_data.ipynb        
    │   ├── 02-Preprocessing.ipynb        
    │   ├── 03-Machine_learning_regression.ipynb   
    │   └── 04-Deep_learning_DNN.ipynb     
    │
    ├── reports 
    │   ├── Rendu_1_Projet_FEV_2024_CO2.pdf
    │   ├── Rendu_2_Projet_FEV_2024_CO2.pdf
    │   └── Rendu_final.pdf 
    │
    ├── requirements.txt
    │
    └─── src
        └── streamlit
            ├── app.py 
            ├── favicon.png    
            │    
            ├── assets
            │   ├── __init__.py
            │   ├── explore_ml.py
            │   ├── explore_raw_data.py
            │   ├── menu.py
            │   │
            │   ├── css
            │   │   └── app.css
            │   │
            │   ├── csv
            │   │   ├──  processed 
            │   │   │    ├── data_2022_all_features_cleaned_scaled.csv
            │   │   │    ├── data_2022_cleaned_scaled.csv
            │   │   │    └── data_2022_cleaned.csv
            │   │   │
            │   │   └── raw  
            │   │       └── data_2022_light.csv                  
            │   │
            │   ├── custom_data
            │   │   ├── df_clean_1_2022_na.csv
            │   │   ├── df_clean_1_2022.csv
            │   │   ├── df_cleaned_2022.csv
            │   │   ├── df_dummie_2022.csv
            │   │   ├── df_dummie_head_5.csv
            │   │   ├── df_info_raw.csv
            │   │   ├── df_raw_head_5.csv
            │   │   ├── df_dummie_2022.csv
            │   │   ├── df_raw_modalite.csv
            │   │   ├── df_raw_na.csv
            │   │   ├── df_clean_1_2022.txt
            │   │   ├── df_cleaned_2022.txt
            │   │   ├── df_dummie_2022.txt
            │   │   ├── df_raw_2022_info.txt
            │   │   ├── scaler_all_data_2022.pkl
            │   │   └── scaler.pkl
            │   │
            │   ├── images
            │   │   ├── ADEME.png
            │   │   ├── boxplot_ewltp_ft_raw_data.png
            │   │   ├── correlation_cat_raw_data.png
            │   │   ├── correlation_quantitative_raw_data.png
            │   │   ├── DNN_graphes_TEST.png
            │   │   ├── DNN_graphes_TRAIN.png
            │   │   ├── emmission_consommation.png
            │   │   ├── european_environnement_agency.png
            │   │   ├── history_loss.png
            │   │   ├── LR_graphes_TEST.png
            │   │   ├── LR_graphes_TRAIN.png
            │   │   ├── LR_weights.png
            │   │   ├── PCA.png
            │   │   └── repartition_fuel_type.png
            │   │ 
            │   └── models
            │       ├── DNN_regression.keras
            │       ├── LinearRegression-V2.joblib
            │       └── scaler_data_2022.pkl
            │
            └── pages
                ├── __init__.py
                ├── dataprocessing.py
                ├── exploration.py
                └── modelisation.py
--------

