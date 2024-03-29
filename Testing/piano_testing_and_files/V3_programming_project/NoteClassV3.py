import pygame

pygame.mixer.init()
import threading

class note:
    def __init__(self, num, state, vol, oct, secoct, keysection, given_piano_object):  # this class adopts the pianos attributes
        self.number = num
        self.state = state
        self.volume = vol
        self.octave = oct
        self.secondoctave = secoct
        self.key =keysection
        self.piano_object = given_piano_object


        pygame.mixer.init()
        self.channel = self.piano_object.channel_to_use  # channel attribute now uses the channel_to_use attribute from the piano object

    def notePlay(self):  # this function uses attributes and string formatting to recall the correct wav file
        #noteSound = self.sound
        if self.key == 1:  # this if statement sees whether the key was prat of the first or second half of the piano this is to determine the ocatve
            octave = self.octave
        else:
            self.channel += 12
            octave = self.secondoctave
        self.playSound = pygame.mixer.Sound(f'wavsV3\\{self.state}\\octave{octave}\\{self.state}{self.number}.wav')
        #threading.Thread(target=self.playSound.play())
        # self.playSound.play()
        #
        #
        self.playSound.set_volume(int(self.volume)/10)

        channel = pygame.mixer.Channel(self.channel)
        # channels allow files to play independently of each other this will help avoid any slowdowns

        channel.play(self.playSound)

    def change_channel(self):
        self.piano_object.increment_channel()
        #  this method is from the note class it uses the piano object that was given and uses its method to increment the channel





    def noteStop(self):
        self.playSound.stop()
        print("key has been released")







