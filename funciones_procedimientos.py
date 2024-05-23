#Funciones con parámetros  
def div(a, b):  
    return a / b  
def mult(c, d):  
    return c * d  
 
print("Funciones con parámetros:")  
print("División:", div(10, 2))  
print("Multiplicación:", mult(2, 3))  
 
# Funciones sin parámetros  
def saludo():  
    print("¡Hola mundo!")  
saludo()  
 
# Parámetros por valor y por referencia  
def modificar_lista(lista):  
    lista.append('gato')  
    lista.pop(2)
animales = ['perro','camello', 'jirafa', 'ornitorrinco']  
modificar_lista(animales)  
print("Lista modificada:", animales)  # Se ha modificado mi la lista de animales

    
  
