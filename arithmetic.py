def sumar(a,b):
  return a+b

def restar(a,b):
  return a-b

def multiplicar(a,b):
  return a*b

def dividir(a,b):
  return a/b

# Función principal
def main():
  a = float(input("Ingrese el primer número: "))
  b = float(input("Ingrese el segundo número: "))
  
  operacion = input("¿Qué operación desea realizar? (+ para suma, - para resta, * para multiplicación, / para división): ")
  
  if operacion == '+':
    resultado = sumar(a, b)
  elif operacion == '-':
    resultado = restar(a, b)
  elif operacion == '*':
    resultado = multiplicar(a, b)
  elif operacion == '/':
    resultado = dividir(a, b)
  else:
    resultado = "Operación no válida."
  print("El resultado es:", resultado)
# Llamada a la función principal
main()