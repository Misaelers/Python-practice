from enum import Enum

a = 2 # Entero
b = -2.2 # Real
c = 'l' # Caracter
d = (2, 3, 4, 5) # Lista de tipo Tupla
e = ['pera', 'manzana', 'piña', 'mango'] # Array
f = True # Booleano
g = 1j # Complejo
Dicc = {'a' : 'bueno',
    'b' : 'malo'
}  # Estructura (Deccionario)
Semana = Enum(
    value='Semana',
    names=('LU MA MI JU VI SA DO'),
) # Enumerado
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(Dicc))
for dia in Semana:
    print(dia.name, '<->', dia.value)