from audiofile import AudioFile
class MP3File(AudioFile):
    ext = "mp3"
    def __init__(self, nombre_archivo):
        super().__init__(nombre_archivo)
        
 
    def reproducir(self):
        print("reproduciendo {} como mp3"
        .format(self.nombre_archivo))
