from common import load_inventory, aggregate_by_category, get_top_products_by_value, get_critical_products

INVENTORY_FILE_PATH = "inventario.csv"
CRITICAL_STOCK = 5
TOP_N = 10

# Demostración
def print_table_head(title: str):
    print('=' * 100)
    print(title)
    print('=' * 100)
    
def print_aggregate_categories_table(categories_products):
    print_table_head("1. AGREGACIÓN POR CATEGORÍA")
    print(f"Categoría {' ' * 10 } Stock total {' ' * 10} Valor total")
    print('- ' * 50)
    for pk, pv in categories_products.items():
        print(f"{pk:<15} {' ' * 10} {pv['total_stock']:,} {' ' * 10} $ {pv['valor_total']:,.2f}")
        
        
def print_critical_stock_table(critical_products):
    print_table_head("2. PRODUCTOS CRÍTICOS (STOCK < 5)")
    print(f"ID {' ' * 10 } Nombre {' ' * 10} Categoría {' ' * 10} Stock")
    print('- ' * 50)
    for p in critical_products:
        print(f"{p['id_producto']:<15} {' ' * 10} {p['nombre']:<4} {' ' * 10} {p['categoria']:<15} {' ' * 10} {p['stock']} ")


def print_top_products_table(top_products):
    print_table_head("3. TOP DE PRODUCTOS")
    print(f"ID {' ' * 10 } Nombre {' ' * 10} Categoría {' ' * 10} Valor total")
    print("- " * 50)
    for p in top_products:
        print(f"{p['id_producto']:<15} {' ' * 10} {p['nombre']:<15} {' ' * 10} {p['categoria']:<15} {' ' * 10} $ {p['stock'] * p['precio_unitario'] :,.2f} ")

def print_load_inventory_feedback(rows_read: int, valid_rows: int, products_alert: int, dismissed_count: int): 
    print(f"Filas leídas: {rows_read} | Válidas: {valid_rows} | Descartadas: {dismissed_count} | Alertas: {products_alert}")
    



def main():
    products, ids_errors, dismissed_count = load_inventory(INVENTORY_FILE_PATH)
    categories_products = aggregate_by_category(products)
    rows_read = dismissed_count + len(products)
    valid_rows = rows_read - dismissed_count
    critical_products = get_critical_products(products, CRITICAL_STOCK)
    top_products = get_top_products_by_value(products, TOP_N)
    
    print_aggregate_categories_table(categories_products)
    print_critical_stock_table(critical_products)
    print_top_products_table(top_products)
    print_load_inventory_feedback(rows_read, valid_rows, len(critical_products), dismissed_count)

if __name__ == "__main__":
    main()