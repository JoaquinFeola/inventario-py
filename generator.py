import random
from datetime import date, timedelta

start_date = date(2023,2,3)
end_date = date(2026,11,24)
days_range = (end_date - start_date).days

categories = ["Limpieza","Bebidas", "Alimentos", "Perfumería"]
FIELDS = {
    "id_producto": lambda n : n,
    "nombre": lambda n: f"Producto {n}",
    "categoria": lambda n : random.choice(categories),
    "stock": lambda n: random.randint(0, 39),
    "precio_unitario": lambda n: round(random.uniform(150.0, 25000.0),2),
    "fecha_ingreso": lambda n: (
        start_date + timedelta(days=random.randint(0, days_range))
    ).strftime("%Y-%m-%d"),
}


def generar_producto(n: int) -> dict:
    return {campo: fn(n) for campo, fn in FIELDS.items()}

for i in range(1,101):
    producto = generar_producto(i)
    for k,v in producto.items():
        print(f"{k}: {v}")
    print("-" * 25)