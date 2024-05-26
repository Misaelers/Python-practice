import multiprocessing

# Función para ejecutar en un proceso
def contar_hasta_diez():
    for i in range(1, 11):
        print(i)

if __name__ == "__main__":
    # Crear y ejecutar un proceso
    proceso = multiprocessing.Process(target=contar_hasta_diez)
    proceso.start()

    # El programa principal continúa ejecutándose mientras el proceso cuenta hasta diez
    print("El programa principal sigue ejecutándose")
