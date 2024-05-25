 
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

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)

# Obtener solo la hora actual
hora_actual = fecha_hora_actual.time()
print("Hora actual:", hora_actual)

# Crear una fecha y hora específicas
fecha_hora_especifica = datetime.datetime(2024, 12, 31, 23, 59, 59)
print("Fecha y hora específica:", fecha_hora_especifica)

# Formatear una fecha y hora
fecha_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
print("Fecha y hora formateada:", fecha_formateada)

# Parsear una cadena a un objeto datetime
cadena_fecha = "2024-12-31 23:59:59"
fecha_parseada = datetime.datetime.strptime(cadena_fecha, "%Y-%m-%d %H:%M:%S")
print("Fecha parseada:", fecha_parseada)

# Sumar días a una fecha
dias_a_sumar = datetime.timedelta(days=10)
nueva_fecha = fecha_actual + dias_a_sumar
print("Nueva fecha (10 días después):", nueva_fecha)

# Restar días a una fecha
dias_a_restar = datetime.timedelta(days=5)
fecha_resta = fecha_actual - dias_a_restar
print("Fecha (5 días antes):", fecha_resta)

# Comparar fechas
if fecha_actual < otra_fecha:
    print("La fecha actual es anterior a la otra fecha")
elif fecha_actual > otra_fecha:
    print("La fecha actual es posterior a la otra fecha")
else:
    print("Las fechas son iguales")

# Diferencia en segundos entre dos datetimes
diferencia_segundos = (fecha_hora_especifica - fecha_hora_actual).total_seconds()
print("Diferencia en segundos:", diferencia_segundos)

# Obtener el día de la semana (0 es lunes, 6 es domingo)
dia_semana = fecha_actual.weekday()
print("Día de la semana (0=lunes, ..., 6=domingo):", dia_semana)

# Obtener el nombre del día de la semana
nombres_dia_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
print("Nombre del día de la semana:", nombres_dia_semana[dia_semana])

# Obtener el primer día del mes
primer_dia_mes = fecha_actual.replace(day=1)
print("Primer día del mes:", primer_dia_mes)

# Obtener el último día del mes
ultimo_dia_mes = (primer_dia_mes + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
print("Último día del mes:", ultimo_dia_mes)

# Calcular la edad en años a partir de una fecha de nacimiento
fecha_nacimiento = datetime.date(1990, 6, 15)
hoy = datetime.date.today()
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
print("Edad en años:", edad)