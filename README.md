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

## Dépendances     
`pip install -r requirements.txt`    

## Streamlit  
`cd  VOTRE_DOSSIER/streamlit`     
`streamlit run --client.showSidebarNavigation=False app.py`

# Organisation du projet

--------
    │
    ├── LICENSE
    ├── README.md  
    ├── app.py 
    ├── favicon.png  
    │ 
    ├── data 
    |   ├── processed
    |   |   ├── data_2022_all_features_cleaned_scaled.csv          
    |   |   ├── data_2022_cleaned_scaled.csv  
    |   │   └── data_2022_cleaned.csv             
    |   │
    |   └── raw
    |       ├── data_2022_light.csv          
    |       └── data_2022.csv    <- Not added [Link](https://co2cars.apps.eea.europa.eu/?source=%7B%22track_total_hits%22%3Atrue%2C%22query%22%3A%7B%22bool%22%3A%7B%22must%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22constant_score%22%3A%7B%22filter%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22year%22%3A2022%7D%7D%5D%7D%7D%2C%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22scStatus%22%3A%22Final%22%7D%7D%5D%7D%7D%5D%7D%7D%7D%7D%5D%7D%7D%2C%22filter%22%3A%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22MS%22%3A%22FR%22%7D%7D%5D%7D%7D%7D%7D%2C%22display_type%22%3A%22tabular%22%7D) 
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
    └── streamlit    
        │   
        ├── assets
        │   │ 
        │   ├── __init__.py
        │   ├── explore_ml.py
        │   ├── explore_raw_data.py
        │   ├── menu.py
        │   │
        │   ├── css
        │   │   │ 
        │   │   └── app.css
        │   │
        │   ├── csv
        │   │   │ 
        │   │   ├── processed 
        │   │   │   │ 
        │   │   │   ├── data_2022_all_features_cleaned_scaled.csv
        │   │   │   ├── data_2022_cleaned_scaled.csv
        │   │   │   └── data_2022_cleaned.csv
        │   │   │
        │   │   └── raw  
        │   │       │ 
        │   │       └── data_2022_light.csv                  
        │   │
        │   ├── custom_data
        │   │   │  
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
        │   │   │ 
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
        │       │ 
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

