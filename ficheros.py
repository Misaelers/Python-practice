# Escritura en un fichero
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.write("Esta es una línea adicional.\n")
    archivo.write("Añadimos otra línea.\n")
print("Escritura completada.\n")

# Lectura de un fichero
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
print("Lectura completada.\n")

# Recorrido secuencial de un fichero
with open("archivo.txt", "r") as archivo:
    linea = archivo.readline()
    print("Recorrido secuencial del fichero:")
    while linea:
        print("Línea:", linea.strip())  # Eliminar el salto de línea al final
        linea = archivo.readline()
print("Recorrido secuencial completado.\n")

# Escritura adicional en el fichero
with open("archivo.txt", "a") as archivo:
    archivo.write("Nueva línea agregada al final del fichero.\n")
print("Escritura adicional completada.\n")

# Lectura línea por línea con un bucle for
with open("archivo.txt", "r") as archivo:
    print("Lectura línea por línea usando un bucle for:")
    for linea in archivo:
        print("Línea:", linea.strip())  # Eliminar el salto de línea al final
print("Lectura con bucle for completada.\n")

# Contar el número de líneas en el fichero
with open("archivo.txt", "r") as archivo:
    num_lineas = sum(1 for _ in archivo)
print(f"El fichero tiene {num_lineas} líneas.\n")
