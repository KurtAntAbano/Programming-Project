import pygame


# Database of wav files


class note:
    def __init__(self, num, soundFile):
        self.number = num
        self.sound = soundFile
        # CONVERT STRING INTO FILENAME

    def notePlay(self):
        print(self.sound)
        sound = pygame.mixer.Sound(self.sound)
        sound.play()


if __name__ == "__main__":
    pygame.mixer.init()
    myObject = note("C_0",
                    r'C:\Users\ka041\Programming-Project\Testing\piano testing and files\wav-piano-sound-master_wav_a1s.wav')
    myObject.notePlay()

    sound = pygame.mixer.Sound('wav-piano-sound-master_wav_a1s.wav')
    sound.play()


