import pandas as pd
import matplotlib.pyplot as plt

class Cliente:
    def __init__(self, customer_type, gender):
        self.customer_type = customer_type
        self.gender = gender
    
    def __str__(self):
        return f"Cliente: Tipo: {self.customer_type}, Género: {self.gender}"
    
    @staticmethod
    def analisis_distribucion_compras(df_ventas):
        # Filtrar y agrupar por tipo de cliente y género
        df_clientes = df_ventas.groupby(['Customer type', 'Gender']).size().unstack()
        
        # Plotear el gráfico de barras dobles
        df_clientes.plot(kind='bar', stacked=False)
        plt.xlabel('Tipo de Cliente')
        plt.ylabel('Número de Compras')
        plt.title('Distribución de Compras por Tipo de Cliente y Género')
        plt.xticks(rotation=0)
        plt.show()
    
    @staticmethod
    def distribucion_compras_por_genero(df_ventas):
        # Filtrar los datos relevantes para el análisis
        df_clientes = df_ventas[['Gender', 'Product line']]

        # Agrupar por género y categoría de producto, contar las compras y ordenar por categoría
        df_clientes_agrupado = df_clientes.groupby(['Product line', 'Gender']).size().unstack(fill_value=0)

        # Plotear el gráfico de barras
        df_clientes_agrupado.plot(kind='bar', figsize=(12, 6), width=0.8)

        # Añadir etiquetas y título
        plt.title('Distribución de Compras por Género y Categoría de Producto')
        plt.xlabel('Categoría de Producto')
        plt.ylabel('Número de Compras')
        plt.xticks(rotation=45)
        plt.legend(title='Género')

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def tipos_pago_por_tipo_cliente(df):
        # Agrupar por tipo de cliente y tipo de pago, y contar las ocurrencias
        pago_por_cliente = df.groupby(['Customer type', 'Payment']).size().unstack()
        
        # Crear el gráfico de barras agrupadas
        pago_por_cliente.plot(kind='bar', stacked=False, figsize=(12, 8), colormap='tab10')
        
        plt.title('Tipos de Pago por Tipo de Cliente', fontsize=14)
        plt.xlabel('Tipo de Cliente', fontsize=12)
        plt.ylabel('Cantidad de Pagos', fontsize=12)
        plt.legend(title='Tipo de Pago', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=0)
        plt.grid(True)
        plt.tight_layout()
        plt.show()