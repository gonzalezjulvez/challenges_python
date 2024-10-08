"""
EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.
"""


def div0(num1: float | int, num2: float | int) -> float | None:
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print(f"No puedes dividir por Cero: {e}")
    except TypeError as e:
        print(
            f"Existe un error de tipos, esto es debido a que alguno de los operandos no es un número: {e} "
        )


# div0(num1=10, num2=5)

"""
 DIFICULTAD EXTRA (opcional):
 Crea una función que sea capaz de procesar parámetros, pero que también
 pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 corresponderse con un tipo de excepción creada por nosotros de manera
 personalizada, y debe ser lanzada de manera manual) en caso de error.
 - Captura todas las excepciones desde el lugar donde llamas a la función.
 - Imprime el tipo de error.
 - Imprime si no se ha producido ningún error.
 - Imprime que la ejecución ha finalizado.
"""


class StrTypeError(Exception):
    pass


def process_params(params: list):
    if len(params) < 3:
        raise IndexError
    elif params[1] == 0:
        raise ZeroDivisionError
    elif any(isinstance(param, str) for param in params):
        raise StrTypeError("No puede haber ningun string")

    print(params[2])
    print(params[0] / params[1])
    print(params[2] + 5)


try:
    params = [1, 2, 3, 4]
    process_params(params)
except IndexError:
    print("La lista debe de ser superior o igual a 3 valores")
except ZeroDivisionError:
    print("El segundo elemento de la lista no puede ser un cero")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido Errores")
finally:
    print("El programa ha finalizado")
