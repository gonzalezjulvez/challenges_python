import os
import time

"""
EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como
tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.
"""


def create_file(file_name: str) -> None:
    with open(file_name, "w", encoding="UTF-8") as file:
        file.write("Nombre: Javier González\n")
        file.write("Edad: 30\n")
        file.write("Lenguaje de programación favorito: Python\n")

    with open(file_name, "r", encoding="UTF-8") as file:
        print(file.read())

    os.remove(file_name)


file_name = "prueba.txt"
# create_file(file_name)


"""
DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
"""


file_name = "prueba.txt"

while True:
    print("\n--- Menú de opciones ---")
    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Borrar Producto")
    print("5. Mostrar todos los productos")
    print("6. Calcular venta total")
    print("7. Calcular por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")
    print("\n")

    if option == "1":
        # Añadir un nuevo producto
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name},{quantity},{price}\n")
        print("Producto añadido.")
        time.sleep(1.5)

    elif option == "2":
        # Consultar un producto por nombre
        name = input("Nombre del producto a consultar: ")
        found = False
        with open(file_name, "r") as file:
            for line in file:
                if name in line:
                    print("Producto encontrado: ", line.strip())
                    found = True
        if not found:
            print("Producto no encontrado.")
        time.sleep(1.5)

    elif option == "3":
        # Actualizar un producto
        name = input("Nombre del producto a actualizar: ")
        updated_lines = []
        updated = False
        with open(file_name, "r") as file:
            for line in file:
                if name in line:
                    quantity = input("Nueva cantidad: ")
                    price = input("Nuevo precio: ")
                    updated_lines.append(f"{name},{quantity},{price}\n")
                    updated = True
                else:
                    updated_lines.append(line)
        if updated:
            with open(file_name, "w") as file:
                file.writelines(updated_lines)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

        time.sleep(1.5)

    elif option == "4":
        # Borrar un producto
        name = input("Nombre del producto a borrar: ")
        updated_lines = []
        deleted = False
        with open(file_name, "r") as file:
            for line in file:
                if name not in line:
                    updated_lines.append(line)
                else:
                    deleted = True
        if deleted:
            with open(file_name, "w") as file:
                file.writelines(updated_lines)
            print("Producto borrado.")
        else:
            print("Producto no encontrado.")
        time.sleep(1.5)

    elif option == "5":
        # Mostrar todos los productos
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                content = file.read()
                if content.strip():
                    print("\n--- Lista de productos ---")
                    print(content)
                else:
                    print("No hay productos.")
        else:
            print("El archivo de productos no existe.")
        time.sleep(1.5)

    elif option == "6":
        # Calcular venta total (asumiendo que cantidad y precio son números)
        total = 0
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                for line in file:
                    name, quantity, price = line.strip().split(",")
                    total += int(quantity) * float(price)
            print(f"Venta total: {total}")
        else:
            print("No hay productos para calcular la venta total.")
        time.sleep(1.5)

    elif option == "7":
        # Calcular venta por producto
        name = input("Nombre del producto: ")
        found = False
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                for line in file:
                    if name in line:
                        found = True
                        name, quantity, price = line.strip().split(",")
                        total = int(quantity) * float(price)
                        print(f"Venta total para {name}: {total}")
        if not found:
            print("Producto no encontrado.")

        time.sleep(1.5)

    elif option == "8":
        # Salir del programa
        print("Saliendo del programa.")
        time.sleep(1.5)
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción correcta.")
        time.sleep(1.5)
