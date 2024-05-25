# Creación de un array
mi_array = [1, 2, 3, 4, 5]

# Acceso a elementos del array
print("El primer elemento del array es:", mi_array[0])
print("El último elemento del array es:", mi_array[-1])

# Modificación de elementos del array
mi_array[2] = 10
print("Array después de modificar el tercer elemento:", mi_array)

# Recorrido del array
print("Recorrido del array:")
for elemento in mi_array:
    print(elemento)

# Agregar un elemento al final del array
mi_array.append(6)
print("Array después de agregar un nuevo elemento:", mi_array)

# Eliminar un elemento del array
elemento_eliminado = mi_array.pop(1)
print("Array después de eliminar el segundo elemento:", mi_array)
print("Elemento eliminado:", elemento_eliminado)

# Obtener la longitud del array
print("Longitud del array:", len(mi_array))

# Buscar un elemento en el array
elemento_buscado = 4
if elemento_buscado in mi_array:
    print(f"El elemento {elemento_buscado} está presente en el array.")
else:
    print(f"El elemento {elemento_buscado} no está presente en el array.")
