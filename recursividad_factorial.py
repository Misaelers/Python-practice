# Función recursiva para calcular el factorial de un número  
def factorial(n):  
    if n == 0:  
        return 1  
    else:  
        return n * factorial(n - 1)  
 
# Ejemplo de uso  
resultado = factorial(6)  
print("El factorial de 6:", resultado)  
