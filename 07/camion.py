from vehiculo import Vehiculo

class Camion(Vehiculo):
    def arrancar(self):
        return "La Camion está arrancando..."
    def detener(self):
        return "La Camion está deteniéndose..."