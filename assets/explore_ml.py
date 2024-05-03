import pandas as pd
import numpy as np
import pickle
from joblib import dump, load
from keras.models import load_model
import keras
import shap

shap.initjs()

pd.options.mode.copy_on_write = True
keras.backend.clear_session()

def load_data(filename):
    return pd.read_csv(filename, index_col="ID", low_memory=False)

def get_random_rows(df, num):
    a = np.arange(0, df.shape[0], 1)
    random_row = np.random.choice(a,  num)
    return random_row

def load_pickle(filename):
    file = open(filename, "rb")
    data = pickle.load(file)
    file.close()
    return data

def load_ml_model(model_name):
    return load(model_name)

def load_keras_model(model_name):
    return load_model(model_name)

def create_df_raw(df):
    df_raw = load_data("./../../../data/raw/data_2022.csv")
    df_raw_indexed_by_df = df_raw.loc[df.index]

    df_raw_indexed_by_df = df_raw_indexed_by_df[["Mp", "Mk", "Ct", "Cn", "Mt", "Ft", "ec (cm3)", "ep (KW)", "Fuel consumption "]]
    df_raw_indexed_by_df.to_csv("./../../../data/raw/data_2022_light.csv")
    
class Simulator():
    def __init__(self, df, df_raw_light, model, keras_model, scaler):
        self.df = df
        self.df_no_ewltp = df.drop(["Ewltp"], axis=1)
        self.df_raw_light = df_raw_light
        self.model = model
        self.scaler = scaler
        self.keras_model = keras_model
        
    def shap_f(self, X):
        return self.keras_model.predict(X).flatten()
        
    def explain_prediction(self, df_sample):
        X = df_sample.copy()
        X = X.drop(["Ewltp"], axis=1)
        explainer = shap.KernelExplainer(self.shap_f, self.df_no_ewltp.iloc[:40, :])
        shap_values = explainer.shap_values(X, nsamples=500)
        
        df_shap = pd.DataFrame({
            "Features": X.columns.ravel(),
            "Coefs": shap_values.ravel()
        })
        
        v_max = df_shap["Coefs"].max()
        v_min = df_shap["Coefs"].min()
        
        df_shap = df_shap.set_index("Features")
        df_shap = df_shap[df_shap.Coefs != 0.0]
        df_shap = df_shap.reset_index()
        df_shap["Abs"] = abs(df_shap["Coefs"])
        df_shap = df_shap.sort_values(by="Abs", ascending=True)
        
        row = {
            "Features": ["", ""],
            "Coefs": [max(v_max, abs(v_min)), max(v_max, abs(v_min)) * (-1)]
        }
        df_shap = pd.concat([pd.DataFrame(row), df_shap])
        return explainer, shap_values, df_shap
        
    def get_rescaled(self, df, model_name="", y=False):
        if y:
            if model_name == "lr":
                X = df.copy()
                X = X.drop(["Ewltp"], axis=1)
                y_pred = self.model.predict(X)
                X.insert(1, "Ewltp", y_pred)
                X[X.columns] = self.scaler.inverse_transform(X[X.columns])
                return X["Ewltp"]
            elif model_name == "dnn":
                X_DNN = df.copy()
                X_DNN = X_DNN.drop(["Ewltp"], axis=1)
                y_pred_dnn = self.keras_model.predict(X_DNN)
                X_DNN.insert(1, "Ewltp", y_pred_dnn)
                X_DNN[X_DNN.columns] = self.scaler.inverse_transform(X_DNN[X_DNN.columns])
                return X_DNN["Ewltp"]
            else:
                return

        else:
            X = df.copy()
            X[X.columns] = self.scaler.inverse_transform(X[X.columns])
            return X
 
    def make_simulation(self, num, has_filter, cbs):
        df = self.df_raw_light

        if has_filter:
            df = df.loc[df["Ft"].isin(cbs)]
        
        df_raw_light = df.iloc[get_random_rows(df, num)]
        df_sample = self.df.loc[df_raw_light.index]
        df_sample_copy = df_sample.copy()
        df_sample_rescaled = self.get_rescaled(df_sample_copy)
        y_ml_pred = self.get_rescaled(df_sample_copy, model_name="lr", y=True)
        y_dl_pred = self.get_rescaled(df_sample_copy, model_name="dnn", y=True)
 
        simulation = pd.DataFrame({
            "DNN": y_dl_pred.round(2),
            "EWLTP": df_sample_rescaled["Ewltp"],
            "LR": y_ml_pred.round(2),
            "Groupe": df_raw_light["Mk"],
            "Modèle": df_raw_light["Cn"],
            "Énergie": df_raw_light["Ft"],
            "Cylindrée": df_raw_light["ec (cm3)"],
            "Puissance": df_raw_light["ep (KW)"],
            "Consommation": df_raw_light["Fuel consumption "],
            "Masse WLTP": df_raw_light["Mt"],
        })
        
        return simulation, df_sample_copy
     
if __name__ == "__main__":
    pass
