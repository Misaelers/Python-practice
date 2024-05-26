# Ejemplos de trabajo con listas y tuplas

# Listas: mutables
mi_lista = [1, 2, 3]

# Agregar un elemento al final de la lista
mi_lista.append(4)
# Modificar el primer elemento de la lista
mi_lista[0] = 0

# Mostrar la lista modificada
print("Lista modificada:", mi_lista)

# Tuplas: inmutables
mi_tupla = (1, 2, 3)

# Intentar modificar la tupla generará un error
# mi_tupla.append(4)  # Esto generaría un error, las tuplas no pueden ser modificadas
# mi_tupla[0] = 0     # Esto generaría un error, las tuplas no pueden ser modificadas

# Mostrar la tupla original
print("Tupla original:", mi_tupla)

# Diferencia entre listas y tuplas
# Las listas pueden ser modificadas después de su creación
# Las tuplas no pueden ser modificadas después de su creación

# Uso en distintos contextos
# Por ejemplo, las tuplas pueden ser utilizadas como claves en un diccionario debido a su inmutabilidad
diccionario = {(1, 2): "valor"}
print("Valor asociado a la tupla en el diccionario:", diccionario[(1, 2)])

# Más ejemplos de operaciones con listas
otra_lista = [5, 6, 7, 8]

# Concatenar dos listas
lista_concatenada = mi_lista + otra_lista
print("Listas concatenadas:", lista_concatenada)

# Insertar un elemento en una posición específica
mi_lista.insert(2, 'insertado')
print("Lista después de la inserción:", mi_lista)

# Eliminar un elemento por valor
mi_lista.remove('insertado')
print("Lista después de la eliminación:", mi_lista)

# Eliminar un elemento por índice
eliminado = mi_lista.pop(1)
print("Elemento eliminado:", eliminado)
print("Lista después de pop:", mi_lista)

# Más ejemplos de operaciones con tuplas
otra_tupla = (4, 5, 6)

# Concatenar dos tuplas
tupla_concatenada = mi_tupla + otra_tupla
print("Tuplas concatenadas:", tupla_concatenada)

# Acceder a elementos de una tupla
primer_elemento = mi_tupla[0]
print("Primer elemento de la tupla:", primer_elemento)

# Desempaquetar una tupla
a, b, c = mi_tupla
print("Desempaquetado de la tupla:", a, b, c)

# Intentar modificar una tupla genera un error
# mi_tupla[1] = 10  # Esto generaría un error

# Comprobar si un elemento está en una tupla
existe = 2 in mi_tupla
print("¿El 2 está en la tupla?", existe)
