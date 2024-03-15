class MemoriaRam:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo
    def __str__(self):
        return f"Memoria RAM: {self.capacidad}GB, {self.tipo}"