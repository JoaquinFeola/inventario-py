import csv
from datetime import datetime

def parse_product(product):
    try:
        parsed_product = {
            "id_producto": int(product["id_producto"]),
            "nombre": product["nombre"].strip(),
            "categoria": product["categoria"].strip().title(),
            "stock": int(product["stock"]),
            "precio_unitario": float(product["precio_unitario"]),
            "fecha_ingreso": product["fecha_ingreso"].strip()
        }
        
        datetime.strptime(parsed_product["fecha_ingreso"], "%Y-%m-%d")
        
    except (ValueError, KeyError, AttributeError): 
        return None
    
    if parsed_product["id_producto"] < 0 or parsed_product["nombre"] == "" or parsed_product["categoria"] == "" or parsed_product["stock"] < 0 or parsed_product["precio_unitario"] < 0: 
        return None
    
    return parsed_product

# Carga y validación: lista de diccionarios + set.
# Cada producto es un diccionario porque permite acceder a sus campos por nombre
# (p["stock"]) en O(1) y deja el código más legible que usar posiciones.
# Los productos se guardan en una lista porque mantiene el orden del archivo,
# agregar al final es O(1) y después hay que recorrerla completa en cada operación.
# Para detectar IDs repetidos se usa un set: preguntar "id in ids_seen" es O(1)
# en promedio, mientras que buscarlo en una lista sería O(n) por cada fila.
# Complejidad total de la carga: O(n), siendo n la cantidad de filas.
def load_inventory(path: str):
    products = []
    dismissed_count = 0
    ids_seen = set()
    ids_errors = set()
    
    with open(path, "r", newline="", encoding="utf-8") as f: 
        
        for row in csv.DictReader(f):
            product = parse_product(row)
            
            if product is None or product["id_producto"] in ids_seen:
                dismissed_count += 1
                ids_errors.add(row["id_producto"])
                continue
            
            ids_seen.add(product["id_producto"])
            products.append(product)
    
    return products, ids_errors, dismissed_count


# Agregación por categoría: diccionario {categoria: {total_stock, valor_total}}.
# La categoría es la key, así que encontrar sus acumuladores es O(1) en promedio
# y todo el recorrido es O(n).
# Con una lista habría que buscar la categoría en cada producto. Además, el código sería menos claro.
def aggregate_by_category(products: list[dict]) -> dict:
    categories_products = {}
    
    for product in products:
        category: str = product["categoria"].strip().title()
        
        if category not in categories_products:
            categories_products[category] = { "total_productos": 0, "total_stock": 0, "valor_total": 0.0 }
            
        categories_products[category]["total_stock"] += product["stock"]
        categories_products[category]["valor_total"] += product["precio_unitario"] * product["stock"]
        categories_products[category]["total_productos"] += 1
    
    for cp in categories_products.values():
        cp["valor_total"] = round(cp["valor_total"],2)
        
    return categories_products


# Productos críticos: lista filtrada y ordenada.
# Se usa una lista porque el resultado tiene que quedar ordenado por stock
# ascendente, y la lista es la estructura que conserva un orden y se puede
# ordenar con sort(). Un diccionario o un set no sirven para eso.
def get_critical_products(products: list[dict], critical_stock: int = 5) -> list[dict]:
    critical_stock = [p for p in products if p["stock"] < critical_stock]
    critical_stock.sort(key=lambda p: p["stock"])
    
    return critical_stock

# Top-N por valor: cola de prioridad simulada con una lista ordenada.
# Se ordena la lista de mayor a menor por valor (stock * precio_unitario), así el
# primer elemento es el de mayor prioridad, y se toman los primeros N con [:n].
def get_top_products_by_value(products: list[dict], n: int = 10) -> list[dict]:
    in_stock = [p for p in products if p["stock"] != 0]
    in_stock.sort(key=lambda p: p["stock"] * p["precio_unitario"], reverse=True)
    return in_stock[:n]
