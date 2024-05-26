# Clase base
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base
    
    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, Salario: {self.calcular_salario()}")

# Subclase para Empleados a Tiempo Completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bonificacion):
        super().__init__(nombre, salario_base)
        self.bonificacion = bonificacion
    
    def calcular_salario(self):
        return self.salario_base + self.bonificacion

# Subclase para Empleados a Medio Tiempo
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, salario_base, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora
    
    def calcular_salario(self):
        return self.salario_base + (self.horas_trabajadas * self.pago_por_hora)

# Polimorfismo
def mostrar_salario_empleado(empleado):
    empleado.mostrar_informacion()

# Creación de objetos
empleado_fulltime = EmpleadoTiempoCompleto("Ana", 3000, 500)
empleado_parttime = EmpleadoMedioTiempo("Luis", 1500, 20, 20)

# Uso de polimorfismo
mostrar_salario_empleado(empleado_fulltime)  # Imprimirá "Empleado: Ana, Salario: 3500"
mostrar_salario_empleado(empleado_parttime)  # Imprimirá "Empleado: Luis, Salario: 1900"
