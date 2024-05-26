import random

# Parte a: Generar números aleatorios
def generar_numeros_aleatorios(cantidad, rango_inicio, rango_fin):
    numeros = [random.randint(rango_inicio, rango_fin) for _ in range(cantidad)]
    return numeros

# Parte b: Utilizar estos números para simular experimentos y tomar decisiones
def simular_experimento():
    # Ejemplo de tirar un dado 10 veces
    resultados_dado = generar_numeros_aleatorios(10, 1, 6)
    print("Resultados de tirar un dado 10 veces:", resultados_dado)
    
    # Decisión basada en la media de los resultados
    media_resultados = sum(resultados_dado) / len(resultados_dado)
    print("Media de los resultados del dado:", media_resultados)
    
    if media_resultados > 3.5:
        decision = "La media es mayor que 3.5, tomamos la decisión A."
    else:
        decision = "La media es menor o igual a 3.5, tomamos la decisión B."
    
    print("Decisión tomada:", decision)

# Ejemplo de uso
if __name__ == "__main__":
    # Generar una lista de 5 números aleatorios entre 1 y 100
    numeros_aleatorios = generar_numeros_aleatorios(5, 1, 100)
    print("Números aleatorios generados:", numeros_aleatorios)
    
    # Simular un experimento basado en números aleatorios
    simular_experimento()
