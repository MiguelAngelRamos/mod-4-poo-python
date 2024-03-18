class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamento = None
    
    def asignar_departamento(self, departamento):
        self.departamento = departamento
        departamento.empleados.append(self)