 
# Supongamos que el diagrama de flujo es para encontrar el máximo de tres números.  
 
def maximo_de_tres(a, b, c):  
    if a >= b and a >= c:  
        return a  
    elif b >= a and b >= c:  
        return b  
    else:  
        return c
 
# Ejemplo de uso  
print("Máximo de tres números:", maximo_de_tres(10, 5, 8))  
