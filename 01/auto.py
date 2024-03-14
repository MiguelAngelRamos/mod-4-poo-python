class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_descripcion(self):
        print(f"Este auto es un {self.modelo} de {self.marca}.")

  
# Mi primera instancia "mi_auto" es un objeto de la clase Auto
mi_auto = Auto("Toyota", "Corolla")
print(mi_auto.marca) # Toyota
print(mi_auto.modelo) # Corolla
mi_auto.mostrar_descripcion()
# Segunda instancia "mi_auto_2" es un objeto de la clase Auto
mi_auto_2 = Auto("Hyundai", "Elantra")
print(mi_auto_2.marca)
print(mi_auto_2.modelo)
mi_auto_2.mostrar_descripcion()
