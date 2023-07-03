import wave
import pygame

obj = wave.open(r'C:\Users\ka041\Programming-Project\Testing\piano testing and files\wav-piano-sound-master_wav_a1.wav','rb')
sound = pygame.mixer.Sound(obj)
sound.play()