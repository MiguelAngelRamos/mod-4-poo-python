from audiofile import AudioFile

class WavFile(AudioFile):
    ext = "wav"
    def __init__(self, nombre_archivo):
        super().__init__(nombre_archivo)
        
    def reproducir(self):
        print("reproduciendo {} como wav"
        .format(self.nombre_archivo))