# Inventory management

products = {}

def add_product():
    while True:
        try:
            print("ADD PRODUCT")
            name = input("Add the product name: ").strip().lower()
            if name in products:
                print("Error, product already exists")
                return
            price = int(input("Add the product price: "))
            try:
                quantity = int(input("Add the product quantity: "))
                if quantity < 1:
                    print("Quantity must be greater than 0.")
                    return
            except ValueError:
                print("quantity of invalid")
                return
            products[name] = {
                "price" : price,
                "quantity" : quantity
            }
            print(f"{name} product added correctly")
            return False
        except ValueError:
            print("Error, enter a valid value")

def search_product():
    while True:
        try:
            print("SEARCH PRODUCTS")
            name_search = (input("add name to search for product: ")).strip().lower()
            product = products.get(name_search)
            if not product:
                print("Product no found")
                return
            print(f"\n Name: {name_search}\n Price: ${product['price']}\n Quantity: {product['quantity']}")
            return False
        except ValueError:
            print("Error, enter a valid value")
    
def update_price_product():
    while True:
        try:
            print("UPDATE PRICE PRODUCT")
            name_search = input("add name to search for product: ").strip().lower()
            product = products.get(name_search)
            if not product:
                print("Product no found")
                return True
            print(f"Name: {name_search}\n Price: ${product['price']}\n Quantity: {product['quantity']}")
            change_price = int(input("Add the new price of the product: "))
            if change_price > 0:
                product['price'] = change_price
                print("Product price updated.")
                print(f"Name: {name_search}\n Price: ${product['price']}\n Quantity: {product['quantity']}")
                return False
            else:
                print("the price is invalid")
                return True
        except ValueError:
            print("Error, enter a valid value")

def deleted_product():
    while True:
        try:
            print("DELETE PRICE PRODUCT")
            name_search = input("add name to search for product: ").strip().lower()
            product = products.get(name_search)
            if not product:
                print("Product no found")
                return 
            del products[name_search]
            print(f"Deleted ")
            return False
        except ValueError:
            print("Error, enter a valid value")

def cal_inventory_value():
    total = sum(map(lambda product: product['price'] * product['quantity'], products.values()))
    print(f"The total of the product is: ${total}")
def menu():
    opcion = {
        "1": add_product,
        "2": search_product,
        "3": update_price_product,
        "4": deleted_product,
        "5": cal_inventory_value,
        "6": exit
    }

    while True:
        print("\nInventory management")
        print("1. Add product")
        print("2. Search product")
        print("3. Update price product")
        print("4. Deleted product")
        print("5. calculate inventory value")
        print("6. Exit")

        action = input("Choose an option: ").strip()
        if action in opcion:
            opcion[action]()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
#@quiro66
