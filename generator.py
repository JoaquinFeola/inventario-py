import random
from datetime import date, timedelta
import csv



start_date = date(2023,2,3)
end_date = date(2026,11,24)
days_range = (end_date - start_date).days

categories = ["Limpieza","Bebidas", "Alimentos", "Perfumería"]
FILE_NAME="inventario.csv"
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
FIELD_NAMES = [fname for fname in FIELDS]


def generar_producto(n: int) -> dict:
    return {campo: fn(n) for campo, fn in FIELDS.items()}

def generate_rows(quantity: int) -> list[dict]:
    return [generar_producto(i) for i in range(1, quantity+1)]



def main() -> None:
    rows = generate_rows(120)
    
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Archivo '{FILE_NAME}' generado con éxito.")
    
if __name__ == "__main__":
    main()