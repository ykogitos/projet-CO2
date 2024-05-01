Projet: Émissions de CO2
==============================

## Résumé  
Estimation des émissions de CO2 des véhicules en France pour l'année 2022  
+ Extraction des données
+ Pré-processing et Feature engineering
+ Modèles de regression linéaire
    + Machine Learning avec Scikit-learn
    + Deep Learning avec Keras et Tensorflow

[Streamlit online](https://ykogitos-projet-co2-app-rbd3uy.streamlit.app/)     

[Raw Data](https://co2cars.apps.eea.europa.eu/?source=%7B%22track_total_hits%22%3Atrue%2C%22query%22%3A%7B%22bool%22%3A%7B%22must%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22constant_score%22%3A%7B%22filter%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22year%22%3A2022%7D%7D%5D%7D%7D%2C%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22scStatus%22%3A%22Provisional%22%7D%7D%5D%7D%7D%5D%7D%7D%7D%7D%5D%7D%7D%2C%22filter%22%3A%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22MS%22%3A%22FR%22%7D%7D%5D%7D%7D%7D%7D%2C%22display_type%22%3A%22tabular%22%7D)

## Installation
     
`mkdir VOTRE_DOSSIER`          
`cd  VOTRE_DOSSIER`              
`git clone https://github.com/ykogitos/projet-CO2.git .`      

## Dépendances     
`pip install -r requirements.txt`    

## Streamlit      
`streamlit run --client.showSidebarNavigation=False app.py`

