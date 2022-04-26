# Importar las librerías necesarias para ofrecer los requerimientos de negocio
import json
from plistlib import load
from typing import Optional
from typing_extensions import Self
from DataModel import DataModel, DataModelList, DataModelPredictVariableList
from typing import FrozenSet
import pandas as pd
import numpy as np
from pandas import json_normalize
from sklearn.metrics import r2_score, mean_squared_error
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

# Endpoint 2: Determinar la métrica de r^2 del modelo ML de regresión lineal
@app.post("/r2")
def r2(data: DataModelList, dataTrue: DataModelPredictVariableList):
    df = convert_json_to_dataframe(data)
    df.columns = DataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    dict = jsonable_encoder(dataTrue)
    y_true = []
    for i in dict["dataTrue"]:
        y_true.append(float(i["life_expectancy"]))
    r2 = r2_score(y_true, result.tolist())
    return {"r^2": r2}

# Función: Está se encarga de convertir los datos recibidos a través del JSON en un dataframe para que puedan ser usados en el modelo ML
def convert_json_to_dataframe(data):
    dict = jsonable_encoder(data)
    dataframe = json_normalize(dict['data']) 
    return dataframe