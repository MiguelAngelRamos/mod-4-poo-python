from procesador import Procesador
from memoria_ram import MemoriaRam
from disco_duro import DiscoDuro
from computadora import Computadora


def main():
    procesador_intel = Procesador('Intel Core i7', 3.8)
    ram = MemoriaRam(16, 'DDR4')
    disco_duro_ssd = DiscoDuro(512, 'SSD')

    mi_pc = Computadora('Mi PC Gaming', procesador_intel, ram, disco_duro_ssd)

    print(mi_pc.especificaciones())
if __name__ == "__main__":
    main()

# Este es un ejemplo para ejercicio grupal 1