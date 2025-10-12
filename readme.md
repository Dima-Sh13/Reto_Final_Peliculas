# Aplicación de web api-flask con SQLite

Programa hecho en python con el framework flask y Sqlite

# Instalación
- crear un entorno en python y ejecutar el comando
```
pip install -r requirements.txt
```

la libreria utilizada en flask https://flask.palletsprojects.com/en/stable/installation/

# Ejecucion del programa por dotenv 
- Instalar dotenv
```
pip install python-dotenv
```
- crear el archivo .env y dentro agregar los siguientes parametros:
```
FLASK_APP=main.py
FLASK_DEBUG=True
```
- y luego ejecutar desde la terminal el comando:
```
flask run
```


# Otra Ejecucion del programa

-inicializar parametros para el servidor de flask

-en mac:
```
export FLASK_APP=main.py
```

-en windows:
```
set FLASK_APP=main.py
```

# comando para ejecutar el servidor
```
flask --app main run
```
# comando para ejecutar el servidor en otro puerto diferente del default que es siempre el 5000
```
flask --app main run -p 5002
```

# Base de datos
-La base da datos ya viene adjunta en el directorio data. Con ejemplos de prueba en las peliculas (up, harry potter, red, sweet novembre)
- en su defecto, crear una base de datos en sqlite y ejecutar el script de create.sql
- el path de la base de datos hay que pasarlo en config
```
ORIGIN_DATA="data/nombre.sqlite"
```

# Api

-Para poder usar la api debes añadir una api key valida en el fichero config.py en la variable API_KEY.
puedes conseguir una registrandote en : (https://www.omdbapi.com/)

-Al terminar. usa el comando flask run en tu consola y ve a la direccion : [text](http://127.0.0.1:5000) en tu navegador.
A veces puede tardar un poco en cargar.

# Uso

-Desde aqui puedes buscar una pelicula directamente por nombre o explorar las peliculas recientes de esta año en "/".

-Al poner solo el nopmbre de la pelicula te llevara a una vista detallada de esta, si solamente pones un año, te llevara a una vista de una seleccion de peliculas de ese año. usa ambos para buscar peliculas con mas precision.

-Desde la vista detallada se pueden leer los comentarios, una sinopsis y las caracteristicas principales de la pelicula, tambien puedes puntuar con estrellas.

-La vista muestra tanto el rating de Imdb como el de los usuarios de esta pagina.

-Disfruta!