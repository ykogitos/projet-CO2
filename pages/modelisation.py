import streamlit as st
import pandas as pd
import numpy as np
from assets.menu import menu
from assets.explore_ml import load_ml_model, load_data, load_pickle, load_keras_model, Simulator
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes
import shap

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
    st.session_state["page"] = "modelisation"
    
model = load_ml_model("./assets/models/LinearRegression-V2.joblib")
keras_model = load_keras_model("./assets/models/DNN_regression.keras")
df = load_data("./assets/csv/processed/data_2022_all_features_cleaned_scaled.csv")
df_raw_light = load_data("./assets/csv/raw/data_2022_light.csv")
scaler = load_pickle("./assets/custom_data/scaler_all_data_2022.pkl")
    
menu()
st.title("Modélisation")

st.header("Machine Learning", "ML")

st.header("Recherche d'un modèle de régression", "GridSearch")
st.write("""
<div id="GridSearch">
Utilisation du GridSearchCV pour les modèles ci-dessous:

| Modèle | Score | Meilleurs paramètres |
| - | - | ----- |
| LinearSVR | 0.911968 | C=1, dual=auto, fit_intercept=True, loss=squared_epsilon_insensitive, max_iter=2000 |
| Ridge | 0.911957 | alpha=0.1, fit_intercept=True |
| **LinearRegression** | 0.911954 | fit_intercept=False |
| Lasso | 0.859463 | alpha=0.001, fit_intercept=False, max_iter=2000, selection=cyclic |
| Elastic_Net | 0.529188 | alpha=0.1, fit_intercept=True, l1_ratio=0.1, max_iter=2000 |

</div>
""", unsafe_allow_html=True)
st.write("")
st.write("""
\n         
Le modèle choisi est le  **LinearRegression** en raison de se rapidité et de son bon score         
         
         
*Remarque* : L'utilisation des modèles **RandomForestRegressor** et **SVR** n'a pas 
été possible en raison des limites mémoires des machines.
         """)

st.header("Entrainement et résultats", "MLTrain")
st.write("""
Le modèle est entrainé avec le jeu de données mis à l'échelle (MinMaxScaler)

Les scores R2 obtenus sont : 
| | Score R2|
| - | - |
| Train | 0.91134 |
| Test | 0.91195 |
         """)

st.header("Graphes Train", "MLGraphTrain")
st.image("./assets/images/LR_graphes_TRAIN.png")

st.header("Graphes Test", "MLGraphTest")
st.image("./assets/images/LR_graphes_TEST.png")

st.header("Poids du modèle", "MlWeights")
st.image("./assets/images/LR_weights.png")

st.header("Deep Learning", "DL")
st.header("Présentation du réseau de neurones", "DNNPres")

st.text("""
input_shape = (X_train.shape[1],)

model = Sequential()
model.add(Input(shape=input_shape))
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=2048, activation='relu'))
model.add(Dropout(rate=0.2))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(rate=0.2))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='linear'))

model.compile(loss='mae', optimizer='adam', metrics=['mse','mae']) 
        """)


st.write("""
**summary** 

<div id="DLSymmary">

| Layer (type) | Output Shape | Param # |
| -- | -- | --|
| dense_16 :blue[(Dense)] | (:blue[None], :green[16])  | :green[256] |
| dense_17 :blue[(Dense)] | (:blue[None], :green[128])  | :green[2,176] |
| dense_18 :blue[(Dense)] | (:blue[None], :green[2048])  | :green[264,192] |
| dropout_4 :blue[(Dropout)] | (:blue[None], :green[2048])  | :green[0] |
| dense_19 :blue[(Dense)] | (:blue[None], :green[256])  | :green[524,544] |
| dense_20 :blue[(Dense)] | (:blue[None], :green[256])  | :green[65,792] |
| dropout_5 :blue[(Dropout)] | (:blue[None], :green[256])  | :green[0] |
| dense_21 :blue[(Dense)] | (:blue[None], :green[128])  | :green[65,792] |
| dense_22 :blue[(Dense)] | (:blue[None], :green[128])  | :green[32,896] |
| dense_23 :blue[(Dense)] | (:blue[None], :green[1])  | :green[129] |

Total params: :green[2,867,333] (10.94 MB)  
Trainable params: :green[955,777] (3.65 MB)  
Non-trainable params: :green[0] (0.00 B)  
Optimizer params: :green[1,911,556] (7.29 MB)  

</div>
         """, unsafe_allow_html=True)

st.header("Entrainement", "DNNTrain")
st.write("""
    Le modèle est entrainé avec **200** epochs par batch de **30** avec le même jeu de données utilisé lors du machine learning 
    avec deux callbacks pour arrêter un epoch si nécessaire :  
    + **early_stopping** qui consiste à stopper l'étape d'entraînement dès que le loss de validation atteint un plateau ou commence à augmenter  
    + **lr_plateau**  qui consiste à modifier le learning rate quand il n'y a plus d'amélioration 
         """)

st.text("""
    history = model.fit(
        X_train, 
        y_train, 
        epochs=200, 
        batch_size=30, 
        validation_split=0.2, 
        callbacks=[early_stopping, lr_plateau])    
        """)


# st.image("./assets/images/history_loss.png")

st.write("""
Les scores R2 obtenus sont :  
| | Score R2|
| - | - |
| Train | 0.98764 |
| Test | 0.98820 |
         """)

st.header("Graphes Train", "DNNGraphTrain")
st.image("./assets/images/DNN_graphes_TRAIN.png")

st.header("Graphes Test", "DNNGraphTest")
st.image("./assets/images/DNN_graphes_TEST.png")
st.write("")
st.write("")
st.write("")

