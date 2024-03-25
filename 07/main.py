from moto import Moto
from camion import Camion
# from vehiculo import Vehiculo

# vehiculo_poli = Vehiculo()
# vehiculo_poli = Moto()
# print(vehiculo_poli.arrancar())
# print(vehiculo_poli.detener())


# Son 2 métodos que van a reflejar el polimorfismo

def iniciar_vehiculo(vehiculo):
    print(vehiculo.arrancar())
    
def detener_vehiculo(vehiculo):
    print(vehiculo.detener())

moto = Moto()
camion = Camion()

# Moto
iniciar_vehiculo(moto)
detener_vehiculo(moto)

# Camion
iniciar_vehiculo(camion)
detener_vehiculo(camion)