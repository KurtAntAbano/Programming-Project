
from future.moves.tkinter import messagebox

# 15/09/23
from playNoteFunctionsV3 import *
from song_string_conversion import *
from SQL_teacherV2 import *
import tkinter as tk
from tkinter import *
from SQL_teacherV2 import studentProject
from Project_loginUI_windows import *
import pygame as pygame
from PIL import ImageTk, Image
import time

""" --__Midi0ke__--

First try for Midi0ke virtual piano for the midi-output.

Import pygame and tkinter in order to make a GUI for a piano-keyboard.

In the first piece of code I specify the functions for each note and the path for the .wav and
in the second I build the GUI for the piano-keyboard.

@author : Dead"""



class MyPianoGUI:
    def __init__(self, master, givenUserID, givenName):

        self.song_db = studentProject()
        self.song_db.createTable()

        self.user = givenUserID
        self.name = givenName
        self.master = master
        self.volume = 90
        self.backgroundColour = '#d8d8d8'  # '#5A5A5A'
        self.labelColour = '#856ff8'
        self.frameColour = '#F0F0F0'
        self.label_background_colour = "white"
        self.octave = 0
        self.secondoctave = 1
        self.recording = False
        self.input_string = []
        self.previous_time = 0
        # self.noteShow = ''
        # self.noteShow = tk.StringVar()
        self.noteColour1 = 'black'
        self.noteColour2 = 'white'
        self.channel_to_use = 0

        self.master.resizable(0, 0)

        self.pianoFrame = Frame(self.master)
        self.pianoFrame.pack(side='bottom', fill="none", expand=True, pady=5, padx=5, ipadx=10, ipady=10)
        self.pianoFrame.configure(bg=self.frameColour)

        self.octaveframe = Frame(self.master)
        self.octaveframe.pack(side='right', fill="both", expand=False, pady=5, padx=5, ipadx=10, ipady=10)

        self.controlFrame = Frame(self.master)
        self.controlFrame.pack(side="left", fill="both", expand=True, padx=5, pady=5, ipadx=10, ipady=10)
        self.controlFrame.configure(bg=self.frameColour)

        self.recordFrame = Frame(self.master)
        self.recordFrame.pack(side='left', fill="both", expand=True, pady=5, padx=5, ipadx=0, ipady=0)

        # https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/

        master.title("piano GUI")
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

        self.settings_menu.add_command(label='Colour themes', command=lambda: themeChangeWindow(self))

        self.help_menu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label='Commonly Asked Questions ', command=lambda: QandA_window())
        self.help_menu.add_command(label='Piano Guide', command=lambda: piano_guide_window())

        self.mainLabel = Label(self.pianoFrame, text="VIRTU-PIANO", fg=self.labelColour)
        self.mainLabel.grid(row=0, columnspan=11)

        def colourChange(btn):
            btn.configure(bg="green")
            time.sleep(0.5)
            print("hi")
            btn.configure(bg="white")
            # unused function to change the colour of the button when pressed
            # unused as the colour changing function adds latency to the audio

        def record(keytoadd):  # this functions checks whether we are in recording mode
            if self.recording == True:
                self.end_time = time.time()
                time_elapsed = self.end_time - self.previous_time
                self.input_string.append(time_elapsed)
                self.input_string.append(f'{keytoadd}')

                self.previous_time = self.end_time

        #  function takes the key being pressed as a parameter and adds it to a list alongside the time of the
        #  previous input

        # Buttons for keyboard
        self.C_0_button = Button(self.pianoFrame, bg="white", text="C_0", fg=self.noteColour1,
                                 command=lambda: [note_C0(self, 1), record(f'C{self.octave}'),
                                                  update_note_text(f'C{self.octave}')], height=10, width=6)
        #  the keys are buttons that passes itself and either 1 or 2 corresponding to the first 12 keys or second 12 keys
        #  it also records the note alongside the current octave

        self.C_0_button.grid(row=3, column=0)
        self.master.bind('<z>',
                         lambda event: [note_C0(self, 1), record(f'C{self.octave}'), update_note_text(f'C{self.octave}')])

        self.D_0_button = Button(self.pianoFrame, bg="white", text="D_0", fg=self.noteColour1,
                                 command=lambda: [note_D0(self, 1), record(f'D{self.octave}'),
                                                  update_note_text(f'D{self.octave}')], height=10, width=6)
        self.D_0_button.grid(row=3, column=1)
        self.master.bind('<x>',
                         lambda event: [note_D0(self, 1), record(f'D{self.octave}'), update_note_text(f'D{self.octave}')])

        self.E_0_button = Button(self.pianoFrame, bg="white", text="E_0", fg=self.noteColour1,
                                 command=lambda: [note_E0(self, 1), record(f'E{self.octave}'),
                                                  update_note_text(f'E{self.octave}')], height=10, width=6)
        self.E_0_button.grid(row=3, column=2)
        self.master.bind('<c>',
                         lambda event: [note_E0(self, 1), record(f'E{self.octave}'), update_note_text(f'E{self.octave}')])

        self.F_0_button = Button(self.pianoFrame, bg="white", text="F_0", fg=self.noteColour1,
                                 command=lambda: [note_F0(self, 1), record(f'F{self.octave}'),
                                                  update_note_text(f'F{self.octave}')], height=10, width=6)
        self.F_0_button.grid(row=3, column=3)
        self.master.bind('<v>',
                         lambda event: [note_F0(self, 1), record(f'F{self.octave}'), update_note_text(f'F{self.octave}')])

        self.G_0_button = Button(self.pianoFrame, bg="white", text="G_0", fg=self.noteColour1,
                                 command=lambda: [note_G0(self, 1), record(f'G{self.octave}'),
                                                  update_note_text(f'G{self.octave}')], height=10, width=4)
        self.G_0_button.grid(row=3, column=4)
        self.master.bind('<b>',
                         lambda event: [note_G0(self, 1), record(f'G{self.octave}'), update_note_text(f'G{self.octave}')])

        self.A_0_button = Button(self.pianoFrame, bg="white", text="A_0", fg=self.noteColour1,
                                 command=lambda: [note_A0(self, 1), record(f'A{self.octave}'),
                                                  update_note_text(f'A{self.octave}')], height=10, width=6)
        self.A_0_button.grid(row=3, column=5)
        self.master.bind('<n>',
                         lambda event: [note_A0(self, 1), record(f'A{self.octave}'), update_note_text(f'A{self.octave}')])

        self.B_0_button = Button(self.pianoFrame, bg="white", text="B_0", fg=self.noteColour1,
                                 command=lambda: [note_B0(self, 1), record(f'B{self.octave}'),
                                                  update_note_text(f'B{self.octave}')], height=10, width=6)
        self.B_0_button.grid(row=3, column=6)
        self.master.bind('<m>',
                         lambda event: [note_B0(self, 1), record(f'B{self.octave}'), update_note_text(f'B{self.octave}')])

        self.placeHolder = Label(self.pianoFrame, height=7, width=6, bg=self.frameColour)
        self.placeHolder.grid(row=1, column=6)

        self.CC_0_button = Button(self.pianoFrame, bg="black", fg=self.noteColour2, text="C#_0",
                                  command=lambda: [note_CC0(self, 1), record(f'C#{self.octave}'),
                                                   update_note_text(f'C#{self.octave}')], height=10, width=3)
        # self.CC_0_button.grid(row=1, columnspan=2)
        self.CC_0_button.place(x=35, y=40)
        self.master.bind('<s>',
                         lambda event: [note_CC0(self, 1), record(f'C#{self.octave}'), update_note_text(f'C#{self.octave}')])

        self.DD_0_button = Button(self.pianoFrame, bg="black", fg=self.noteColour2, text="D#_0",
                                  command=lambda: [note_DD0(self, 1), record(f'D#{self.octave}'),
                                                   update_note_text(f'D#{self.octave}')], height=10, width=3)
        # self.DD_0_button.grid(row=1, columnspan=4)
        self.DD_0_button.place(x=85, y=40)
        self.master.bind('<d>',
                         lambda event: [note_DD0(self, 1), record(f'D#{self.octave}'), update_note_text(f'D#{self.octave}')])

        self.AA_0_button = Button(self.pianoFrame, bg="black", fg=self.noteColour2, text="A#_0",
                                  command=lambda: [note_AA0(self, 1), record(f'A#{self.octave}'),
                                                   update_note_text(f'A#{self.octave}')], height=10, width=3)
        # self.AA_0_button.grid(row=1, column=5, columnspan=2)
        self.AA_0_button.place(x=290, y=40)
        self.master.bind('<j>',
                         lambda event: [note_AA0(self, 1), record(f'A#{self.octave}'), update_note_text(f'A#{self.octave}')])

        self.GG_0_button = Button(self.pianoFrame, bg="black", fg=self.noteColour2, text="G#_0",
                                  command=lambda: [note_GG0(self, 1), record(f'G#{self.octave}'),
                                                   update_note_text(f'G#{self.octave}')], height=10, width=3)
        # self.GG_0_button.grid(row=1, column=4, columnspan=2)
        self.GG_0_button.place(x=240, y=40)
        self.master.bind('<h>',
                         lambda event: [note_GG0(self, 1), record(f'G#{self.octave}'), update_note_text(f'G#{self.octave}')])

        self.FF_0_button = Button(self.pianoFrame, bg="black", fg=self.noteColour2, text="F#_0",
                                  command=lambda: [note_FF0(self, 1), record(f'F#{self.octave}'),
                                                   update_note_text(f'F#{self.octave}')], height=10, width=3)
        # self.FF_0_button.grid(row=1, column=3, columnspan=2)
        self.FF_0_button.place(x=190, y=40)
        self.master.bind('<g>',
                         lambda event: [note_FF0(self, 1), record(f'F#{self.octave}'), update_note_text(f'F#{self.octave}')])

        # -----------------------------------------------------------------------------------------------------
        #
        self.C_0_button2 = Button(self.pianoFrame, bg="white", text="C_1",
                                  command=lambda: [note_C0(self, 2), record(f'C{self.secondoctave}'), update_note_text(f'C{self.secondoctave}')],
                                  height=10, width=6)
        self.C_0_button2.grid(row=3, column=7)
        self.master.bind('<w>', lambda event: [note_C0(self, 2), record(f'C{self.secondoctave}'), update_note_text(f'C{self.secondoctave}')])

        self.D_0_button2 = Button(self.pianoFrame, bg="white", text="D_1",
                                  command=lambda: [note_D0(self, 2), record(f'D{self.secondoctave}'),
                                                   update_note_text(f'D{self.secondoctave}')], height=10, width=6)
        self.D_0_button2.grid(row=3, column=8)
        self.master.bind('<e>', lambda event: [note_D0(self, 2), record(f'D{self.secondoctave}'), update_note_text(f'D{self.secondoctave}')])

        self.E_0_button2 = Button(self.pianoFrame, bg="white", text="E_1",
                                  command=lambda: [note_E0(self, 2), record(f'E{self.secondoctave}'),
                                                   update_note_text(f'E{self.secondoctave}')], height=10, width=6)
        self.E_0_button2.grid(row=3, column=9)
        self.master.bind('<r>', lambda event: [note_E0(self, 2), record(f'E{self.secondoctave}'), update_note_text(f'E{self.secondoctave}')])

        self.F_0_button2 = Button(self.pianoFrame, bg="white", text="F_1",
                                  command=lambda: [note_F0(self, 2), record(f'F{self.secondoctave}'),
                                                   update_note_text(f'F{self.secondoctave}')], height=10, width=6)
        self.F_0_button2.grid(row=3, column=10)
        self.master.bind('<t>', lambda event: [note_F0(self, 2), record(f'F{self.secondoctave}'), update_note_text(f'F{self.secondoctave}')])

        self.G_0_button2 = Button(self.pianoFrame, bg="white", text="G_1",
                                  command=lambda: [note_G0(self, 2), record(f'G{self.secondoctave}'),
                                                   update_note_text(f'G{self.secondoctave}')], height=10, width=4)
        self.G_0_button2.grid(row=3, column=11)
        self.master.bind('<y>', lambda event: [note_G0(self, 2), record(f'G{self.secondoctave}'), update_note_text(f'G{self.secondoctave}')])

        self.A_0_button2 = Button(self.pianoFrame, bg="white", text="A_1",
                                  command=lambda: [note_A0(self, 2), record(f'A{self.secondoctave}'),
                                                   update_note_text(f'A{self.secondoctave}')], height=10, width=6)
        self.A_0_button2.grid(row=3, column=12)
        self.master.bind('<u>', lambda event: [note_A0(self, 2), record(f'A{self.secondoctave}'), update_note_text(f'A{self.secondoctave}')])

        self.B_0_button2 = Button(self.pianoFrame, bg="white", text="B_1",
                                  command=lambda: [note_B0(self, 2), record(f'B{self.secondoctave}'),
                                                   update_note_text(f'B{self.secondoctave}')], height=10, width=6)
        self.B_0_button2.grid(row=3, column=13)
        self.master.bind('<i>', lambda event: [note_B0(self, 2), record(f'B{self.secondoctave}'), update_note_text(f'B{self.secondoctave}')])

        self.placeHolder2 = Label(self.pianoFrame, height=7, width=6, bg=self.frameColour)
        self.placeHolder2.grid(row=1, column=14)

        self.CC_0_button2 = Button(self.pianoFrame, bg="black", fg="white", text="C#_1",
                                   command=lambda: [note_CC0(self, 2), record(f'C#{self.secondoctave}'),
                                                    update_note_text(f'C#{self.secondoctave}')], height=10, width=3)
        # self.CC_0_button.grid(row=1, columnspan=2)
        self.CC_0_button2.place(x=385, y=40)
        self.master.bind('<Key-3>',
                         lambda event: [note_CC0(self, 2), record(f'C#{self.secondoctave}'), update_note_text(f'C#{self.secondoctave}')])

        self.DD_0_button2 = Button(self.pianoFrame, bg="black", fg="white", text="D#_1",
                                   command=lambda: [note_DD0(self, 2), record(f'D#{self.secondoctave}'),
                                                    update_note_text(f'D#{self.secondoctave}')], height=10, width=3)
        # self.DD_0_button.grid(row=1, columnspan=4)
        self.DD_0_button2.place(x=435, y=40)
        self.master.bind('<Key-4>',
                         lambda event: [note_DD0(self, 2), record(f'D#{self.secondoctave}'), update_note_text(f'D#{self.secondoctave}')])

        self.AA_0_button2 = Button(self.pianoFrame, bg="black", fg="white", text="A#_1",
                                   command=lambda: [note_AA0(self, 2), record(f'A#{self.secondoctave}'),
                                                    update_note_text(f'A#{self.secondoctave}')], height=10, width=3)
        # self.AA_0_button.grid(row=1, column=5, columnspan=2)
        self.AA_0_button2.place(x=640, y=40)
        self.master.bind('<8>',
                         lambda event: [note_AA0(self, 2), record(f'A#{self.secondoctave}'), update_note_text(f'A#{self.secondoctave}')])

        self.GG_0_button2 = Button(self.pianoFrame, bg="black", fg="white", text="G#_1",
                                   command=lambda: [note_GG0(self, 2), record(f'G#{self.secondoctave}'),
                                                    update_note_text(f'G#{self.secondoctave}')], height=10, width=3)
        # self.GG_0_button.grid(row=1, column=4, columnspan=2)
        self.GG_0_button2.place(x=590, y=40)
        self.master.bind('<7>',
                         lambda event: [note_GG0(self, 2), record(f'G#{self.secondoctave}'), update_note_text(f'G#{self.secondoctave}')])

        self.FF_0_button2 = Button(self.pianoFrame, bg="black", fg="white", text="F#_1",
                                   command=lambda: [note_FF0(self, 2), record(f'F#{self.secondoctave}'),
                                                    update_note_text(f'F#{self.secondoctave}')], height=10, width=3)
        # self.FF_0_button.grid(row=1, column=3, columnspan=2)
        self.FF_0_button2.place(x=540, y=40)
        self.master.bind('<6>',
                         lambda event: [note_FF0(self, 2), record(f'F#{self.secondoctave}'), update_note_text(f'F#{self.secondoctave}')])

        # -----------------------------------------------------------------------------------------------------

        self.lowerKeynotes = [self.C_0_button, self.D_0_button, self.E_0_button, self.F_0_button, self.G_0_button,
                              self.A_0_button,
                              self.B_0_button, self.C_0_button2, self.D_0_button2, self.E_0_button2, self.F_0_button2,
                              self.G_0_button2, self.A_0_button2,
                              self.B_0_button2]

        self.upperKeynotes = [self.CC_0_button, self.DD_0_button, self.AA_0_button, self.GG_0_button, self.FF_0_button,
                              self.CC_0_button2, self.DD_0_button2, self.AA_0_button2, self.GG_0_button2,
                              self.FF_0_button2]

        def note_colour_change():
            if self.noteColour1 == 'black':
                self.noteColour1 = 'white'
                self.noteColour2 = 'black'

            else:
                self.noteColour1 = 'black'
                self.noteColour2 = 'white'

            for i in range(0, len(self.lowerKeynotes)):
                self.lowerKeynotes[i].configure(fg=self.noteColour1)

            for i in range(0, len(self.upperKeynotes)):
                self.upperKeynotes[i].configure(fg=self.noteColour2)

        def pianoKeyText_change():
            t = 'text'
            for i in range(0, 7):
                self.lowerKeynotes[i].configure(text=f'{self.lowerKeynotes[i].cget(t)[0:2]}{self.octave}')

            for i in range(0, 5):
                self.upperKeynotes[i].configure(text=f'{self.upperKeynotes[i].cget(t)[0:3]}{self.octave}')

            for i in range(7, 14):
                self.lowerKeynotes[i].configure(text=f'{self.lowerKeynotes[i].cget(t)[0:2]}{self.secondoctave}')

            for i in range(5, 10):
                self.upperKeynotes[i].configure(text=f'{self.upperKeynotes[i].cget(t)[0:3]}{self.secondoctave}')

        self.lower_keybinds = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'W', 'E', 'R', 'T', 'Y', 'U', 'I']

        self.upper_keybinds = ['S', 'D', 'G', 'H', 'J', '3', '4', '6', '7', '8']

        def pianoKey_keybind_text():
            for i in range(0, 14):
                self.lowerKeynotes[i].configure(text=f'{self.lower_keybinds[i]}')

            for i in range(0, 10):
                self.upperKeynotes[i].configure(text=f'{self.upper_keybinds[i]}')

        self.piano_keybind_btn = Button(self.controlFrame, text='show key-binds', fg=self.labelColour, command=lambda: pianoKey_keybind_text())

        # self.piano_keybind_btn.place(x=300, y=50)  #to be implemented labels to show key binds

        # -----------------------------------------------------------------------------------------------------
        def print_volume(v):  # function will print the current volume
            self.volume = v
            self.sliderLabel.config(text='you have selected ' + v, fg=self.labelColour)
            print(self.volume)

        #  initiate volume slider
        self.volumeSlider = tk.Scale(self.controlFrame, label='VOLUME', from_=0, to=10, orient=tk.HORIZONTAL,
                                     length=200,
                                     tickinterval=1, resolution=1, command=print_volume)
        self.volumeSlider.grid(row=5, column=8)
        self.volumeSlider.configure(fg=self.labelColour)
        self.volumeSlider.set(5)

        self.sliderLabel = tk.Label(self.controlFrame, bg='white', fg='black', width=20, text='empty')
        self.sliderLabel.grid(row=6, column=8)

        # -------------------------------------------------------------------------------------

        def print_octave(o):  # this function will print the current octave
            self.secondoctave = int(o) + 1
            if self.secondoctave == 3:
                self.secondoctave = 2

            self.octavesliderLabel.config(text='octave: ' + o, fg=self.labelColour, bg=self.label_background_colour)
            self.octave = int(o)
            pianoKeyText_change()
            print(self.octave)
            print(self.secondoctave)

        # initiate octave slider
        self.octaveSlider = tk.Scale(self.octaveframe, label='OCTAVE', from_=-2, to=2, orient=tk.HORIZONTAL, length=100,
                                     tickinterval=1, resolution=1, command=print_octave)
        self.octaveSlider.grid(row=1, column=2)
        self.octaveSlider.configure(fg=self.labelColour)
        self.octaveSlider.set(0)

        # key binds added to change octave slider with the keyboard. works by adding or subtracting one to the slider
        self.master.bind('<Left>', lambda event: self.octaveSlider.set(self.octaveSlider.get() - 1), pianoKeyText_change())
        self.master.bind('<Right>', lambda event: self.octaveSlider.set(self.octaveSlider.get() + 1), pianoKeyText_change())

        self.octavesliderLabel = tk.Label(self.octaveframe, bg=self.label_background_colour, fg=self.labelColour, width=20, text='octave:0')
        self.octavesliderLabel.grid(row=2, column=2)

        #  changes colour of the recording buttonn
        def changeRecBtn():
            if self.recording == False:
                self.recording = True
                self.record_btn.configure(bg="red")
            else:
                self.recording = False
                self.record_btn.configure(bg="white")
                print("recording finished")
                print(self.input_string)
                self.previous_time = 0

        # uses loops to play back the recording list

        # WHERE OLD PLAYBACK FUNCTON USED TO GOOOO

        def deleteSong_function():
            deleteSong_msgbox = messagebox.askyesno('Confirmation', 'Do you want to proceed')
            if deleteSong_msgbox:
                self.input_string = []
                messagebox.showinfo(title="SUCCESS", message=f"Recorded song has been deleted")

        def show_user_details():
            print(f'The current ID is {self.user}')
            print(f'The current student name is {self.name}')

            messagebox.showinfo(title="ERROR", message=f"The current ID is {self.user}\nThe current student name is {self.name}")

        self.record_btn = tk.Button(self.recordFrame, text="⏺", fg=self.labelColour, height=3, width=4, command=lambda: changeRecBtn())
        # self.record_btn.grid(row=1, column=1)
        self.record_btn.place(x=0, y=20)

        self.playback_btn = tk.Button(self.recordFrame, text="⏵", fg=self.labelColour, height=3, width=4,
                                      command=lambda: threading.Thread(self.playback(self.input_string)).start())
        # self.playback_btn.grid(row=1, column=2)
        self.playback_btn.place(x=40, y=20)

        self.noteLabel = tk.Label(self.recordFrame, bg=self.label_background_colour, fg=self.labelColour, width=10, text=" ")
        # self.noteLabel.grid(row=1, column=5)
        self.noteLabel.place(x=0, y=80)

        self.deleteSong = tk.Button(self.recordFrame, text='🗑', fg=self.labelColour, height=1, width=4, command=deleteSong_function)
        self.deleteSong.place(x=0, y=100)

        self.saveSong = tk.Button(self.recordFrame, text='save', fg=self.labelColour, height=1, width=4, command=lambda: self.saveSong_window())
        self.saveSong.place(x=40, y=100)

        self.showIDNAME = tk.Button(self.recordFrame, text='show ID', fg=self.labelColour, height=1, width=7, command=show_user_details)
        self.showIDNAME.place(x=90, y=100)

        self.viewFeedback = tk.Button(self.recordFrame, text='View feedback', fg=self.labelColour, height=1, width=12, command=self.feedback_window)
        self.viewFeedback.place(x=160, y=100)

        self.instrument_list = ["Piano", "Guitar", "Harp", "Flute"]
        print(len(self.instrument_list))
        self.instrument_count = 0

        def update_btn_text(sign):  # changes text on a button
            if sign == ">":
                self.instrument_count += 1
                if self.instrument_count > len(self.instrument_list) - 1:
                    self.instrument_count = 0


            else:
                self.instrument_count -= 1
                if self.instrument_count < 0:
                    self.instrument_count = 3

            self.state.set(self.instrument_list[self.instrument_count])
            self.state_Label.configure(text=self.instrument_list[self.instrument_count])


        def update_note_text(note):
            # self.noteShow.set(note)
            self.noteLabel.configure(text=note)

        self.state = tk.StringVar()
        self.state.set("Piano")

        self.state_left_btn = tk.Button(self.controlFrame, text="<", command=lambda: update_btn_text("<"),
                                        fg=self.labelColour)
        self.state_left_btn.grid(row=6, column=11)

        self.state_right_btn = tk.Button(self.controlFrame, text=">", command=lambda: update_btn_text(">"),
                                         fg=self.labelColour)
        self.state_right_btn.grid(row=6, column=12)

        self.Label = Label(self.controlFrame, text="change\n instrument", fg=self.labelColour)
        self.Label.grid(row=6, column=10)

        self.state_Label = Label(self.controlFrame, text=self.instrument_list[0], width=5, bg='white', fg=self.labelColour, )
        self.state_Label.place(x=240, y=40)

        self.showNotes = Button(self.controlFrame, text='show notes', fg=self.labelColour, command=lambda: note_colour_change())
        self.showNotes.place(x=300, y=50)


        img = (Image.open(r"virtupiano_logo.png"))
        resized_img = img.resize((205, 30))
        new_img = ImageTk.PhotoImage(resized_img, master=self.master)
        self.photo_lbl = Label(self.recordFrame, image=new_img)
        self.photo_lbl.image = new_img

        self.photo_lbl.pack(side="right")

    def increment_channel(self):  # this function will increment the channel by 1
        self.channel_to_use += 1  # this is so that each note has its own channel and can play to its full length
        if self.channel_to_use == 88:
            self.channel_to_use = 0

    def playback(self, given_list):
        if not given_list:
            messagebox.showinfo(title="", message=f"Please record a song before using the playback function")
        pygame.mixer.set_num_channels(100)
        state = self.state.get()
        string_to_play = given_list
        print(string_to_play)
        channel_count = 0
        for i in range(1, len(string_to_play)):
            note = given_list[i]
            if i % 2 != 0:  # this flipflops between every item in the song string
                if str(note[1]) == '#':  # this if functions checks whether the note is black
                    note = pygame.mixer.Sound(f'wavsV3\\{state}\\octave{note[2:]}\\{state}{note[0:2]}.wav')
                else:
                    note = pygame.mixer.Sound(f'wavsV3\\{state}\\octave{note[1:]}\\{state}{note[0]}.wav')
                channel = pygame.mixer.Channel(channel_count)
                channel.play(note)
                channel_count += 1
            else:
                time.sleep(string_to_play[i])

    def saveSong_function(self, window, givenEntry):
        saveSong_msgbox = messagebox.askyesno('Confirmation', 'Do you want to proceed')
        songName = givenEntry.get()

        if saveSong_msgbox:
            if songName == "" or self.input_string == []:
                messagebox.showinfo(title="ERROR",
                                    message=f"invalid recording or name\n please fill out name entry\n make sure you"
                                            f" have recorded something")
            else:
                song_to_save = listtostring(self.input_string)  # converts the list
                print(song_to_save)
                self.song_db.insertData(self.user, self.name, songName, song_to_save)
                window.destroy()

            # this sql query saves the song with the following attributes

            #  song_to_save can be the same
            #  but user cannot?

    # uses configure to change all attributes

    def updateWindow(self):  # this function is used after UI colour changes are made
        self.master.configure(bg=self.backgroundColour)
        self.pianoFrame.configure(bg=self.frameColour)
        self.controlFrame.configure(bg=self.frameColour)

        self.sliderLabel.config(fg=self.labelColour, bg=self.label_background_colour)
        self.volumeSlider.configure(fg=self.labelColour, bg=self.frameColour)
        self.Label.configure(fg=self.labelColour, bg=self.frameColour)
        self.state_Label.configure(fg=self.labelColour, bg=self.label_background_colour)
        self.mainLabel.configure(fg=self.labelColour, bg=self.frameColour)
        self.state_left_btn.configure(fg=self.labelColour, bg=self.frameColour)
        self.state_right_btn.configure(fg=self.labelColour, bg=self.frameColour)
        self.placeHolder.configure(bg=self.frameColour)
        self.placeHolder2.configure(bg=self.frameColour)

        self.octaveSlider.configure(fg=self.labelColour, bg=self.frameColour)
        self.octaveframe.configure(bg=self.frameColour)
        self.octavesliderLabel.configure(fg=self.labelColour, bg=self.label_background_colour)

        self.recordFrame.configure(bg=self.frameColour)
        self.record_btn.configure(bg=self.frameColour, fg=self.labelColour)
        self.playback_btn.configure(bg=self.frameColour, fg=self.labelColour)
        self.noteLabel.configure(fg=self.labelColour, bg=self.label_background_colour)
        self.showNotes.configure(bg=self.frameColour, fg=self.labelColour)
        self.deleteSong.configure(bg=self.frameColour, fg=self.labelColour)
        self.saveSong.configure(bg=self.frameColour, fg=self.labelColour)
        self.showIDNAME.configure(bg=self.frameColour, fg=self.labelColour)
        self.viewFeedback.configure(bg=self.frameColour, fg=self.labelColour)

    def themeChanger(self, value):  # window containing buttons that change attributes for colour
        darkList = ['#5A5A5A', '#FFA500', '#656565', '#424242']
        highConTheme = ['#000000', '#39FF14', '#202020', '#373737']
        defaultList = ['#d8d8d8', '#856ff8', '#F0F0F0', 'white']
        #  function uses lists for the hex codes of colour
        # the if statements then make the appropriate change followed by the update function

        if value == "1":
            self.backgroundColour = darkList[0]
            self.labelColour = darkList[1]
            self.frameColour = darkList[2]
            self.label_background_colour = darkList[3]

            self.updateWindow()

        elif value == "2":
            self.backgroundColour = defaultList[0]
            self.labelColour = defaultList[1]
            self.frameColour = defaultList[2]
            self.label_background_colour = defaultList[3]

            self.updateWindow()

        elif value == "3":
            self.backgroundColour = highConTheme[0]
            self.labelColour = highConTheme[1]
            self.frameColour = highConTheme[2]
            self.label_background_colour = highConTheme[3]

            self.updateWindow()

    def destroy_GUI(self):
        self.master.destroy()

    def show_GUI(self):
        self.master.mainloop()

    def saveSong_window(self):
        win = Tk()
        win.title("Welcome")
        win.geometry("350x150")

        savelabel = Label(win, text="Please enter song name")
        savelabel.grid(row=1, column=1)

        songName_entry = Entry(win, width=30)
        songName_entry.grid(row=2, column=2)

        save_btn = Button(win, text="save", width=12, command=lambda: self.saveSong_function(win, songName_entry))
        save_btn.grid(row=2, column=1, padx=10, pady=10)

        exitButton = Button(win, text="back", width=12, command=lambda: win.destroy())
        exitButton.grid(row=3, column=2, pady=5)

    def feedback_window(self):
        win = Tk()
        win.title("Welcome")
        win.geometry("500x550")

        savelabel = Label(win, text="FEEDBACK AND SCORE", font='Times 18')
        savelabel.grid(row=1, column=1)

        conn = sqlite3.connect('Student_songs.db')

        cursor = conn.cursor()

        result_to_fetch = cursor.execute('SELECT SongName, Feedback, Score FROM SONG_DATABASE WHERE StudentID = ?', (self.user,))
        results = result_to_fetch.fetchall()  # this will return a list of (song name, feedback, score) for all records under the specified ID

        row_coords = 2
        column_coords = 1

        for i in range(0, len(results)):
            string = f"For song: {results[i][0]} \nFeedback: {results[i][1]} \nScore: {results[i][2]}/10\n"
            #  this uses a for loop, string slicing, and list indexing to formulate a label that will show feedback/score for the song
            print(string)

            review_label = Label(win, text=string, bg='white', font='Times 14', justify="left")
            review_label.grid(row=row_coords, column=column_coords)
            if i == 4:  # the 6th song will be pushed to the next column
                row_coords = 2
                column_coords += 2

            else:
                row_coords += 4  # This is count is part of the loop so that every new label is placed underneath each other

        exitButton = Button(win, text="back", width=12, command=lambda: win.destroy())
        exitButton.grid(row=1, column=3)

        print(results)
        # feedback = cursor.fetchone()[0]
        # score = cursor.fetchone()[1]
        # print(f"i found the feedback: {feedback}")
        # print(f"i found the score: {score}")


