# Movies API

Este proyecto utiliza Django REST Framework y PostgreSQL para proporcionar una API para administrar películas.

El repositorio tiene dos ramas:

- **main**: Contiene la implementación de los endpoints mencionados en la sección 1 del requerimiento.
- **seccion2**: Contiene la implementación adicional para la sección 2 del requerimiento, que incluye un servicio para devolver un GeoJSON con los puntos geográficos de los países de las películas en la base de datos.

## Endpoints

- **Welcome**: 
  - Ruta: /
  - Método: GET
  - Descripción: Saludo de bienvenida a la API.

- **Obtener todas las películas**: 
  - Ruta: /movies/
  - Método: GET
  - Descripción: Obtiene todas las películas con la capacidad de filtrar por título, rating y país. También admite paginación y ordenamiento.

- **Buscar películas**: 
  - Ruta: /search/
  - Método: GET
  - Descripción: Busca películas por título, rating, país o ID.

- **Obtener película por ID**: 
  - Ruta: /movies/<int:id>/
  - Método: GET
  - Descripción: Obtiene una película por su ID.

- **Eliminar película por ID**: 
  - Ruta: /movies/<int:id>/
  - Método: DELETE
  - Descripción: Elimina una película por su ID.

- **Modificar película por ID**: 
  - Ruta: /movies/<int:id>/
  - Método: PUT
  - Descripción: Modifica una película por su ID.

- **Crear película**: 
  - Ruta: /movies/
  - Método: POST
  - Descripción: Crea una nueva película.

- **Resumen de películas**: 
  - Ruta: /summary/
  - Método: GET
  - Descripción: Obtiene un resumen de películas por país y conteo de calificaciones.

- **Obtener las mejores películas**: 
  - Ruta: /top/
  - Método: GET
  - Descripción: Obtiene las 5 mejores películas según su rating.

  - **GeoJSON de películas por país**: 
  - Ruta: /geojson/
  - Método: GET
  - Descripción: Devuelve un GeoJSON con los puntos geográficos de los países de las películas en la base de datos. Cada punto incluye el título de la película, su calificación y el país donde se ubicó. 

  El cuerpo de la respuesta sigue el formato GeoJSON con un `FeatureCollection` que contiene las características de cada película, incluyendo sus propiedades (título, calificación y país) y la geometría del punto geográfico.


## Vistas

Las vistas utilizan Django REST Framework y manejan las solicitudes HTTP para cada endpoint.

## Base de Datos

Se utiliza PostgreSQL como base de datos para almacenar la información sobre las películas.

## Requisitos adicionales para la Seccion2

Para la implementación de la funcionalidad de la Sección 2, se requiere instalar la librería `gdal` y en el archivo de configuración settings.py definir la variable de entorno `GDAL_LIBRARY_PATH` apuntando al archivo `gdal308.dll`. Esto es necesario para el correcto funcionamiento del servicio que devuelve el GeoJSON con los puntos geográficos de los países de las películas. `GDAL_LIBRARY_PATH = 'C:/OSGeo4W/bin/gdal308.dll'`


