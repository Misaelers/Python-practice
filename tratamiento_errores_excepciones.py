try:
    # Intentar ejecutar código que puede generar una excepción
    valor = int(input("Ingrese un número: "))
    resultado = 10 / valor
except ValueError:
    # Capturar la excepción específica de valor incorrecto
    print("Error: ¡Debe ingresar un número válido!")
except ZeroDivisionError:
    # Capturar la excepción específica de división por cero
    print("Error: ¡No se puede dividir entre cero!")
else:
    # Bloque que se ejecuta si no se generó ninguna excepción
    print("El resultado de la división es:", resultado)
finally:
    # Bloque opcional que se ejecuta siempre, independientemente de si se generó una excepción o no
    print("Fin del bloque try-except")
