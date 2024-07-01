import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Evaluacion:
    def __init__(self, rating):
        self.rating = rating
    
    def __str__(self):
        return f"Evaluación: Calificación: {self.rating}"
    
    @staticmethod
    def promedio_ratings_por_categoria(df_ventas):
        # Agrupar por categoría de producto y calcular el promedio de ratings
        promedios_ratings = df_ventas.groupby('Product line')['Rating'].mean()

        # Ordenar por promedio de ratings
        promedios_ratings = promedios_ratings.sort_values(ascending=False)

        # Plotear el gráfico de barras
        plt.figure(figsize=(10, 6))
        promedios_ratings.plot(kind='bar', color='skyblue')

        # Añadir etiquetas y título
        plt.title('Promedio de Ratings por Categoría de Productos')
        plt.xlabel('Categoría de Producto')
        plt.ylabel('Promedio de Rating')
        plt.xticks(rotation=45)

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def ratings_por_categoria_genero(df):
        # Crear el gráfico de violín
        plt.figure(figsize=(14, 10))
        sns.violinplot(x='Product line', y='Rating', hue='Gender', data=df, split=True, palette='muted', inner='quartile')
        
        plt.title('Distribución de Ratings por Categoría de Producto y Género', fontsize=14)
        plt.xlabel('Categoría de Producto', fontsize=12)
        plt.ylabel('Rating', fontsize=12)
        plt.legend(title='Género', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()