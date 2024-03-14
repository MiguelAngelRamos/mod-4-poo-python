class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_informacion(self):
        print(f"El auto de marca: {self.marca} y modelo: {self.modelo}")

# Auto_Hyundai hereda de Auto
class Auto_Hyundai(Auto):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Clindrada: {self.cilindrada }")

auto_hyundai = Auto_Hyundai('Hyundai', 'Elantra', "1.8L")
auto_hyundai.mostrar_informacion()