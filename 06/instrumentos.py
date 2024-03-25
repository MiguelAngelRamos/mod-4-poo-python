class Instrumento:
    def tocar(self):
        pass
    
class Bateria(Instrumento):
    def tocar(self):
        return "Boom Bom tac tac splis splis"
    
class Guitarra(Instrumento):
    def tocar(self):
        return "Trinn"
    
class Violin(Instrumento):
    def tocar(self):
        return "iiiiih"