def themeChangeWindow(object):
    win_theme = Tk()
    win_theme.title("Welcome")
    win_theme.geometry("350x100")

    dark_btn = Button(win_theme, text="dark", width=12, command=lambda: object.themeChanger("1"))
    dark_btn.grid(row=1, column=1, padx=10, pady=10)

    default_btn = Button(win_theme, text="default", width=12, command=lambda: object.themeChanger("2"))
    default_btn.grid(row=1, column=2, padx=10, pady=10)

    high_contrast_btn = Button(win_theme, text="high_contrast", width=12, command=lambda: object.themeChanger("3"))
    high_contrast_btn.grid(row=1, column=3, padx=10, pady=10)

    exitButton = Button(win_theme, text="back", width=12, command=lambda: win_theme.destroy())
    exitButton.grid(row=2, column=2, pady=5)

    mainloop()


def QandA_window():
    QandA_win = Tk()
    QandA_win.title("Help Window")
    QandA_win.geometry("500x400")

    welcome_lbl = Label(QandA_win, text="Welcome to the help window\nThis window will provide you with information\n to help you make the "
                                        "most out of my application")
    welcome_lbl.place(x=110, y=12)

    common_questions_lbl = Label(QandA_win, text="Commonly asked questions:\n"
                                                 "Q1: How do i record songs?\n A: Press the button with the symbol '⏺' any notes you now play will "
                                                 "then be recorded, "
                                                 "\n after pressing the button again the recording will stop"
                                                 "\n\nQ2: How do i listen to my recorded song?\nA: Press the button with the symbol '⏵'"
                                                 "\n\nQ3: How do i save my song?\nA: after you have recorded a song, press the 'save' button"
                                                 "\nA prompt will appear to write a song name, make sure this has been filled in.\n"
                                                 "Once done, press the 'save' button and press 'ok'"
                                                 "\n\nQ4:I have recorded a song but i want to restart it, how do i do this?"
                                                 "\nA: If you want to restart your song, press the button labeled, '🗑'"
                                                 "\nThis will delete your recorded song and allow you to restart"
                                                 "\n\nQ5: Where can i view my feedback?\nA: Press the, 'view feedback' button", justify="left",
                                 bg="white")
    common_questions_lbl.place(x=10, y=70)


