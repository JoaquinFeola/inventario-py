import csv
from common import load_inventory, aggregate_by_category, get_critical_products

CRITICAL_STOCK = 5
RESUMEN_FILE_PATH = "resumen_categorias.csv"
ALERT_FILE_PATH = "alertas_reposicion.txt"
INVENTORY_FILE_PATH = "inventario.csv"


def exportar_categoria_csv(categories_products, archivo_salida=RESUMEN_FILE_PATH):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as file:
        data = csv.writer(file)
        data.writerow(["categoria", "total_productos", "total_stock", "valor_total"])

        for categoria, datos in categories_products.items():
            data.writerow([
                categoria,
                datos["total_productos"],
                datos["total_stock"],
                f"{datos['valor_total']:.2f}",
            ])

def exportar_alertas_txt(critical_products, archivos_salida=ALERT_FILE_PATH):
    with open(archivos_salida, "w", newline="", encoding="utf-8") as f:
        for producto in critical_products:
            f.write(
                f"{producto['id_producto']} | {producto['nombre']} | "
                f"Stock actual: {producto['stock']} | Categoria: {producto['categoria']}\n"
            )


def print_best_category_total_value(categories_products):
    if len(categories_products) > 0:
        best_category = max(
            categories_products.items(),
            key=lambda item: item[1]["valor_total"],
        )
        print(
            f"Categoría con mayor valor total: {best_category[0]} "
            f"(${best_category[1]['valor_total']:,.2f})"
        )


def print_products_percentage(products, categories_products, critical_products=None):
    total_products = len(products)

    if critical_products is not None:
        percentage = (len(critical_products) / total_products ) * 100 if total_products > 0 else 0.0
        print(
            f"Productos críticos: {len(critical_products)} de {total_products} "
            f"({percentage:,.2f}%)"
        )
        
    print("Precio promedio por categoría:")
    for categoria, item in categories_products.items():
        print(f"  - {categoria}: ${item['precio_promedio']:,.2f}")

def main():
    products, ids_errors, dismissed_count = load_inventory(INVENTORY_FILE_PATH)
    categories_products = aggregate_by_category(products)
    critical_products = get_critical_products(products, CRITICAL_STOCK)
    
    exportar_categoria_csv(categories_products)
    exportar_alertas_txt(critical_products)
    print_best_category_total_value(categories_products)
    print_products_percentage(products, categories_products, critical_products)

if __name__ == "__main__":
    main()