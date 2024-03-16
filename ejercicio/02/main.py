from procesador import Procesador
from memoria_ram import MemoriaRam
from disco_duro import DiscoDuro
from computadora import Computadora


def main():
    # UN PC
    procesador_intel = Procesador('Intel Core i7', 3.8)
    ram = MemoriaRam(16, 'DDR4')
    disco_duro_ssd = DiscoDuro(512, 'SSD')

    mi_pc = Computadora('Mi PC Gaming', procesador_intel, ram, disco_duro_ssd)


    # UN MACBOOK
    procesador_apple_silicon = Procesador('M1 pro', 3.2)
    ram_unificada = MemoriaRam(16, 'unificada')
    disco_duro_ssd_mac = DiscoDuro(512, 'SSD')

    mac = Computadora('Macbook Pro', procesador_apple_silicon, ram_unificada, disco_duro_ssd_mac)


    print(mi_pc.especificaciones()) # el pc
    print(mac.especificaciones()) # Mac
    
if __name__ == "__main__":
    main()

# Este es un ejemplo para ejercicio grupal 1