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
 
 <ol>
  <li>
    Endpoint: <code>http://127.0.0.1:8000/predict</code> o <code>https://lab4-bi-uniandes.herokuapp.com/predict</code>
    <br>
    <strong>Funcionalidad:</strong> Calcular la predicción del modelo machine learning de regresión lineal.
    <strong>Operabilidad:</strong> Se envia un JSON con los predictores X de un registro de la base de datos para obtener la predicción realizada por el model de regresión lineal. El API retorna la predicción del modelo de regresión lineal
  </li>
  <li>Endpoint: <code>http://127.0.0.1:8000/r^2</code> o <code>https://lab4-bi-uniandes.herokuapp.com/r^2</code>
    <br>
    <strong>Funcionalidad:</strong> Calcular la metrica R^2 del modelo de regresión lineal.
    <strong>Operabilidad:</strong> Se envia un JSON con un conjunto de registros incluyendo predictores X y valores esperados Y. El API retorna la metrica R^2 del modelo de regresión lineal.
  </li>
 </ol>
 
