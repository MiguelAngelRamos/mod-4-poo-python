from instrumentos import Bateria, Guitarra, Violin

# instrumento = Instrumento()
# bateria_1 = Bateria()
# instrumento = bateria_1
# print(instrumento.tocar())
# Polimorfismo
def tocar_instrumento(instrumento):
    print(instrumento.tocar())

guitarra = Guitarra()
bateria = Bateria()
violin = Violin()

tocar_instrumento(guitarra)
tocar_instrumento(bateria)
tocar_instrumento(violin)

