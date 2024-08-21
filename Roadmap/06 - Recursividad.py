"""
1. Ejecercio de recursividad
Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
"""


def countdown(number: int) -> None:
    if number < 0:
        return
    print(number)
    countdown(number - 1)


# countdown(100)

"""
2. Ejecercio de recursividad
Calcular el factorial de un número concreto (la función recibe ese número).
"""


def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)


print(factorial(number=5))

"""
3. Ejercicio de recursividad

Calcular el valor de un elemento concreto (según su posición) en la sucesión de fibonacci (la función recibe la posición).
"""


def fibonacci(pos: int) -> int:
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)


print(fibonacci(40))
