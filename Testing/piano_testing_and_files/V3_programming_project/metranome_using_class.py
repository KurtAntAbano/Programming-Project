import threading
import time

import pygame


class metronome:
    def __init__(self, given_bpm, given_mode):
        self.bpm = given_bpm
        self.mode = given_mode

        pygame.init()
        self.delay = 60.0 /self.bpm  # Calculate the time interval in seconds

        # Initialize the audio mixer
        pygame.mixer.init()

        # Load your metronome sound file
        self.metronome_sound = pygame.mixer.Sound("metronome.wav")  # Replace with your sound file


    def play_metronome(self):
        while True:
            # pygame.event.post(pygame.event.Event(pygame.USEREVENT, {}))  # Post a custom event
            self.metronome_sound.play()
            time.sleep(self.delay)