def piano_guide_window():
    guide_win = Tk()
    guide_win.title("Help Window")
    guide_win.geometry("500x250")

    welcome_lbl = Label(guide_win, text="Welcome to the help window\nThis window will provide you with information\n to help you make the "
                                        "most out of my application")
    welcome_lbl.place(x=110, y=12)

    features_lbl = Label(guide_win, text="How to use the piano:\nThe piano can be played in three ways..."
                                         "\n1. Clicking the keys with your mouse/trackpad"
                                         "\n2. Pressing your computer keyboard"
                                         "\n3. Touching the screen (If you laptop has touchscreen functionality)"
                                         "\n\n Volume and Octaves can be changed by adjusting their respective sliders"
                                         "\n You can press either the left(←) or right(→) arrow keys to shift octaves"
                                         "\n Clicking the buttons, '<' or '>' will change which instrument sound you will hear ", justify="left",
                         bg="white")
    features_lbl.place(x=10, y=70)


class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Main Window')
        self.geometry('900x500')  # 450 x 600 , 900 used to be 750


def Piano_main(userID, userName):
    mainWindow = main_window()
    pianoFrame = MyPianoGUI(mainWindow, userID, userName)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(100)

    pianoFrame.show_GUI()


if __name__ == "__main__":
    # main("1", "Kurt")

    Piano_main("1", "Kurt")
