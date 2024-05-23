# Manejo de excepciones en Python utilizando bloques try, except y finally  
 
try:  
    # Intentar ejecutar código que puede generar una excepción  
    resultado = 10 / 0  
except ZeroDivisionError:  
    # Capturar una excepción específica  
    print("Error: división por cero")  
finally:  
    # Bloque opcional que se ejecuta siempre, independientemente de si se generó una excepción o no  
    print("Fin del bloque try-except")  
