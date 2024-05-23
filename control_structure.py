 # Estructuras condicionales 
numero = 10 
if numero > 0: 
    print("El número es positivo.") 
elif numero == 0: 
    print("El número es cero.") 
elif numero % 2 == 0:
    print("El número es par")
elif numero % 2 != 0:
    print("El número es impar")
else: 
    print("El número es negativo.") 
  
# Bucle for 
print("Bucle for:") 
for i in range(6): 
    print(i) 
  
# Bucle while 
print("Bucle while:") 
contador = 0 
while contador < 5: 
    print(contador) 
    contador += 1 
