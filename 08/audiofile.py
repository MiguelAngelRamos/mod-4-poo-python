class AudioFile:
    def __init__(self, nombre_archivo):
        if not nombre_archivo.endswith(self.ext):
            raise Exception("formato de archivo invalido")
        self.nombre_archivo = nombre_archivo