st.header("Simulateur", "Prediction")
simulator = Simulator(df, df_raw_light, model, keras_model, scaler)

with st.form("ml_form"):
    slider_val = st.slider("Nombre", min_value=1, max_value=10, value=5)
    with st.expander("Filtres"):
        st.write("Énergie ")
        Ft_PETROL = st.checkbox("Essence")
        Ft_DIESEL = st.checkbox("Diesel")
        Ft_PETROL_ELECTRIC = st.checkbox("Hybride Essence/Électrique")
        Ft_DIESEL_ELECTRIC = st.checkbox("Hybride Diesel/Électrique")
        Ft_E85 = st.checkbox("Superéthanol-E85")
        Ft_LPG = st.checkbox("gaz de pétrole liquéfié (GPL)")
        Ft_NG = st.checkbox("Gaz naturel (NG)")

    submitted = st.form_submit_button("Simuler")

    if submitted:
        has_filter = Ft_PETROL or Ft_DIESEL or Ft_PETROL_ELECTRIC or Ft_DIESEL_ELECTRIC or Ft_E85 or Ft_LPG or Ft_NG
        cbs = []
        
        if Ft_PETROL:
            cbs.append("PETROL")
            
        if Ft_DIESEL:
            cbs.append("DIESEL")
            
        if Ft_PETROL_ELECTRIC:
            cbs.append("PETROL/ELECTRIC")
            
        if Ft_DIESEL_ELECTRIC:
            cbs.append("DIESEL/ELECTRIC")    

        if Ft_E85:
            cbs.append("E85")
            
        if Ft_LPG:
            cbs.append("LPG")

        if Ft_NG:
            cbs.append("NG")


        simulation, df_sample = simulator.make_simulation(slider_val, has_filter, cbs)

        st.dataframe(simulation)
        makes = simulation["Modèle"]
        metrics = {
            "DNN": simulation["DNN"],
            "EWLTP": simulation["EWLTP"],
            "LR": simulation["LR"],
        }
        x = np.arange(len(makes))
        bar_colors = {
            "DNN": (30/255, 136/255, 229/255, 1),
            "EWLTP": (1, 13/255, 87/255, 1),
            "LR": (30/255, 136/255, 229/255, 0.5)
        }
        width = 0.15
        multiplier = 0
        fig, ax = plt.subplots(layout="constrained")
        ymin = []
        ymax = []
        for attribute, measurement in metrics.items():
            offset = width * multiplier
            rects = ax.bar(
                x + offset, 
                measurement, 
                width, 
                label=attribute, 
                color=bar_colors[attribute])
            ymin.append(min(measurement))
            ymax.append(max(measurement))
            ax.bar_label(rects, padding=3, rotation=90, fontsize=8)
            multiplier += 1.04
            
        plt.xticks(rotation=90, fontsize=8)
        plt.yticks(fontsize=8)
        ax.set(ylim=(min(ymin) - 20, max(ymax) + 40))
        ax.legend(loc='upper right', ncols=3, fontsize=8)
        ax.set_xticks(x + width, makes)
        st.pyplot(fig)
        
        # Explain
        st.write("## Explication des prédictions pour le DNN ")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        df_sample_no_Ewltp = df_sample.drop(["Ewltp"], axis=1)
        for n in range(slider_val):
            explainer, shap_values, df_shap = simulator.explain_prediction(df_sample.iloc[[n]])
            st.write("#### "+ simulation["Groupe"].iloc[n] + " - " + simulation["Modèle"].iloc[n])
            dnn = str(round(simulation["DNN"].iloc[n], 2))
            ewltp = str(round(simulation["EWLTP"].iloc[n], 2))
            resume = "Émission de CO2 -   "
            resume += " Prédiction : <b>" + dnn + "</b> "
            resume += "| Réelle : <b>" + ewltp + "</b>"
            resume += "<br>Énergie (Ft): <b>" + simulation["Énergie"].iloc[n] + "</b>"
            resume += " | " + "Cylindrée (ec) : <b>" + str(simulation["Cylindrée"].iloc[n]) + "</b>"
            resume += " | " + "Puissance (ep) : <b>" + str(simulation["Puissance"].iloc[n]) + "</b>"
            resume += " | " + "Masse (Mt) : <b>" + str(simulation["Masse WLTP"].iloc[n]) + "</b>"      
            st.write('<span style="font-size: 0.8rem;">' + resume + '</span>', unsafe_allow_html=True)
            plt.clf()
            st.pyplot(shap.force_plot(
                explainer.expected_value, 
                shap_values, 
                df_sample_no_Ewltp.iloc[n, :],
                matplotlib=True))
            plt.show()
            plt.close()

            fig, ax = plt.subplots(layout="constrained", figsize=(10, 2.5))

            colorsValue = []
            color_positive = (1, 13/255, 87/255, 1)
            color_negative = (30/255, 136/255, 229/255, 1)
            white = (1, 1, 1, 0)

            for i, value in enumerate(df_shap["Coefs"]):
                
                if i > 1:
                    if value < 0:
                        colorsValue.append(color_negative)
                    else:
                        colorsValue.append(color_positive)
                else:
                    colorsValue.append(white)
       
            p = ax.barh(
                data=df_shap, 
                width="Coefs", 
                y="Features", 
                height=0.2,
                color=colorsValue)
            
            
            ax.bar_label(p, labels=df_shap["Features"], padding=10, fontsize=8, rotation=0)
            ax.set_axis_off()
            plt.title("Part des features")
            st.pyplot(fig)
            
i=0
while i < 20:
    st.write("  \n")
    i += 1

