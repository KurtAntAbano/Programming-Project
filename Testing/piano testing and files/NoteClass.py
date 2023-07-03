import pygame


# Database of wav files


class note:
    def __init__(self, num, soundFile, vol):
        self.number = num
        self.sound = soundFile
        self.volume = vol
        # CONVERT STRING INTO FILENAME

    def notePlay(self):
        noteSound = self.sound
        playSound = pygame.mixer.Sound(noteSound)
        playSound.play()

        playSound.set_volume(int(self.volume)/10)





