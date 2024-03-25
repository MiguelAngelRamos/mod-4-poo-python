from audiofile import AudioFile

class WavFile(AudioFile):
    ext = "wav"
    def reproducir(self):
        print("reproduciendo {} como wav"
        .format(self.nombre_archivo))