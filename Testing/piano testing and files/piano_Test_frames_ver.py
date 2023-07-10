from tkinter import *  # for python > 3.4
import tkinter as tk
import pygame
from NoteClass import *

""" --__Midi0ke__--

First try for Midi0ke virtual piano for the midi-output.

Import pygame and tkinter in order to make a GUI for a piano-keyboard.

In the first piece of code I specify the functions for each note and the path for the .wav and
in the second I build the GUI for the piano-keyboard.

@author : Dead"""


def note_C0(soundObj):
    if soundObj.state.get() == "Piano":
        noteToplay = r'wav-piano-sound-master_wav_c1.wav'
    else:
        noteToplay = r'56111__guitarmaster__c-note.wav'
    noteObject = note("C_0", noteToplay, soundObj.volume)
    noteObject.notePlay()
    mainWindow.bind("<c>", noteObject.notePlay())


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


class MyPianoGUI:
    def __init__(self, master):
        self.master = master
        self.state = "Piano"
        self.volume = 90
        self.backgroundColour = "#F0F0F0"
        self.labelColour = '#856ff8'

        self.pianoFrame = Frame(self.master)
        self.pianoFrame.pack(side='bottom', fill="both", expand=True, pady=5, padx=5, ipadx=10, ipady=10)

        self.controlFrame = Frame(self.master)
        self.controlFrame.pack(side="top", fill="both", expand=True, padx=5, pady=5, ipadx=10, ipady=10)

        #https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/

        master.title("Midi0ke__piano_GUI")
        master['background'] = self.backgroundColour

        # create a menubar
        menubar = Menu(master)
        master.config(menu=menubar)

        # create a menu
        file_menu = Menu(menubar, tearoff=False)

        # add a menu item to the menu
        file_menu.add_command(label='Exit', command=master.destroy)

        # add the File menu to the menubar
        menubar.add_cascade(label="File", menu=file_menu)

        settings_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Settings", menu=settings_menu)

        settings_menu.add_command(label='Colour themes')
        settings_menu.add_command(label='Adjust piano size')

        self.Label = Label(self.pianoFrame, text="MIDIOKE", fg=self.labelColour)
        self.Label.grid(row=0, columnspan=11)

        # Buttons for keyboard
        self.C_0_button = Button(self.pianoFrame, bg="white", text="C_0", command=lambda: note_C0(pianoFrame), height=10, width=6)
        self.C_0_button.grid(row=5, column=0)
        self.master.bind('<c>', lambda event: note_C0(pianoFrame))

        self.CC_0_button = Button(self.pianoFrame, bg="black", fg="white", text="C#_0", command=note_CC0, height=10, width=4)
        self.CC_0_button.grid(row=1, columnspan=2)

        self.DD_0_button = Button(self.pianoFrame, bg="black", fg="white", text="D#_0", command=note_DD0, height=10, width=4)
        self.DD_0_button.grid(row=1, columnspan=4)

        self.D_0_button = Button(self.pianoFrame, bg="white", text="D_0", command=note_D0, height=10, width=6)
        self.D_0_button.grid(row=5, column=1)

        self.E_0_button = Button(self.pianoFrame, bg="white", text="E_0", command=note_E0, height=10, width=6)
        self.E_0_button.grid(row=5, column=2)

        self.F_0_button = Button(self.pianoFrame, bg="white", text="F_0", command=note_F0, height=10, width=6)
        self.F_0_button.grid(row=5, column=3)

        self.FF_0_button = Button(self.pianoFrame, bg="black", fg="white", text="F#_0", command=note_FF0, height=10, width=4)
        self.FF_0_button.grid(row=1, column=3, columnspan=2)

        self.G_0_button = Button(self.pianoFrame, bg="white", text="G_0", command=note_G0, height=10, width=4)
        self.G_0_button.grid(row=5, column=4)

        self.GG_0_button = Button(self.pianoFrame, bg="black", fg="white", text="G#_0", command=note_GG0, height=10, width=4)
        self.GG_0_button.grid(row=1, column=4, columnspan=2)

        self.A_0_button = Button(self.pianoFrame, bg="white", text="A_0", command=note_A0, height=10, width=6)
        self.A_0_button.grid(row=5, column=5)

        self.AA_0_button = Button(self.pianoFrame, bg="black", fg="white", text="A#_0", command=note_AA0, height=10, width=4)
        self.AA_0_button.grid(row=1, column=5, columnspan=2)

        self.B_0_button = Button(self.pianoFrame, bg="white", text="B_0", command=note_B0, height=10, width=6)
        self.B_0_button.grid(row=5, column=6)

        # -----------------------------------------------------------------------------------------------------

        def print_selection(v):
            self.volume = v
            self.sliderLabel.config(text='you have selected ' + v)

        self.volumeSlider = tk.Scale(self.controlFrame, label='VOLUME', from_=0, to=10, orient=tk.HORIZONTAL, length=200,
                                     tickinterval=1, resolution=1, command=print_selection)
        self.volumeSlider.grid(row=5, column=8)
        self.volumeSlider.set(5)

        self.sliderLabel = tk.Label(self.controlFrame, bg='white', fg='black', width=20, text='empty')
        self.sliderLabel.grid(row=6, column=8)

        def update_btn_text():
            if self.state.get() == "Piano":
                self.state.set("Guitar")
            else:
                self.state.set("Piano")

        self.state = tk.StringVar()
        self.state_btn = tk.Button(self.controlFrame, textvariable=self.state, command=update_btn_text)
        self.state.set("Piano")
        self.state_btn.grid(row=5, column=7)

        self.Label = Label(self.controlFrame, text="change\n state")
        self.Label.grid(row=6, column=7)


class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Main Window')
        self.geometry('400x500')


mainWindow = main_window()
pianoFrame = MyPianoGUI(mainWindow)
num1 = StringVar()
pygame.mixer.init()

mainWindow.mainloop()
