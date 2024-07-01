from datos.productos import Producto
from datos.ventas import Venta
from datos.clientes import Cliente
from datos.sucursal import Sucursal
from datos.pagos import Pago
from datos.evaluaciones import Evaluacion
import random
import csv
from datetime import datetime, timedelta
import pandas as pd

# Cargar datos desde el archivo CSV
df_ventas = pd.read_csv('supermarket_sales.csv')

def menu_analisis_ventas():
    while True:
        print("\n=== Menú de Análisis de Ventas ===")
        print("1. Distribución de clientes")
        print("2. Análisis de pagos/precios")
        print("3. Ventas y sucursales")
        print("4. Análisis de categorías")
        print("5. Volver al Menú Principal")
        
        opcion_analisis = input("Ingrese una opción (1/2/3/4/5): ")
        
        if opcion_analisis == '1':
            # Análisis gráfico que involucra clientes
            Cliente.analisis_distribucion_compras(df_ventas)
            Evaluacion.ratings_por_categoria_genero(df_ventas)
        elif opcion_analisis == '2':
            # Análisis con gráficos referentes a pagos y precios
            Pago.analisis_distribucion_pagos(df_ventas)
            Pago.scatter_tipo_pago_vs_cantidad(df_ventas)
            Producto.histograma_precios_unitarios(df_ventas)
            Cliente.tipos_pago_por_tipo_cliente(df_ventas)
        elif opcion_analisis == '3':
            # Gráficos de análisis que tienen que ver con sucursales
            Sucursal.ventas_por_ciudad_y_sucursal(df_ventas)
            Sucursal.categorias_mas_vendidas_por_sucursal(df_ventas)
        elif opcion_analisis == '4':
            # Análisis enfocado a diferencias entre categorías de producto
            Cliente.distribucion_compras_por_genero(df_ventas)
            Evaluacion.promedio_ratings_por_categoria(df_ventas)
            Producto.boxplot_precios_unitarios_por_categoria(df_ventas)
        elif opcion_analisis == '5':
            print("Volviendo al Menú Principal...")
            break  # Salir del bucle while
        else:
            print("Opción no válida. Por favor, ingrese 1, 2, 3, 4 o 5.")

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar una nueva venta")
        print("2. Eliminar una venta por ID")
        print("3. Analizar ventas")
        print("4. Salir")
        
        opcion = input("Ingrese una opción (1/2/3/4): ")
        
        if opcion == '1':
            Venta.registrar_nueva_venta()
        elif opcion == '2':
            invoice_id = input("Ingrese el Invoice ID de la venta a eliminar: ")
            Venta.eliminar_venta_por_id(invoice_id)
        elif opcion == '3':
            print(df_ventas.head())  # Mostrar los primeros registros del DataFrame
            menu_analisis_ventas()  # Llama al menú de análisis de ventas
        elif opcion == '4':
            print("Saliendo del programa...")
            break  # Salir del bucle while
        else:
            print("Opción no válida. Por favor, ingrese 1, 2, 3 o 4.")

if __name__ == "__main__":
    menu_principal()

