"""
1. Ejercicio de pilas y colas
Implementa los mecanismos de introducción y recuperación de elementos propios de las pilas
(stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array o lista
(dependiendo de las posibilidades de tu lenguaje).
"""

# Pila/Stack (LIFO)
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())

# Cola/Queue (FIFO)
queue = []

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.pop(0))
print(queue)


"""
2. Ejercicio de pilas y colas
Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
"""


def web_navigation():
    stack = []
    current_page = "google.com"
    stack.append(current_page)
    while True:
        action = input("Introduce la acción a realizar: ")
        if action == "adelante":
            if len(stack) > 1:
                stack.pop()
                print(f"Estás en la página: {stack[-1]}")
            else:
                print("No hay más páginas hacia adelante.")
        elif action == "atrás":
            web = input("Introduce la página web: ")
            stack.append(web)
            print(f"Estás en la página: {web}")
        elif action == "salir":
            print("Saliendo del programa.")
            break
        else:
            print(f"Estás en la página: {action}")
            stack.append(action)


# web_navigation()


"""
3. Ejercicio de pilas y colas
Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
"""


def printer():
    queue = []
    while True:
        action = input("Introduce la acción a realizar: ")
        if action == "imprimir":
            if queue:
                print(f"Imprimiendo documento: {queue.pop(0)}")
            else:
                print("No hay documentos para imprimir.")
        elif action == "salir":
            print("Saliendo del programa.")
            break
        else:
            print(f"Documento añadido a la cola: {action}")
            queue.append(action)


printer()
