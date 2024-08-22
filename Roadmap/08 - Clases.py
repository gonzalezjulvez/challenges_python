"""
1. Ejercicio de clases

Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.
"""


class Person:
    def __init__(self, name: str, age: int, country: str):
        self.name = name
        self.age = age
        self.country = country

    def print_person(self):
        print(f"Name: {self.name}, Age: {self.age}, Country: {self.country}")


person = Person(name="John", age=30, country="USA")
person.print_person()

"""
2. Ejercicio de clases
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido.
"""


class Stack:
    def __init__(self):
        self.stack: list[int] = []

    def add(self, element: int) -> None:
        self.stack.append(element)

    def remove(self) -> int:
        return self.stack.pop()

    def count(self) -> int:
        return len(self.stack)

    def print_stack(self) -> list[int]:
        return self.stack


class Queue:
    def __init__(self):
        self.queue: list[int] = []

    def add(self, element: int) -> None:
        self.queue.append(element)

    def remove(self) -> int:
        return self.queue.pop(0)

    def count(self) -> int:
        return len(self.queue)

    def print_queue(self) -> list[int]:
        return self.queue


stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
print(stack.print_stack())
print(stack.remove())
print(stack.print_stack())
print(stack.count())

queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.print_queue())
print(queue.remove())
print(queue.print_queue())
print(queue.count())
