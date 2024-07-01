
import pandas as pd
import matplotlib.pyplot as plt

class Sucursal:
    def __init__(self, branch, city):
        self.branch = branch
        self.city = city
    
    def __str__(self):
        return f"Sucursal: {self.branch}, Ciudad: {self.city}"
    
    @staticmethod
    def ventas_por_ciudad_y_sucursal(df_ventas):
        # Agrupar por ciudad y branch, contar las ventas y ordenar por ciudad
        df_ventas_agrupado = df_ventas.groupby(['City', 'Branch']).size().unstack(fill_value=0)

        # Plotear el gráfico de barras
        df_ventas_agrupado.plot(kind='bar', stacked=True, figsize=(10, 6))
        
        # Añadir etiquetas y título
        plt.title('Número de Ventas por Ciudad y Sucursal')
        plt.xlabel('Ciudad')
        plt.ylabel('Número de Ventas')
        plt.xticks(rotation=45)
        
        plt.legend(title='Sucursal', loc='upper right')
        
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def categorias_mas_vendidas_por_sucursal(df):
        # Agrupar por Sucursal y Categoría, y contar la cantidad de productos vendidos
        categorias_por_sucursal = df.groupby(['City', 'Product line']).size().unstack()
        
        # Crear el gráfico de barras
        categorias_por_sucursal.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='tab20')
        
        plt.title('Categorías Más Vendidas por Sucursal', fontsize=14)
        plt.xlabel('Ciudad', fontsize=12)
        plt.ylabel('Cantidad de Productos Vendidos', fontsize=12)
        plt.legend(title='Categoría', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
