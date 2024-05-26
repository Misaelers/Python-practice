import os
import random
import unittest

# Funciones a probar

def generar_numeros_aleatorios(cantidad, rango_inicio, rango_fin):
    return [random.randint(rango_inicio, rango_fin) for _ in range(cantidad)]

def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return archivo.read()

def obtener_directorio_actual():
    return os.getcwd()

def listar_archivos(directorio):
    return os.listdir(directorio)

def ejecutar_comando_ls():
    comando = "ls -l" if os.name == 'posix' else "dir"
    return os.system(comando)

# Clase de prueba

class TestMiModulo(unittest.TestCase):
    
    def test_generar_numeros_aleatorios(self):
        numeros = generar_numeros_aleatorios(5, 1, 100)
        self.assertEqual(len(numeros), 5)
        for numero in numeros:
            self.assertTrue(1 <= numero <= 100)

    def test_escribir_y_leer_archivo(self):
        nombre_archivo = "test_archivo.txt"
        contenido = "Hola, mundo!"
        escribir_archivo(nombre_archivo, contenido)
        contenido_leido = leer_archivo(nombre_archivo)
        self.assertEqual(contenido, contenido_leido)
        os.remove(nombre_archivo)

    def test_obtener_directorio_actual(self):
        directorio_actual = obtener_directorio_actual()
        self.assertTrue(os.path.isdir(directorio_actual))

    def test_listar_archivos(self):
        directorio_actual = obtener_directorio_actual()
        archivos = listar_archivos(directorio_actual)
        self.assertIsInstance(archivos, list)

    def test_ejecutar_comando_ls(self):
        resultado_comando = ejecutar_comando_ls()
        self.assertEqual(resultado_comando, 0)

# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main()
