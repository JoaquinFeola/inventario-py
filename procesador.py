import csv
from datetime import date,  timedelta
from  pathlib  import Path
from datetime import datetime


def es_fecha_valida(fecha_ingresada: str): #Validamos la fecha
    texto = fecha_ingresada.strip()
    if len(texto) != 10:
        return False
    try:
        datetime.strptime(texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def cargar_validar(inventario_csv):
    productos = []
    descartados = 0
    
productos = {
    "producto"
    "Nombre"
    "Categoria"
    "Stock"
    "Precio unitario"
    "Fecha ingreso"
}
productos.append(productos)

