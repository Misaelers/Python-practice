# Manipulación de cadenas de caracteres en Python  

cadena = "Hola, mundo!"  
 
# Longitud de la cadena  
print("Longitud de la cadena:", len(cadena))  
 
# Acceso a caracteres individuales  
print("Primer carácter:", cadena[0])  
print("Último carácter:", cadena[-1])  
 
# Subcadenas  
print("Subcadena:", cadena[0:4])  
 
# Concatenación  
otra_cadena = " Adiós!"  
concatenacion = cadena + otra_cadena  
print("Concatenación:", concatenacion)  
 
# Búsqueda de subcadenas  
print("Posición de 'mundo':", cadena.find("mundo"))  

# Reemplazo de subcadenas
cadena_reemplazada = cadena.replace("mundo", "Python")
print("Cadena reemplazada:", cadena_reemplazada)

# Conversión a mayúsculas y minúsculas
print("Mayúsculas:", cadena.upper())
print("Minúsculas:", cadena.lower())

# Eliminación de espacios en blanco al inicio y al final
cadena_con_espacios = "  Hola, mundo!  "
print("Sin espacios al inicio y al final:", cadena_con_espacios.strip())

# División de cadenas
cadena_dividida = cadena.split(", ")
print("Cadena dividida:", cadena_dividida)

# Comprobación de prefijo y sufijo
print("Empieza con 'Hola':", cadena.startswith("Hola"))
print("Termina con 'mundo!':", cadena.endswith("mundo!"))

# Formateo de cadenas
nombre = "Juan"
edad = 30
formateo = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print("Formateo de cadena:", formateo)

# Uso de join para concatenar elementos de una lista
lista_palabras = ["Hola", "mundo", "desde", "Python"]
cadena_unida = " ".join(lista_palabras)
print("Cadena unida:", cadena_unida)

# Repetición de cadenas
cadena_repetida = cadena * 3
print("Cadena repetida:", cadena_repetida)
