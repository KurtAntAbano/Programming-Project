import pygame


# Database of wav files


class note:
    def __init__(self, num, soundFile):
        self.number = num
        self.sound = soundFile
        # CONVERT STRING INTO FILENAME

    def notePlay(self):
        noteSound = self.sound
        playSound = pygame.mixer.Sound(noteSound)
        playSound.play()


if __name__ == "__main__":
    pygame.mixer.init()
    noteToplay = r'C:\Users\ka041\Programming-Project\Testing\piano testing and files\wav-piano-sound-master_wav_c1.wav'
    myObject = note("C_0", noteToplay)
    myObject.notePlay()

