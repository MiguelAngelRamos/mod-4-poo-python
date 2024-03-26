from audiofile import AudioFile

class OggFile(AudioFile):
    ext = "ogg"
    def __init__(self, nombre_archivo):
        super().__init__(nombre_archivo)
    def reproducir(self):
        print("reproduciendo {} como ogg"
        .format(self.nombre_archivo))