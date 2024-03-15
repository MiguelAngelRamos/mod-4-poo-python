class Procesador:
    def __init__(self, modelo, frencuencia):
        self.modelo = modelo
        self.frecuencia = frencuencia
    ## toString
    def __str__(self):
        return f"Procesador: {self.modelo}, {self.frecuencia}Ghz"