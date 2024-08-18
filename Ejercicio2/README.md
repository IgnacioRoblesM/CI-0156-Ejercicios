# Frontend Clean Architecture Folder Structure Breakdown

## Entities

Está compuesta por archivos de tipo entidad, las cuales representan unidades de negocio que conforman la lógica más básica y definitiva que define al negocio.

Esta capa no cambia sin importar que los desarrolladores cambien de framework web o casos de uso.

## Services

Esta capa funciona como una serie de archivos que contienen funciones con parámetros que envían datos y reciben respuestas para la aplicación. Puede utilizar las entidades para moldear las respuestas (usualmente en formato JSON) de los APIs.

## Use Cases / Stores

Esta capa contiene los casos de uso que van a ser llamados por los componentes. Estos casos de uso van a guardar los datos en una variable "state". Además facilita la interacción con los componentes,

## Components

Esta capa se encarga de la presentación UI, la interacción con el usuario y actualización de vistas. 
