from audiofile import AudioFile

class MP3File(AudioFile):
    ext = "mp3"
    def reproducir(self):
        print("reproduciendo {} como mp3"
        .format(self.nombre_archivo))