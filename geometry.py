# Ejemplo de Programación Basada en Funciones
# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
  return lado * lado
# Función para calcular el volumen de un cubo
def calcular_volumen_cubo(lado):
  return lado * lado * lado
# Función principal para mostrar resultados
def main():
  lado_cuadrado = 5
  lado_cubo = 3
  area = calcular_area_cuadrado(lado_cuadrado)
  volumen = calcular_volumen_cubo(lado_cubo)
  print("Área del cuadrado:", area)
  print("Volumen del cubo:", volumen)
if __name__ == "__main__":
  main()
