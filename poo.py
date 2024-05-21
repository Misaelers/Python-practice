# Ejemplo de Programación Orientada a Objetos (POO)
# Definición de la clase Cuadrado
class Cuadrado:
  def __init__(self, lado):
    self.lado = lado
  def calcular_area(self):
    return self.lado * self.lado
# Definición de la clase Cubo que hereda de Cuadrado
class Cubo(Cuadrado):
  def calcular_volumen(self):
    return self.lado * self.lado * self.lado

# Función principal para mostrar resultados
def main():
  lado_cuadrado = 5
  lado_cubo = 3
  
  cuadrado = Cuadrado(lado_cuadrado)
  area = cuadrado.calcular_area()
  print("Área del cuadrado:", area)
  
  cubo = Cubo(lado_cubo)
  volumen = cubo.calcular_volumen()
  
  print("Volumen del cubo:", volumen)
if __name__ == "__main__":
  main()
