# import csv
# from datetime import date,  timedelta
# from dataclasses import dataclass
# from decimal import Decimal
# from  pathlib  import Path
# from datetime import datetime

# FILE_NAME = "inventario.csv"

# @dataclass(frozen=True)
# class Product:
#    id_producto: int
#    nombre: str
#    categoria: str
#    stock: int
#    precio_unitario: Decimal
#    fecha_ingreso: date
   
#    @classmethod
#    def from_row(cls, row: dict) -> "Producto":
#     try:
#         id_producto = int(row["id_producto"].strip())
#         except

# def es_fecha_valida(fecha_ingresada: str): #Validamos la fecha
#     texto = fecha_ingresada.strip()
#     if len(texto) != 10:
#         return False
#     try:
#         datetime.strptime(texto, "%Y-%m-%d")
#         return True
#     except ValueError:
#         return False
    
# def cargar_validar(inventario_csv):
#     productos = []
#     descartados = 0

# productos = {
#     "producto"
#     "Nombre"
#     "Categoria"
#     "Stock"
#     "Precio unitario"
#     "Fecha ingreso"
# }
# productos.append(productos)



# def validate_product(product: Dict)


# with open(FILE_NAME, "r", newline=" ") as f: 
#     reader = csv.DictReader(f)
#     data = []


import csv
from datetime import datetime

INPUT_FILE = "inventario.csv"
CRITICAL_STOCK = 5

def validate_row(row):
    try:
        product = {
            "id_producto": int(row["id_producto"]),
            "nombre": row["nombre"].strip(),
            "categoria": row["categoria"].strip(),
            "stock": int(row["stock"]),
            "precio_unitario": float(row["precio_unitario"]),
            "fecha_ingreso": row["fecha_ingreso"].strip()
        }
        
        datetime.strptime(product["fecha_ingreso"], "%Y-%m-%d")
        
    except (ValueError, KeyError, AttributeError): 
        return None
    
    if product["id_producto"] < 0 or product["nombre"] == "" or product["categoria"] == "" or product["stock"] < 0: 
        return None
    
    return product
    

def load_data(path: str):
    products = []
    dismissed_products_count = 0
    ids_seen = set()
    ids_errors = set()
    
    with open(path, "r", newline="", encoding="utf-8") as f: 
        
        for row in csv.DictReader(f):
            product = validate_row(row)
            
            if product is None or product["id_producto"] in ids_seen:
                dismissed_products_count += 1
                ids_errors.add(row["id_producto"])
                continue
            
            ids_seen.add(product["id_producto"])
            products.append(product)
    
    print(ids_errors)

load_data(INPUT_FILE)

""" def categories_aggregation(products):
    categoriesProducts = {}
    
    for product in products """