# Importar las librerías necesarias para ofrecer los requerimientos de negocio
import json
from plistlib import load
from typing import Optional
from typing_extensions import Self
from DataModel import DataModel, DataModelList, DataModelPredictVariable
from typing import FrozenSet
import pandas as pd
import numpy as np
from pandas import json_normalize
from sklearn.metrics import mean_squared_error
from joblib import load
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI

# Creación de la instancia de FastAPI
app = FastAPI()

# Endpoint inicial de la API
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint 1: Realizar predicciones con el modelo ML de regresión lineal
@app.post("/predict")
def make_predictions(data: DataModelList):
    df = convert_json_to_dataframe(data)
    df.columns = DataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    lists = result.tolist()
    json_predict = json.dumps(lists)
    return json_predict

# Endpoint 2: Determinar la métrica de mse del modelo ML de regresión lineal
@app.post("/mse")
def mse(data: DataModelList, dataModePredictVariable: DataModelPredictVariable):
    df = convert_json_to_dataframe(data)
    df.columns = DataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    dict = jsonable_encoder(dataModePredictVariable)
    y_true = dict["life_expectancy"]
    mse = mean_squared_error([y_true], result)
    result = np.sqrt(mse)
    return {"mse": mse}

# Función: Está se encarga de convertir los datos recibidos a través del JSON en un dataframe para que puedan ser usados en el modelo ML
def convert_json_to_dataframe(data):
    dict = jsonable_encoder(data)
    dataframe = json_normalize(dict['data']) 
    return dataframe