# Proyecto final DAAD

Sistema para almacenamiento y análisis de ventas de un supermercado.

## Instrucciones para probar la implementación:

1. Descargar este proyecto como `.zip` o clonar directamente el repositorio a una ubicación local.
2. Descomprima el .zip o abra en su navegador de archivos la carpeta donde ha clonado el proyecto.
4. Asegúrese de ubicarse dentro de la carpeta `proyecto_supermercado` que ha descargado.
5. Instale las librerías seaborn, pandas y matplotlib si aún no las tiene en su ambiente de python. 
6. Asegurándose de estar a la altura de `supermarket.csv` y `main.py`, ejecute `main.py`.
7. Navegue por el menú de opciones que verá en la terminal y pruebe las opciones del menú. 
8. Para la sección de análisis, verá que se abren gráficos; cierre un gráfico para que aparezca el siguiente.

## ¿Cómo funciona?

Este sistema utiliza el paradigma orientado a objetos, dentro de la carpeta 'datos' pueden encontrarse en forma de paquete las distintas clases creadas para su funcionamiento (clientes, evaluaciones, pagos, productos, sucursal, ventas).

Dentro de 'datos' está un archivo __init__py que marca este directorio como paquete y facilitar el acceso a los módulos.

El programa arranca con 'main.py' que despliega un menú en la terminal con opciones para interactuar con las clases y sus métodos.

El sistema inicialmente se alimenta de el dataset que hemos incluido en este proyecto: 'supermarket_sales.csv' y pueden añadirse más registros de ventas o eliminarse por ID.

Con pandas, matplotlib y seaborn se han creado varios gráficos de análisis que pueden explorarse para entender mejor la distribución de los datos.
