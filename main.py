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
                quantity = int(input("Add the product amount: "))
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
            print(f"\n Name: {name_search}\n Price: {product['price']}\n Quantity: {product['quantity']}")
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
            print(f"Name: {name_search}\n Price: {product['price']}\n Quantity: {product['quantity']}")
            change_price = int(input("Add the new price of the product: "))
            if change_price > 0:
                product['price'] = change_price
                print("Product price updated.")
                print(f"Name: {name_search}\n Price: {product['price']}\n Quantity: {product['quantity']}")
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
            return False
        except ValueError:
            print("Error, enter a valid value")

def cal_inventory_value(products):
    total = sum(map(lambda product: product['price'] * product['quantity'], products.values()))
    return total
    
add_product()
add_product()
search_product()
update_price_product()
deleted_product()

# Calculate inventory value
total_value = cal_inventory_value(products)
print(f"Total value of inventory: {total_value}")