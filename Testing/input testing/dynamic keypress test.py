import keyboard
keypress = False
key = 'space'
import pygame
pygame.mixer.init()

while True:
    sound = pygame.mixer.Sound("../c note.wav")
    if keyboard.is_pressed(key) and not keypress:
        sound.play()
        keypress = True        

    elif keypress and not keyboard.is_pressed(key):
        sound.stop()
        keypress = False
        break

