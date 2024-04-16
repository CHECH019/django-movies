# Movies API

Este proyecto utiliza Django REST Framework y PostgreSQL para proporcionar una API para administrar películas.

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

## Vistas

Las vistas utilizan Django REST Framework y manejan las solicitudes HTTP para cada endpoint.

## Base de Datos

Se utiliza PostgreSQL como base de datos para almacenar la información sobre las películas.



