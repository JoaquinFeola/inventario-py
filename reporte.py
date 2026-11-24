import csv

RESUMEN_FILE = "resumen_categorias.csv"
RESUMEN_FILE = "alertas_reposicion.txt"

def exportar_categoria_csv(resumen_categorias, archivo_salida=RESUMEN_FILE):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as file:
        data = csv.writer(file)
        data.writerow(["categoria", "total_productos", "total_stock", "valor_total"])

        for categoria, datos in resumen_categorias.items():
            data.writerow([
                categoria,
                datos["total_productos"],
                datos["total_stock"],
                f"{datos['valor_total']:.2f}",
            ])
            
def exportar_alertas_txt(productos_criticos, archivos_salida=RESUMEN_FILE):
    with open(archivos_salida, "w", newline="", encoding="uft-8") as f:
        for productos in productos_criticos:
            f.write(
                f"{productos['id_productos']}  |  {productos['nombre']} | "
                f"Stock actual: {productos['stock']} | Categoria: {productos['categoria']}\n"
            )
            
def mostrar_productos(productos, resumen_categorias, productos_criticos):
    total_productos = len(productos)

    if resumen_categorias:
        cat_mayor = max(
            resumen_categorias.items(),
            key=lambda item: item[1]["valor_total"],
        )
        print(
            f"Categoría con mayor valor total: {cat_mayor[0]} "
            f"(${cat_mayor[1]['valor_total']:.2f})"
        )
        
def mostrar_productos(productos, resumen_categorias, productos_criticos=None):
    total_productos = len(productos)

    if productos_criticos is not None:
        porcentaje = (
            (len(productos_criticos) / total_productos * 100)
            if total_productos > 0
            else 0.0
        )
        print(
            f"Productos críticos: {len(productos_criticos)} de {total_productos} "
            f"({porcentaje:.2f}%)"
        )
        
        print("Precio promedio por categoría:")
    for categoria, datos in resumen_categorias.items():
        promedio = (
            datos["suma_precios"] / datos["total_productos"]
            if datos["total_productos"] > 0
            else 0.0
        )
        print(f"  - {categoria}: ${promedio:.2f}")