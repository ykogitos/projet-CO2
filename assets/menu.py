import streamlit as st

def menu():
    st.sidebar.title("Sommaire")
    st.sidebar.page_link("app.py", label="Présentation")
    if "page" in st.session_state and st.session_state.page == "Présentation":
        st.sidebar.markdown("""
        + [Présentation](#Présentation)
        + [Données](#Données)
        + [Contexte et périmètre](#Contexte)
        """, unsafe_allow_html=True)
    st.sidebar.page_link("pages/exploration.py", label="Exploration & Visualisation")
    if "page" in st.session_state and st.session_state.page == "Exploration":
        st.sidebar.markdown("""
        + [Analyse](#Analyse)
            + [Structure](#Structure)
            + [Valeurs nulles](#Nulles)
            + [Modalités](#Modalites)
            + [Variable cible](#Cible)
        + [Visualisation](#Correlation_cat)
            + [Corrélation catégorielle](#Correlation_cat)
            + [Corrélation quantitative](#Correlation_quant)
            + [Ewltp (Consommation)](#Emission)
            + [Ewltp (Ft)](#ewltp_ft)
            + [Répartition Ft](#rep_ft)
        + [Annexe](#Annexe)
        """, unsafe_allow_html=True)
    st.sidebar.page_link("pages/dataprocessing.py", label="Dataprocessing")
    if "page" in st.session_state and st.session_state.page == "Dataprocessing":
        st.sidebar.markdown("""
        + [Pré-processing](#Preprocessing)
        + [Feature engineering](#FeatureProcessing)
        + [Jeu de données final](#FinalDataset)
        """, unsafe_allow_html=True)
    st.sidebar.page_link("pages/modelisation.py", label="Modélisation")
    if "page" in st.session_state and st.session_state.page == "modelisation":
        st.sidebar.markdown("""
        + [Machine Learning](#ML)
            + [Recherche d'un modèle](#GridSearch)
            + [Entrainement et résultats](#MLTrain)
            + [Graphes Train](#MLGraphTrain)
            + [Graphes Test](#MLGraphTest)
            + [Poids du modèle](#MlWeights)
        + [Deep Learning](#DL)
            + [Présentation](#DNNPres)
            + [Entrainement et résultats](#DNNTrain)
            + [Graphes Train](#DNNGraphTrain)
            + [Graphes Test](#DNNGraphTest)
        + [Simulateur](#Prediction)
        """, unsafe_allow_html=True)
        