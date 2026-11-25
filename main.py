from processor import main as process_inventory_csv
from report import main as generate_report

def main():
    process_inventory_csv()
    generate_report()
    
if __name__ == "__main__":
    main()