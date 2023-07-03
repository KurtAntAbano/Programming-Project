import pygame


def note_C0():
    #num1.set("C_0")
    note = r'C:\Users\ka041\Programming-Project\Testing\piano testing and files\wav-piano-sound-master_wav_c1.wav'
    sound = pygame.mixer.Sound(note)
    sound.play()

pygame.mixer.init()
x = input("input")
if x == "y":
    note_C0()