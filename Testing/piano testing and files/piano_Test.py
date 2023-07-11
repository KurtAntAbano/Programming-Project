from tkinter import *  # for python > 3.4
import tkinter as tk
from playNoteFunctions import *
from themeChanger import *

""" --__Midi0ke__--

First try for Midi0ke virtual piano for the midi-output.

Import pygame and tkinter in order to make a GUI for a piano-keyboard.

In the first piece of code I specify the functions for each note and the path for the .wav and
in the second I build the GUI for the piano-keyboard.

@author : Dead"""



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
        self.menubar = Menu(master)
        self.master.config(menu=self.menubar)

        # create a menu
        self.file_menu = Menu(self.menubar, tearoff=False)

        # add a menu item to the menu
        self.file_menu.add_command(label='Exit', command=master.destroy)

        # add the File menu to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.settings_menu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Settings", menu=self.settings_menu)

        self.settings_menu.add_command(label='Colour themes', command=lambda:themeChangeWindow(pianoFrame))
        self.settings_menu.add_command(label='Adjust piano size')


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


        def themeChanger(value):
            darkList = ['#5A5A5A', '#FFA500']
            highConTheme = ['#000000', '#028A0F']

            if value == "1":
                self.backgroundColour = darkList[0]
                self.labelColour = darkList[1]




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
