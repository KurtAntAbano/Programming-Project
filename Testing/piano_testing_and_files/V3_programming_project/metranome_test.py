
import pygame
import time
import threading
class metronome:
    def __init__(self, given_bpm, given_mode):
        self.bpm = given_bpm
        self.mode = given_mode


    def playMetronome(self):
        print(float(self.bpm), "bpm")
        delay = 60/self.bpm
        count = 0
        beat = 0

        mode = 4
        multiple = 8

        while True:
            time.sleep(delay)

            # increment count after every wait and beat after ever 4 counts
            count += 1
            if count > mode:
                count = 1
                beat += 1

            # set metronome audio according to beat count
            playSound = pygame.mixer.Sound('metronome.wav')
            if count == 1:
                playSound = pygame.mixer.Sound('metronomeup.wav')
            pygame.mixer.Channel(1)
            t1 = threading.Thread(pygame.mixer.find_channel().play(playSound))
            t1.start()

            print(beat, count)

if __name__ == '__main__':
    pygame.mixer.init()
    mymetro = metronome(120, 4)
    mymetro.playMetronome()
