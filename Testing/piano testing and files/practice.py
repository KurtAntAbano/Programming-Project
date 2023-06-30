import pygame
# Database of wav files




class note:
    def __init__(self, num, soundFile):
        self.number = num
        self.sound = soundFile
        # CONVERT STRING INTO FILENAME

    def note_C0(self):
        self.number.set("C_0")
        sound = pygame.mixer.Sound(self.sound)
        sound.play()
