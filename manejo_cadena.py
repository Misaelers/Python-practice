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
