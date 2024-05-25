# Función recursiva para calcular el factorial de un número  
def factorial(n):  
    if n == 0:  
        return 1  
    else:  
        return n * factorial(n - 1)  
 
# Ejemplo de uso  
resultado = factorial(6)  
print("El factorial de 6:", resultado)  

# Función recursiva para calcular el Fibonacci de un número
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso
numero = 6
resultado = fibonacci(numero)
print(f"El Fibonacci de {numero}:", resultado)