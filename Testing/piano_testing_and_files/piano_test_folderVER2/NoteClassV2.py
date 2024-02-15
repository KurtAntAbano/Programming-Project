import pygame


class note:
    def __init__(self, num, instru, vol, oct, secoct, keysection):  # this class adopts the pianos attributes
        self.number = num
        self.instrument = instru
        self.volume = vol
        self.octave = oct
        self.secondoctave = secoct
        self.key = keysection

    def notePlay(self):  # this function uses attributes and string formatting to recall the correct wav file
        # noteSound = self.sound
        # if self.key == 1:
        #     octave = self.octave
        # else:
        #     octave = self.secondoctave
        self.playSound = pygame.mixer.Sound(f'wavsV2\\{self.instrument}\\octave{self.octave}\\{self.instrument}{self.number}.wav')
        self.playSound.play()

        self.playSound.set_volume(int(self.volume) / 10)

    def noteStop(self):
        self.playSound.stop()
        print("key has been released")
