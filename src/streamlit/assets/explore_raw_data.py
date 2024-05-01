import pandas as pd
import numpy as np
import streamlit as st
import io
from sklearn.preprocessing import MinMaxScaler
from pickle import dump
def create_info(df, filename):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    with open("./custom_data/" + filename, "w", encoding="utf-8") as f:  
        f.write(s)

def create_head_5(df, filename):
    df.head(5).to_csv("./custom_data/" + filename)

def create_df_info(filename_text, filename):
    with open("./custom_data/" + filename_text) as f:
        line = f.readline()
        i = 0
        df_info = {
            "#": [],
            "Column": [],
            "Non-Null": [],
            "Count": [],
            "Dtype": []
        }
        while line:
            i += 1
            if i > 5:
                splitline = line.split()
                l = len(splitline)
                if splitline[0].isdigit():
                    df_info["#"].append(splitline[0])
                    df_info["Column"].append(" ".join(splitline[1:(l - 3)]))
                    df_info["Count"].append(splitline[l - 3])
                    df_info["Non-Null"].append(splitline[l - 2])
                    df_info["Dtype"].append(splitline[l - 1])
            line = f.readline()
    df_info = pd.DataFrame(df_info)
    df_info.to_csv("./custom_data/" + filename, index=False)

def create_df_na(df, filename):
    df_na = pd.DataFrame(df.isna().sum()).reset_index()
    df_na.rename({0: "NA"}, inplace=True, axis=1)
    df_na["% NA"] = np.round((df_na["NA"]/ df.shape[0]) * 100, 2)
    df_na.to_csv("./custom_data/" + filename)

def create_df_modalite(df, filename):
    #cat = df[df.select_dtypes(include=["object"]).columns]
    df_na = pd.DataFrame(df.nunique()).reset_index()
    df_na.rename({0: "Count"}, inplace=True, axis=1)
    df_na.to_csv("./custom_data/" + filename)

def create_df_preprocessing_1(df, filename):
    df_preproc_1 = df.drop([
        "MMS", #
        "Enedc (g/km)", #
        "Ernedc (g/km)", #
        "Erwltp (g/km)", #
        "De", #
        "Vf", #
        "Country", #
        "Status", # 
        "year", #
        "r", #
        "m (kg)",
        "At2 (mm)",
        "ec (cm3)",
        "Ct",
        "z (Wh/km)",
        "Electric range (km)",
        "VFN", #
        "Mp", # 
        "Mh", #
        "Man", #
        "Tan", #
        "T", #
        "Va", #
        "Ve", #
        "IT", #
        "Mk", #
        "Cn", #
        "Fuel consumption ",
        "Date of registration" #
        ], axis=1)
    df_preproc_1 = df_preproc_1.drop(df[(df["Ft"] == "ELECTRIC") | (df["Ft"] == "HYDROGEN")].index)
    
    create_info(df_preproc_1, filename)
    create_df_na(df_preproc_1, "df_clean_1_2022_na.csv")
    
    # NA / DEDUPLICATE
    df_preproc_1.drop_duplicates(keep="first", inplace=True)
    df_preproc_1.dropna()
    create_info(df_preproc_1, "df_cleaned_2022.txt")
    create_df_info("df_cleaned_2022.txt", "df_cleaned_2022.csv")
    # DUMMIES
    df_preproc_1.replace(["PETROL/ELECTRIC", "DIESEL/ELECTRIC"], ["P_E", "D_E"], inplace=True)
    to_rename = ({
        "Ewltp (g/km)": "Ewltp",
        "W (mm)": "W",
        "At1 (mm)": "At1",
        "ep (KW)": "ep",
    })

    df_dummie = df_preproc_1.rename(columns=to_rename, errors="raise")
    df_dummie = pd.get_dummies(df_dummie, dtype=int, drop_first=True)
    df_dummie.drop_duplicates(keep="first", inplace=True)
    df_dummie.dropna()
    df_all = df_dummie
    create_info(df_dummie, "df_dummie_2022.txt")
    create_df_info("df_dummie_2022.txt", "df_dummie_2022.csv")
    cols = np.array(df_dummie.columns)
    cols_to_fit = np.delete(cols, np.where(cols == "Ewltp"))
    scaler = MinMaxScaler()
    df_dummie[cols_to_fit] = scaler.fit_transform(df_dummie[cols_to_fit])
    dump(scaler, open('scaler.pkl', 'wb'))
    create_head_5(df_dummie, "df_dummie_head_5.csv")
 
    # load the scaler
    # scaler = load(open('scaler.pkl', 'rb'))
    
