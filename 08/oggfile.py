from audiofile import AudioFile

class OggFile(AudioFile):
    ext = "ogg"
    def reproducir(self):
        print("reproduciendo {} como ogg"
        .format(self.nombre_archivo))