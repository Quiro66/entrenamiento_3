# 🛒 Inventory Management System - Python

Este proyecto es un sistema interactivo para **gestionar el inventario de una tienda**, desarrollado en Python. Permite al usuario **añadir, consultar, actualizar y eliminar productos**, además de **calcular el valor total del inventario** usando funciones lambda.  

## 🧾 Requisitos

- Python 3.7+
- Ejecutar desde terminal: `python main.py`

## 🧠 Funcionalidades

- **📥 Añadir productos**  
  Guarda nombre, precio y cantidad del producto en una estructura dinámica.  
  Valida que los datos ingresados sean correctos y únicos.

- **🔍 Consultar productos**  
  Permite buscar un producto por nombre y mostrar su precio y cantidad.  
  Si no se encuentra, notifica al usuario.

- **💰 Actualizar precios**  
  Cambia el precio de un producto existente ingresando su nombre y nuevo valor.

- **🗑️ Eliminar productos**  
  Elimina un producto del inventario por su nombre, si existe.

- **🧮 Calcular valor total del inventario**  
  Usa una función `lambda` para calcular `precio * cantidad` de todos los productos.

## 📦 Estructura de Datos

- Los productos se almacenan en un **diccionario**, con el nombre del producto como **clave** y una **tupla** con precio y cantidad como **valor**:
  
  ```python
  inventory = {
      "laptop": (1500, 3),
      "mouse": (25, 10)
  }
 

```bash
 Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
Choose an option: 1
ADD PRODUCT
Add the product name: fresa
Add the product price: 2000
Add the product quantity: 30
fresa product added correctly

Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
Choose an option: 1
ADD PRODUCT
Add the product name: mango
Add the product price: 3500
Add the product quantity: 22
mango product added correctly

Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
Choose an option: 2
SEARCH PRODUCTS
add name to search for product: fresa

 Name: fresa
 Price: $2000
 Quantity: 30

Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
Choose an option: 3
UPDATE PRICE PRODUCT
add name to search for product: fresa
Name: fresa
 Price: $2000
 Quantity: 30
Add the new price of the product: 2500
Product price updated.
Name: fresa
 Price: $2500
 Quantity: 30

Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
Choose an option: 4
DELETE PRICE PRODUCT
add name to search for product: mango
Deleted

Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
Choose an option: 5
The total of the product is: $75000

Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
Choose an option: 6
```
@Quiro66
