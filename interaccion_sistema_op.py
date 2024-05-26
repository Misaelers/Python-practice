import os

# Parte 1: Lectura y escritura de archivos
def leer_y_escribir_archivo():
    # Escribir en un archivo
    with open("archivo.txt", "w") as archivo:
        archivo.write("Hola, mundo!")
    
    # Leer el contenido del archivo
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:", contenido)

# Parte 2: Navegación por directorios
def navegar_por_directorios():
    # Obtener el directorio actual
    directorio_actual = os.getcwd()
    print("Directorio actual:", directorio_actual)
    
    # Listar archivos en el directorio actual
    archivos = os.listdir(directorio_actual)
    print("Archivos en el directorio actual:", archivos)

# Parte 3: Ejecución de comandos del sistema
def ejecutar_comandos():
    # Ejecutar el comando 'ls -l' en sistemas Unix o 'dir' en Windows
    if os.name == 'posix':
        comando = "ls -l"
    else:
        comando = "dir"
    
    resultado_comando = os.system(comando)
    print("Resultado del comando:", resultado_comando)

# Ejemplo de uso
if __name__ == "__main__":
    # Lectura y escritura de archivos
    leer_y_escribir_archivo()
    
    # Navegación por directorios
    navegar_por_directorios()
    
    # Ejecución de comandos del sistema
    ejecutar_comandos()
