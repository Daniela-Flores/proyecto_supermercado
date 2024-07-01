import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Producto:
    def __init__(self, precio_unitario, cantidad):
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
    
    def __str__(self):
        return f"Precio Unitario: ${self.precio_unitario}, Cantidad: {self.cantidad}"

    @staticmethod
    def boxplot_precios_unitarios_por_categoria(df_ventas):
        # Filtrar los datos relevantes para el análisis
        df_clientes = df_ventas[['Product line', 'Unit price']]

        # Plotear el box plot
        plt.figure(figsize=(10, 6))
        df_clientes.boxplot(by='Product line', column='Unit price', grid=True)

        # Añadir etiquetas y título
        plt.title('Box Plot: Precios Unitarios por Categoría de Productos')
        plt.xlabel('Categoría de Producto')
        plt.ylabel('Precio Unitario ($)')
        plt.xticks(rotation=45)

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def histograma_precios_unitarios(df):
        plt.figure(figsize=(10, 6))
        sns.histplot(df['Unit price'], kde=True, bins=30, color='blue')
        plt.title('Histograma de Precios Unitarios de los Productos', fontsize=14)
        plt.xlabel('Precio Unitario', fontsize=12)
        plt.ylabel('Frecuencia', fontsize=12)
        plt.grid(True)
        plt.show()