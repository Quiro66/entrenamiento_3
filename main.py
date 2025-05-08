# Inventory management

products = {}

def add_product():
    while True:
        try:
            print("ADD PRODUCT")
            name = input("Add the product name: ")
            if name in products:
                print("Error, product already exists")
                return
            price = int(input("Add the product price: "))
            try:
                quantity = int(input("Add the product amount: "))
                if quantity <1:
                    raise ValueError
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

add_product()

