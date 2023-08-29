import pygame


class note:
    def __init__(self, num, state, vol, oct):
        self.number = num
        self.state = state
        self.volume = vol
        self.octave = oct

    def notePlay(self):
        #noteSound = self.sound
        playSound = pygame.mixer.Sound(f'wavs\\{self.state}\\octave{self.octave}\\{self.state}{self.number}.wav')
        playSound.play()

        playSound.set_volume(int(self.volume)/10)





