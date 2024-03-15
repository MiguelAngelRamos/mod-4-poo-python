class Computadora:
    def __init__(self, nombre, procesador, ram, disco_duro):
        self.nombre = nombre
        self.procesador = procesador
        self.ram = ram
        self.disco_duro = disco_duro
    
    def especificaciones(self):
        return f"{self.nombre}\n{self.procesador}\n{self.ram}\n{self.disco_duro}\n"