def table_fields():
    table = """
    | Nom Variable          | Définition    | Exemple de valeur <br> :red[(Obsolète)]   |
    | ---------- | ------------ | ------------ |
    | **ID** <br> integer       | Numéro d\'identification unique des données contenues dans le registre national| - |
    | **Country** <br> varchar(2) | Pays | FR |                         
    | **VFN** <br> varchar(50) | Identifiant de la famille du véhicule <br> (Vehicle family identification number)| IP-DGY____EAT82552-VR3-0 |
    | **Mp** <br> varchar(50) | Pool du constructeur <br> (Manufacturer pooling) | STELLANTIS |
    | **Mh** <br> varchar(50) | Nom du constructeur au standard Européen <br> (Manufacturer name EU standard denomination) | PSA |
    | **Man** <br> varchar(50) | Déclaration **OEM** du nom du fabricant <br> (Manufacturer name OEM declaration) <br> **OEM**: Original Equipment Manufacturer | PSA AUTOMOBILES SA |
    | :red[**MMS** <br> varchar(125)] | :red[Nom du fabricant enregistré MS <br> (Manufacturer name MS registry denomination)] | :red[Remplacé par Man] |
    | **Tan** <br> varchar(50) | Numéro du type d’homologation <br> (Type approval number) | e9\*2018\/858\*11066\*03 |
    | **T** <br> varchar(25) | Type | N |
    | **Va** <br> varchar(25) | Variant | D |
    | **Ve** <br> varchar(35) | Version | DGYP-A1C000 |
    | **Mk** <br> varchar(25) | Marque <br> (Make) | CITROEN |
    | **Cn** <br> varchar(50) | Nom commercial <br> (Commercial name) | C5 X |
    | **Ct** <br> varchar(5) | Catégorie du type de véhicule immatriculé <br> (Category of the vehicle type approved) | M1 |
    | **Cr** <br> varchar(5) | Catégorie du véhicule immatriculé <br> (Category of the vehicle registered) | M1 |
    | **r** <br> integer | Total des nouvelles inscriptions <br> (Total new registrations) | 1 |
    | **m (kg)** <br> integer | Masse véhicule chargé <br> (Mass in running order Completed/complete vehicle) | 1797 |
    | **Mt (kg)** <br> integer | Masse harmonisée WLTP <br> (WLTP test mass) | 1888 |
    | :red[**Enedc (g/km)** <br> integer ] | :red[Réduction des émissions grâce à des technologies innovantes <br> (Emissions reduction through innovative technologies)] | :red[30.0 <br> (plus utilisé depuis 2019, remplacé par le Ewltp)] |
    | **Ewltp (g/km)** <br> integer | Les émissions spécifiques de CO2 (WLTP) <br> (Emissions reduction through innovative technologies (WLTP)) | 30 |
    | **W (mm)** <br> varchar(35) | Empattement <br> (Wheel Base) | 2785 |
    | **At1 (mm)** <br> integer | Largeur de l’essieu directeur <br> (Axle width steering axle) | 1600 |
    | **At2 (mm)** <br> integer | Largeur de l’essieu <br> (Axle width other axle) | 1605 |
    | **Ft** <br> varchar(25) | Type de carburant <br> (Fuel type) | PETROL/ELECTRIC |
    | **Fm** <br> varchar(1) | Mode de carburant <br> (Fuel mode) | P | 
    | **ec (cm3)** <br> integer | Cylindrée <br> (Engine capacity) | 1598.0 |
    | **ep (KW)** <br> integer | Puissance du moteur <br> (Engine power) | 132 |
    | **z (Wh/km)** <br> integer | Consommation électrique <br> (Electric energy consumption) | 159.0 |
    | **IT** <br> varchar(25) | Technologie innovante ou groupe de technologies innovantes <br> (Innovative technology or group of innovative technologies) | e2 28 29 |
    | :red[**Ernedc (g/km)** <br> float] | :red[Emissions spécifiques de CO2 <br> (Specific CO2 Emission) <br>**Deprecated value**, only relevant for data until 2016] | :red[NaN] |
    | :red[**Erwltp (g/km)** <br> float] | :red[Réduction d’émissions spécifiques de CO2 par l’utilisation de technologies spécifiques <br> (Emissions reduction through innovative technologies) <br>**Deprecated value**, only relevant for data until 2016] | :red[NaN] |
    | :red[**De**] | :red[-] | :red[NaN] |
    | :red[**Vf**] | :red[-] | :red[NaN] |
    | **Status** <br> varchar(1)| P: donnée provisoire, F: donnée définitive <br> (P = Provisional data, F = Final data) | P |
    | **Year** <br> integer | Année d’enregistrement <br> (Reporting year) | 2022 |
    | **Date of registration** | Date d’enregistrement | 2022-12-30 |
    | **Fuel consumption** <br> float | Consommation | 1.3 |
    | **Electric range (km)** | Autonomie électrique  | 59 |
    """   
    
    splitline = table.split("\n")
    return splitline
    
if __name__ == "__main__":
    # CREATE CUSTOM DATA
    df_raw = pd.read_csv(
        "./../../../data/raw/data_2022.csv",
        index_col="ID",
        low_memory=False)
    
    create_info(df_raw, "df_raw_2022_info.txt")
    create_head_5(df_raw, "df_raw_head_5.csv")
    create_df_info("df_raw_2022_info.txt", "df_info_raw.csv")
    create_df_na(df_raw, "df_raw_na.csv")
    create_df_modalite(df_raw, "df_raw_modalite.csv")
    create_df_preprocessing_1(df_raw, "df_clean_1_2022.txt")
    create_df_info("df_clean_1_2022.txt", "df_clean_1_2022.csv")