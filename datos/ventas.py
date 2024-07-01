import csv

class Venta:
    ARCHIVO_VENTAS = 'supermarket_sales.csv'  # Definir el archivo CSV donde se guardan las ventas
    
    def __init__(self, invoice_id, branch, city, customer_type, gender, product_line, unit_price, quantity, tax, total, date, time, payment, cogs, gross_margin_percentage, gross_income, rating):
        self.invoice_id = invoice_id
        self.branch = branch
        self.city = city
        self.customer_type = customer_type
        self.gender = gender
        self.product_line = product_line
        self.unit_price = unit_price
        self.quantity = quantity
        self.tax = tax
        self.total = total
        self.date = date
        self.time = time
        self.payment = payment
        self.cogs = cogs
        self.gross_margin_percentage = gross_margin_percentage
        self.gross_income = gross_income
        self.rating = rating

    @classmethod
    def registrar_nueva_venta(cls):
        invoice_id = input("Ingrese el Invoice ID: ")
        branch = input("Ingrese la Branch (A, B o C): ")
        city = input("Ingrese la City: ")
        customer_type = input("Ingrese el Customer type (Member o Normal): ")
        gender = input("Ingrese el Gender (Male o Female): ")
        product_line = input("Ingrese la Product line: ")
        unit_price = float(input("Ingrese el Unit price ($): "))
        quantity = int(input("Ingrese la Quantity: "))
        tax = unit_price * quantity * 0.05
        total = unit_price * quantity + tax
        date = input("Ingrese la Date (Mes/Día/Año): ")
        time = input("Ingrese la Hora (HH:MM): ")
        payment = input("Ingrese el Payment (Cash, Credit card o Ewallet): ")
        cogs = unit_price * quantity
        gross_margin_percentage = 0.3  # Ejemplo de margen bruto (30%)
        gross_income = total - cogs
        rating = input("Ingrese el Rating (1-10): ")

        nueva_venta = {
            'Invoice ID': invoice_id,
            'Branch': branch,
            'City': city,
            'Customer type': customer_type,
            'Gender': gender,
            'Product line': product_line,
            'Unit price': unit_price,
            'Quantity': quantity,
            'Tax': tax,
            'Total': total,
            'Date': date,
            'Time': time,
            'Payment': payment,
            'cogs': cogs,
            'gross margin percentage': gross_margin_percentage,
            'gross income': gross_income,
            'Rating': rating
        }

        with open(cls.ARCHIVO_VENTAS, 'a', newline='') as archivo:
            escritor_csv = csv.DictWriter(archivo, fieldnames=nueva_venta.keys())
            escritor_csv.writerow(nueva_venta)

        print("Nueva venta registrada exitosamente.")

    @staticmethod
    def eliminar_venta_por_id(invoice_id):
        ventas_actualizadas = []
        venta_eliminada = None

        with open(Venta.ARCHIVO_VENTAS, 'r', newline='') as archivo:
            lector_csv = csv.DictReader(archivo)
            for venta in lector_csv:
                if venta['Invoice ID'] == invoice_id:
                    venta_eliminada = venta
                else:
                    ventas_actualizadas.append(venta)

        if venta_eliminada:
            with open(Venta.ARCHIVO_VENTAS, 'w', newline='') as archivo:
                fieldnames = ventas_actualizadas[0].keys() if ventas_actualizadas else []
                escritor_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
                escritor_csv.writeheader()
                for venta in ventas_actualizadas:
                    escritor_csv.writerow(venta)
            print(f"Venta con Invoice ID {invoice_id} eliminada correctamente.")
        else:
            print(f"No se encontró ninguna venta con Invoice ID {invoice_id}.")
