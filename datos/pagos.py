import pandas as pd
import matplotlib.pyplot as plt

class Pago:
    def __init__(self, payment_method):
        self.payment_method = payment_method
    
    def __str__(self):
        return f"Método de Pago: {self.payment_method}"
    
    @staticmethod
    def analisis_distribucion_pagos(df_ventas):
        # Contar la frecuencia de cada tipo de pago
        df_pagos = df_ventas['Payment'].value_counts()

        # Plotear el gráfico de pastel
        plt.figure(figsize=(8, 6))
        df_pagos.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral'])
        plt.title('Distribución de Tipos de Pago')
        plt.ylabel('')

        plt.show()

    @staticmethod
    def scatter_tipo_pago_vs_cantidad(df_ventas):
        # Filtrar los datos relevantes para el scatter plot
        df_pagos = df_ventas[['Payment', 'Total']]
        
        # Plotear el scatter plot
        plt.figure(figsize=(10, 6))
        colors = {'Cash': 'blue', 'Credit card': 'green', 'Ewallet': 'orange'}
        plt.scatter(df_pagos['Payment'], df_pagos['Total'], c=df_pagos['Payment'].map(colors), alpha=0.6)
        
        # Añadir etiquetas y título
        plt.title('Scatter Plot: Tipo de Pago vs Cantidad Pagada')
        plt.xlabel('Tipo de Pago')
        plt.ylabel('Cantidad Pagada ($)')
        plt.xticks(rotation=45)
        
        # Añadir leyenda personalizada
        handles = [plt.Line2D([0,0],[0,0],marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors.values()]
        labels = list(colors.keys())
        plt.legend(handles, labels, loc='best')
        
        plt.grid(True)
        plt.tight_layout()
        plt.show()