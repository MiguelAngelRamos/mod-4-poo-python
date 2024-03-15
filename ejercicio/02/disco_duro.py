class DiscoDuro:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo
    
    def __str__(self):
        return f"Disco Duro: {self.capacidad}GB, {self.tipo}"