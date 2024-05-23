 
import datetime  
# Obtener la fecha actual  
fecha_actual = datetime.date.today()  
print("Fecha actual:", fecha_actual)  
 
# Crear una fecha específica  
otra_fecha = datetime.date(2024, 12, 31)  
print("Otra fecha:", otra_fecha)  
 
# Operaciones con fechas  
diferencia = otra_fecha - fecha_actual  
print("Diferencia de días:", diferencia.days)  
