"""
1. Ejericio de herencia y polimorfismo
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} says: Meow!")


dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

dog.sound()
cat.sound()


"""
2. Ejercicio de herencia y polimorfismo
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""


class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def work(self):
        pass


class Manager(Employee):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self.employees = []

    def work(self):
        print(f"{self.name} is managing the team.")

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class ProjectManager(Manager):
    def work(self):
        print(f"{self.name} is managing the project.")


class Programmer(Employee):
    def work(self):
        print(f"{self.name} is coding.")


manager = Manager(id=1, name="John")
project_manager = ProjectManager(id=2, name="Alice")
programmer = Programmer(id=3, name="Bob")

manager.add_employee(project_manager)
manager.add_employee(programmer)

manager.work()
manager.print_employees()
project_manager.work()
programmer.work()
