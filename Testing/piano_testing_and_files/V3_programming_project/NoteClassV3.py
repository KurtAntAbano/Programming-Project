import pygame

pygame.mixer.init()
import threading

class note:
    def __init__(self, num, state, vol, oct, secoct, keysection):  # this class adopts the pianos attributes
        self.number = num
        self.state = state
        self.volume = vol
        self.octave = oct
        self.secondoctave = secoct
        self.key =keysection
        pygame.mixer.init()

    def notePlay(self):  # this function uses attributes and string formatting to recall the correct wav file
        #noteSound = self.sound
        if self.key == 1:
            octave = self.octave
        else:
            octave = self.secondoctave
        self.playSound = pygame.mixer.Sound(f'wavsV3\\{self.state}\\octave{octave}\\{self.state}{self.number}.wav')
        #threading.Thread(target=self.playSound.play())
        self.playSound.play()


        self.playSound.set_volume(int(self.volume)/10)



    def noteStop(self):
        self.playSound.stop()
        print("key has been released")






