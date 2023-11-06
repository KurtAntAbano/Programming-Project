
import pygame
import time
import threading
from tkinter import *
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


def metranome_win():
    win_theme = Tk()
    win_theme.title("Welcome")
    win_theme.geometry("350x100")

    dark_btn = Button(win_theme, text="dark", width=12)
    dark_btn.grid(row=1, column=1, padx=10, pady=10)


    mainloop()


if __name__ == '__main__':
    metranome_win()
    pygame.mixer.init()
    mymetro = metronome(120, 4)
    mymetro.playMetronome()
