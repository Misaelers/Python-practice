
# Escritura en un fichero  
with open("archivo.txt", "w") as archivo:  
    archivo.write("Hola, mundo!\n")  
    archivo.write("Esta es una línea adicional.\n")  
 
# Lectura de un fichero  
with open("archivo.txt", "r") as archivo:  
    contenido = archivo.read()  
    print("Contenido del archivo:")
    print(contenido)  
 
# Recorrido secuencial de un fichero  
with open("archivo.txt", "r") as archivo:  
    linea = archivo.readline()  
    while linea:  
        print("Línea:", linea.strip())  # Eliminar el salto de línea al final  
        linea = archivo.readline()  
