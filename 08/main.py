from mp3file import MP3File
from oggfile import OggFile
from wavfile import WavFile

def main():
    mp3 = MP3File("cancion.mp3")
    mp3.reproducir()
    
    wav = WavFile("sonido.wav")
    wav.reproducir()
    
    ogg = OggFile("musica.ogg")
    ogg.reproducir()
    
    

if __name__ == "__main__":
    main()