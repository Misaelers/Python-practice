# Encontrar el máximo de tres números
def maximo_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Ejemplo de uso
print("Máximo de tres números:", maximo_de_tres(10, 5, 8))

# Verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso
print("El número 7 es primo:", es_primo(7))
print("El número 10 es primo:", es_primo(10))

# Calcular la suma de una lista de números
def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso
print("Suma de la lista [1, 2, 3, 4, 5]:", suma_lista([1, 2, 3, 4, 5]))

# Ejemplo 5: Buscar un elemento en una lista
def buscar_elemento(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

# Ejemplo de uso
print("Buscar el elemento 3 en la lista [1, 2, 3, 4, 5]:", buscar_elemento([1, 2, 3, 4, 5], 3))
print("Buscar el elemento 6 en la lista [1, 2, 3, 4, 5]:", buscar_elemento([1, 2, 3, 4, 5], 6))

# Ejemplo 6: Calcular la media de una lista de números
def media_lista(lista):
    if len(lista) == 0:
        return 0
    return suma_lista(lista) / len(lista)

# Ejemplo de uso
print("La media de la lista [1, 2, 3, 4, 5]:", media_lista([1, 2, 3, 4, 5]))

# Ejemplo 7: Ordenar una lista de números (Método de la burbuja)
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Ejemplo de uso
print("Lista ordenada [5, 2, 9, 1, 5, 6]:", ordenar_lista([5, 2, 9, 1, 5, 6]))
