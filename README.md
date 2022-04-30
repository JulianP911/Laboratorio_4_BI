# Laboratorio 4 - Inteligencia de Negocios

<h3>Desliegue de Modelos ML mediante uso de API's</h3>

<strong>Integrantes:</strong>
  <ul>
    <li>Julián Padilla Molina - 201913677</li>
    <li>Juan Andrés Ariza - 201911442</li>
    <li>Diego Felipe Carvajal - 201911910</li>
  </ul>
  

<strong>Objetivos:</strong>
  <ul>
    <li>Reforzar el conocimiento adquirido en la construcción de pipelines.</li>
    <li>Exportar un modelo de Machine Learning utilizando joblib.</li>
    <li>Construir un API para montar el modelo en producción y realizar predicciones mediante peticiones HTTP.</li>
  </ul> 

<strong>Instrucciones de instalación:</strong>
  <ol>
  <li>Clonar el proyecto en un carpeta de preferencia.</li>
  <li>Abrir Visual Studio Code en la carpeta donde quede almacenado el proyecto.</li>
  <li>Abrir la terminal en la dirección de proyecto e ingresar el comando <code>$ pip install -r requirements.txt
</code> para instalar las dependencias necesarias para la ejecución respectiva del proyecto.</li>
  </ol>
  
<strong>Despliegue del proyecto:</strong>
  <ul>
    <li>
      Deslpliegue local:
      <ol>
        <li>Abrir la terminal en la dirección del proyecto e ingresar el comando <code>uvicorn main:app --reload</code> para correr el servidor de forma local.</li>
      </ol>
    </li>
    <li>
      Despliegue remoto:
      <ol>
        <li>Abrir el navegador de preferencia y ingresar a la url <code>"https://lab4-bi-uniandes.herokuapp.com/"</code> donde se encuentra el proyecto en el servidor remoto.</li>
      </ol>
    </li>
  </ul>
 
 <strong>Funcionamiento del API:</strong>
 
 El diseño de la API consta principalmente de dos endpoints:
 
 <ul>
  <li>
    Endpoint: <code>http://127.0.0.1:8000/predict</code> o <code>https://lab4-bi-uniandes.herokuapp.com/predict</code>
    <br>
    <strong>Funcionalidad:</strong> Calcular la predicción del modelo machine learning de regresión lineal.
    <br>
    <strong>Operabilidad:</strong> Se envia un JSON con los predictores X de un registro de la base de datos para obtener la predicción realizada por el model de regresión lineal. El API retorna la predicción del modelo de regresión lineal.
    <br>
  </li>
</ul>
<ul>
  <li>Endpoint: <code>http://127.0.0.1:8000/r^2</code> o <code>https://lab4-bi-uniandes.herokuapp.com/r^2</code>
    <br>
    <strong>Funcionalidad:</strong> Calcular la metrica R^2 del modelo de regresión lineal.
    <br>
    <strong>Operabilidad:</strong> Se envia un JSON con un conjunto de registros incluyendo predictores X y valores esperados Y. El API retorna la metrica R^2 del modelo de regresión lineal.
    <br>  
  </li>
 </ul>
 
<strong>Ejemplo de funcionamiento:</strong>
<ul>
    <li><strong>Nota</strong>:Abrir la herramienta Postman para correr los test del endpoint 1 y
      2. (La colección de las pruebas se encuentra en la carpeta "collections").</li>
</ul>

<strong>Endpoint 1: Body Request</strong>
<ul>
  <li>A continuación, se presenta el JSON que se envía por medio del endpoint:</li>
</ul>

```json
{
  "data": [
      {
        "adult_mortality": 151.0,
        "infant_deaths": 0.0,
        "alcohol": 1.8,
        "percentage_expenditure": 423.2953509,
        "hepatitis_B": 9.0,
        "measles": 0,
        "bmi": 68.6,
        "under_five_deaths": 0.0,
        "polio": 91.0,
        "total_expenditure": 4.87,
        "diphtheria": 9.0,
        "hiv_aids": 0.1,
        "gdp": 2284.37858,
        "population": 146.0,
        "thinness_10_19_years": 0.1,
        "thinness_5_9_years": 0.1,
        "income_composition_of_resources": 693,
        "schooling": 14.6
      },
      {
        "adult_mortality": 153.0,
        "infant_deaths": 0,
        "alcohol": 1.79,
        "percentage_expenditure": 45.85105771,
        "hepatitis_B": 85.0,
        "measles": 0.0,
        "bmi": 67.8,
        "under_five_deaths": 0.0,
        "polio": 91.0,
        "total_expenditure": 5.9,
        "diphtheria": 9.0,
        "hiv_aids": 0.1,
        "gdp": 229.714718,
        "population": 99789.0,
        "thinness_10_19_years": 0.1,
        "thinness_5_9_years": 0.1,
        "income_composition_of_resources": 683,
        "schooling": 13.7
      }
   ]
}
```

<strong>Endpoint 1: Response</strong>
<ul>
  <li>A continuación, se presenta el JSON con la respuesta obtenida:</li>
</ul>

```json
{
    "predict": "[73.9653370635737, 72.34518413627389]"
}
```

<strong>Endpoint 2: Body Request</strong>
<ul>
  <li>A continuación, se presenta el JSON que se envía por medio del endpoint:</li>
</ul>

```json
{
  "data": {
    "data": [
      {
        "adult_mortality": 151.0,
        "infant_deaths": 0.0,
        "alcohol": 1.8,
        "percentage_expenditure": 423.2953509,
        "hepatitis_B": 9.0,
        "measles": 0,
        "bmi": 68.6,
        "under_five_deaths": 0.0,
        "polio": 91.0,
        "total_expenditure": 4.87,
        "diphtheria": 9.0,
        "hiv_aids": 0.1,
        "gdp": 2284.37858,
        "population": 146.0,
        "thinness_10_19_years": 0.1,
        "thinness_5_9_years": 0.1,
        "income_composition_of_resources": 693,
        "schooling": 14.6
      },
      {
        "adult_mortality": 153.0,
        "infant_deaths": 0,
        "alcohol": 1.79,
        "percentage_expenditure": 45.85105771,
        "hepatitis_B": 85.0,
        "measles": 0.0,
        "bmi": 67.8,
        "under_five_deaths": 0.0,
        "polio": 91.0,
        "total_expenditure": 5.9,
        "diphtheria": 9.0,
        "hiv_aids": 0.1,
        "gdp": 229.714718,
        "population": 99789.0,
        "thinness_10_19_years": 0.1,
        "thinness_5_9_years": 0.1,
        "income_composition_of_resources": 683,
        "schooling": 13.7
      }
    ]
  },
  "dataTrue": {
    "dataTrue": [
      {
        "life_expectancy": 73.96
      },
      {
        "life_expectancy": 72.34
      }
    ]
  }
}
```


<strong>Endpoint 2: Response</strong>
<ul>
  <li>A continuación, se presenta el JSON con la respuesta obtenida:</li>
</ul>

```json
{
    "r^2": 0.9999578116777199
}
```
