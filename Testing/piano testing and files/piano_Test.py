from tkinter import *  # for python > 3.4
import tkinter as tk
import pygame
from practice import *
""" --__Midi0ke__--

First try for Midi0ke virtual piano for the midi-output.

Import pygame and tkinter in order to make a GUI for a piano-keyboard.

In the first piece of code I specify the functions for each note and the path for the .wav and
in the second I build the GUI for the piano-keyboard.

@author : Dead"""


def note_C0(soundObj):
    # num1.set("C_0")
    # note = r'C:\Users\ka041\Programming-Project\Testing\piano testing and files\wav-piano-sound-master_wav_c1.wav'
    # sound = pygame.mixer.Sound(note)
    # sound.play()
    # # create object
    # # pass parameters
    # # play method to play sound

    if soundObj.state.get() == "Piano":
        noteToplay = r'C:\Users\ka041\Programming-Project\Testing\piano testing and files\wav-piano-sound-master_wav_c1.wav'
    else:
        noteToplay = r'C:\Users\ka041\Programming-Project\Testing\piano testing and files\56111__guitarmaster__c-note.wav'
    noteObject = note("C_0", noteToplay)
    noteObject.notePlay()

def note_CC0():
    num1.set("C#_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_c1s.wav")
    sound.play()


def note_D0():
    num1.set("D_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_d1.wav")
    sound.play()


def note_DD0():
    num1.set("D#_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_d1s.wav")
    sound.play()


def note_E0():
    num1.set("E_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_e1.wav")
    sound.play()


def note_F0():
    num1.set("F_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_f1.wav")
    sound.play()


def note_FF0():
    num1.set("F#_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_f1s.wav")
    sound.play()


def note_G0():
    num1.set("G_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_g1.wav")
    sound.play()


def note_GG0():
    num1.set("G#_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_g1s.wav")
    sound.play()


def note_A0():
    num1.set("A_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_a1.wav")
    sound.play()


def note_AA0():
    num1.set("A#_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_a1s.wav")
    sound.play()


def note_B0():
    num1.set("B_0")
    sound = pygame.mixer.Sound("wav-piano-sound-master_wav_b1.wav")
    sound.play()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.state = "Piano"
        master.title("Midi0ke__piano_GUI")

        self.Label = Label(master, text="MIDIOKE")
        self.Label.grid(row=0, columnspan=11)

        # Buttons for keyboard
        self.C_0_button = Button(master, bg="white", text="C_0", command= lambda: note_C0(myPiano), height=10, width=3)

        self.C_0_button.grid(row=5, column=0)

        self.CC_0_button = Button(master, bg="black", fg="white", text="C#_0", command=note_CC0, height=10, width=2)
        self.CC_0_button.grid(row=1, columnspan=2)

        self.DD_0_button = Button(master, bg="black", fg="white", text="D#_0", command=note_DD0, height=10, width=2)
        self.DD_0_button.grid(row=1, columnspan=4)

        self.D_0_button = Button(master, bg="white", text="D_0", command=note_D0, height=10, width=3)
        self.D_0_button.grid(row=5, column=1)

        self.E_0_button = Button(master, bg="white", text="E_0", command=note_E0, height=10, width=3)
        self.E_0_button.grid(row=5, column=2)

        self.F_0_button = Button(master, bg="white", text="F_0", command=note_F0, height=10, width=3)
        self.F_0_button.grid(row=5, column=3)

        self.FF_0_button = Button(master, bg="black", fg="white", text="F#_0", command=note_FF0, height=10, width=2)
        self.FF_0_button.grid(row=1, column=3, columnspan=2)

        self.G_0_button = Button(master, bg="white", text="G_0", command=note_G0, height=10, width=3)
        self.G_0_button.grid(row=5, column=4)

        self.GG_0_button = Button(master, bg="black", fg="white", text="G#_0", command=note_GG0, height=10, width=2)
        self.GG_0_button.grid(row=1, column=4, columnspan=2)

        self.A_0_button = Button(master, bg="white", text="A_0", command=note_A0, height=10, width=3)
        self.A_0_button.grid(row=5, column=5)

        self.AA_0_button = Button(master, bg="black", fg="white", text="A#_0", command=note_AA0, height=10, width=2)
        self.AA_0_button.grid(row=1, column=5, columnspan=2)

        self.B_0_button = Button(master, bg="white", text="B_0", command=note_B0, height=10, width=3)
        self.B_0_button.grid(row=5, column=6)

  # -----------------------------------------------------------------------------------------------------


        def update_btn_text():
            if self.state.get() == "Piano":
                self.state.set("Guitar")
            else:
                self.state.set("Piano")

        self.state = tk.StringVar()
        self.state_btn = tk.Button(root, textvariable=self.state, command=update_btn_text)
        self.state.set("Piano")
        self.state_btn.grid(row=5, column=7)

        self.Label = Label(master, text="change\n state")
        self.Label.grid(row=6, column=7)


root = Tk()
myPiano = MyFirstGUI(root)
num1 = StringVar()
pygame.mixer.init()

root.mainloop()
