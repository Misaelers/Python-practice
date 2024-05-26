# Diccionario: almacenar información con clave-valor
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Conjunto: almacenar elementos únicos
mi_conjunto = {1, 2, 3, 4, 5}

# Ejemplos de manipulación de diccionarios
print("Diccionario original:", mi_diccionario)

# Acceder a un valor usando su clave
nombre = mi_diccionario["nombre"]
print("Nombre:", nombre)

# Modificar un valor
mi_diccionario["edad"] = 31
print("Diccionario después de modificar la edad:", mi_diccionario)

# Agregar un nuevo par clave-valor
mi_diccionario["profesión"] = "Ingeniero"
print("Diccionario después de agregar una profesión:", mi_diccionario)

# Eliminar un par clave-valor
del mi_diccionario["ciudad"]
print("Diccionario después de eliminar la ciudad:", mi_diccionario)

# Obtener todas las claves
claves = mi_diccionario.keys()
print("Claves del diccionario:", list(claves))

# Obtener todos los valores
valores = mi_diccionario.values()
print("Valores del diccionario:", list(valores))

# Obtener todos los pares clave-valor
items = mi_diccionario.items()
print("Pares clave-valor del diccionario:", list(items))

# Ejemplos de manipulación de conjuntos
print("Conjunto original:", mi_conjunto)

# Agregar un elemento al conjunto
mi_conjunto.add(6)
print("Conjunto después de agregar 6:", mi_conjunto)

# Eliminar un elemento del conjunto
mi_conjunto.remove(3)
print("Conjunto después de eliminar 3:", mi_conjunto)

# Comprobar si un elemento está en el conjunto
existe = 2 in mi_conjunto
print("¿El 2 está en el conjunto?", existe)

# Realizar la unión de dos conjuntos
otro_conjunto = {4, 5, 6, 7, 8}
union_conjuntos = mi_conjunto.union(otro_conjunto)
print("Unión de conjuntos:", union_conjuntos)

# Realizar la intersección de dos conjuntos
interseccion_conjuntos = mi_conjunto.intersection(otro_conjunto)
print("Intersección de conjuntos:", interseccion_conjuntos)

# Realizar la diferencia de dos conjuntos
diferencia_conjuntos = mi_conjunto.difference(otro_conjunto)
print("Diferencia de conjuntos:", diferencia_conjuntos)

# Limpiar el conjunto
mi_conjunto.clear()
print("Conjunto después de limpiarlo:", mi_conjunto)

# Mostrar el diccionario y el conjunto final
print("Diccionario final:", mi_diccionario)
print("Conjunto final:", mi_conjunto)