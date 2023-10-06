import tkinter as tk
from tkinter import *  # for python > 3.4
# 15/09/23
from playNoteFunctionsV3 import *

""" --__Midi0ke__--

First try for Midi0ke virtual piano for the midi-output.

Import pygame and tkinter in order to make a GUI for a piano-keyboard.

In the first piece of code I specify the functions for each note and the path for the .wav and
in the second I build the GUI for the piano-keyboard.

@author : Dead"""
import time


class MyPianoGUI:
    def __init__(self, master):
        self.master = master
        self.state = "Piano"
        self.volume = 90
        self.backgroundColour = '#d8d8d8'  # '#5A5A5A'
        self.labelColour = '#856ff8'
        self.frameColour = '#F0F0F0'
        self.octave = 0
        self.secondoctave = 1
        self.recording = False
        self.input_string = []
        self.previous_time = 0
        self.noteShow = ''
        self.noteShow = tk.StringVar()

        self.master.resizable(0, 0)

        self.pianoFrame = Frame(self.master)
        self.pianoFrame.pack(side='bottom', fill="none", expand=True, pady=5, padx=5, ipadx=10, ipady=10)
        self.pianoFrame.configure(bg=self.frameColour)

        self.octaveframe = Frame(self.master)
        self.octaveframe.pack(side='right', fill="both", expand=False, pady=5, padx=5, ipadx=10, ipady=10)

        self.controlFrame = Frame(self.master)
        self.controlFrame.pack(side="top", fill="both", expand=False, padx=5, pady=5, ipadx=10, ipady=10)
        self.controlFrame.configure(bg=self.frameColour)

        self.recordFrame = Frame(self.master)
        self.recordFrame.pack(side='left', fill="both", expand=True, pady=5, padx=5, ipadx=0, ipady=0)

        # https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/

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

        self.settings_menu.add_command(label='Colour themes', command=lambda: themeChangeWindow(pianoFrame))
        self.settings_menu.add_command(label='Adjust piano size')

        self.mainLabel = Label(self.pianoFrame, text="MIDIOKE", fg=self.labelColour)
        self.mainLabel.grid(row=0, columnspan=11)

        def colourChange(btn):
            btn.configure(bg="green")
            time.sleep(2)
            print("hi")
            # btn.configure(bg="white")
            # unused function to change the colour of the button when pressed
            # unused as the colour changing function adds latency to the audio

        def record(keytoadd):  # this functions checks whether we are in recording mode
            if self.recording == True:
                self.end_time = time.time()
                time_elapsed = self.end_time - self.previous_time
                self.input_string.append(time_elapsed)
                self.input_string.append(f'{keytoadd}{self.octave}')



                self.previous_time = self.end_time
        #  function takes the key being pressed as a parameter and adds it to a list alongside the time of the
        #  previous input

        # Buttons for keyboard
        self.C_0_button = Button(self.pianoFrame, bg="white", text="C_0",
                                 command=lambda: [note_C0(pianoFrame, 1), record("C"),
                                                  update_note_text(f'C{self.octave}')], height=10, width=6)
        self.C_0_button.grid(row=3, column=0)
        self.master.bind('<a>',
                         lambda event: [note_C0(pianoFrame, 1), record("C"), update_note_text(f'C{self.octave}')])

        self.D_0_button = Button(self.pianoFrame, bg="white", text="D_0",
                                 command=lambda: [note_D0(pianoFrame, 1), record("D"),
                                                  update_note_text(f'D{self.octave}')], height=10, width=6)
        self.D_0_button.grid(row=3, column=1)
        self.master.bind('<s>',
                         lambda event: [note_D0(pianoFrame, 1), record("D"), update_note_text(f'D{self.octave}')])

        self.E_0_button = Button(self.pianoFrame, bg="white", text="E_0",
                                 command=lambda: [note_E0(pianoFrame, 1), record("E"),
                                                  update_note_text(f'E{self.octave}')], height=10, width=6)
        self.E_0_button.grid(row=3, column=2)
        self.master.bind('<d>',
                         lambda event: [note_E0(pianoFrame, 1), record("E"), update_note_text(f'E{self.octave}')])

        self.F_0_button = Button(self.pianoFrame, bg="white", text="F_0",
                                 command=lambda: [note_F0(pianoFrame, 1), record("F"),
                                                  update_note_text(f'F{self.octave}')], height=10, width=6)
        self.F_0_button.grid(row=3, column=3)
        self.master.bind('<f>',
                         lambda event: [note_F0(pianoFrame, 1), record("F"), update_note_text(f'F{self.octave}')])

        self.G_0_button = Button(self.pianoFrame, bg="white", text="G_0",
                                 command=lambda: [note_G0(pianoFrame, 1), record("G"),
                                                  update_note_text(f'G{self.octave}')], height=10, width=4)
        self.G_0_button.grid(row=3, column=4)
        self.master.bind('<g>',
                         lambda event: [note_G0(pianoFrame, 1), record("G"), update_note_text(f'G{self.octave}')])

        self.A_0_button = Button(self.pianoFrame, bg="white", text="A_0",
                                 command=lambda: [note_A0(pianoFrame, 1), record("A"),
                                                  update_note_text(f'A{self.octave}')], height=10, width=6)
        self.A_0_button.grid(row=3, column=5)
        self.master.bind('<h>',
                         lambda event: [note_A0(pianoFrame, 1), record("A"), update_note_text(f'A{self.octave}')])

        self.B_0_button = Button(self.pianoFrame, bg="white", text="B_0",
                                 command=lambda: [note_B0(pianoFrame, 1), record("B"),
                                                  update_note_text(f'B{self.octave}')], height=10, width=6)
        self.B_0_button.grid(row=3, column=6)
        self.master.bind('<j>',
                         lambda event: [note_B0(pianoFrame, 1), record("B"), update_note_text(f'B{self.octave}')])

        self.placeHolder = Label(self.pianoFrame, height=7, width=6, bg=self.frameColour)
        self.placeHolder.grid(row=1, column=6)

        self.CC_0_button = Button(self.pianoFrame, bg="black", fg="white", text="C#_0",
                                  command=lambda: [note_CC0(pianoFrame, 1), record("C#"),
                                                   update_note_text(f'C#{self.octave}')], height=10, width=3)
        # self.CC_0_button.grid(row=1, columnspan=2)
        self.CC_0_button.place(x=35, y=40)
        self.master.bind('<w>',
                         lambda event: [note_CC0(pianoFrame, 1), record("C#"), update_note_text(f'C#{self.octave}')])

        self.DD_0_button = Button(self.pianoFrame, bg="black", fg="white", text="D#_0",
                                  command=lambda: [note_DD0(pianoFrame, 1), record("D#"),
                                                   update_note_text(f'D#{self.octave}')], height=10, width=3)
        # self.DD_0_button.grid(row=1, columnspan=4)
        self.DD_0_button.place(x=85, y=40)
        self.master.bind('<e>',
                         lambda event: [note_DD0(pianoFrame, 1), record("D#"), update_note_text(f'D#{self.octave}')])

        self.AA_0_button = Button(self.pianoFrame, bg="black", fg="white", text="A#_0",
                                  command=lambda: [note_AA0(pianoFrame, 1), record("A#"),
                                                   update_note_text(f'A#{self.octave}')], height=10, width=3)
        # self.AA_0_button.grid(row=1, column=5, columnspan=2)
        self.AA_0_button.place(x=290, y=40)
        self.master.bind('<u>',
                         lambda event: [note_AA0(pianoFrame, 1), record("A#"), update_note_text(f'A#{self.octave}')])

        self.GG_0_button = Button(self.pianoFrame, bg="black", fg="white", text="G#_0",
                                  command=lambda: [note_GG0(pianoFrame, 1), record("G#"),
                                                   update_note_text(f'G#{self.octave}')], height=10, width=3)
        # self.GG_0_button.grid(row=1, column=4, columnspan=2)
        self.GG_0_button.place(x=240, y=40)
        self.master.bind('<y>',
                         lambda event: [note_GG0(pianoFrame, 1), record("G#"), update_note_text(f'G#{self.octave}')])

        self.FF_0_button = Button(self.pianoFrame, bg="black", fg="white", text="F#_0",
                                  command=lambda: [note_FF0(pianoFrame, 1), record("F#"),
                                                   update_note_text(f'F#{self.octave}')], height=10, width=3)
        # self.FF_0_button.grid(row=1, column=3, columnspan=2)
        self.FF_0_button.place(x=190, y=40)
        self.master.bind('<t>',
                         lambda event: [note_FF0(pianoFrame, 1), record("F#"), update_note_text(f'F#{self.octave}')])

        # -----------------------------------------------------------------------------------------------------
        #
        self.C_0_button = Button(self.pianoFrame, bg="white", text="C_0", command=lambda:[note_C0(pianoFrame,2),record("C"),update_note_text(f'C{self.octave}')], height=10, width=6)
        self.C_0_button.grid(row=3, column=7)
        self.master.bind('<a>', lambda event: [note_C0(pianoFrame,2), record("C"),update_note_text(f'C{self.octave}')])

        self.D_0_button = Button(self.pianoFrame, bg="white", text="D_0",
                                 command=lambda: [note_D0(pianoFrame,2), record("D"),
                                                  update_note_text(f'D{self.octave}')], height=10, width=6)
        self.D_0_button.grid(row=3, column=8)
        self.master.bind('<s>', lambda event: [note_D0(pianoFrame,2), record("D"), update_note_text(f'D{self.octave}')])

        self.E_0_button = Button(self.pianoFrame, bg="white", text="E_0",
                                 command=lambda: [note_E0(pianoFrame,2), record("E"),
                                                  update_note_text(f'E{self.octave}')], height=10, width=6)
        self.E_0_button.grid(row=3, column=9)
        self.master.bind('<d>', lambda event: [note_E0(pianoFrame,2), record("E"), update_note_text(f'E{self.octave}')])

        self.F_0_button = Button(self.pianoFrame, bg="white", text="F_0",
                                 command=lambda: [note_F0(pianoFrame,2), record("F"),
                                                  update_note_text(f'F{self.octave}')], height=10, width=6)
        self.F_0_button.grid(row=3, column=10)
        self.master.bind('<f>', lambda event: [note_F0(pianoFrame,2), record("F"), update_note_text(f'F{self.octave}')])

        self.G_0_button = Button(self.pianoFrame, bg="white", text="G_0",
                                 command=lambda: [note_G0(pianoFrame,2), record("G"),
                                                  update_note_text(f'G{self.octave}')], height=10, width=4)
        self.G_0_button.grid(row=3, column=11)
        self.master.bind('<g>', lambda event: [note_G0(pianoFrame,2), record("G"), update_note_text(f'G{self.octave}')])

        self.A_0_button = Button(self.pianoFrame, bg="white", text="A_0",
                                 command=lambda: [note_A0(pianoFrame,2), record("A"),
                                                  update_note_text(f'A{self.octave}')], height=10, width=6)
        self.A_0_button.grid(row=3, column=12)
        self.master.bind('<h>', lambda event: [note_A0(pianoFrame,2), record("A"), update_note_text(f'A{self.octave}')])

        self.B_0_button = Button(self.pianoFrame, bg="white", text="B_0",
                                 command=lambda: [note_B0(pianoFrame,2), record("B"),
                                                  update_note_text(f'B{self.octave}')], height=10, width=6)
        self.B_0_button.grid(row=3, column=13)
        self.master.bind('<j>', lambda event: [note_B0(pianoFrame,2), record("B"), update_note_text(f'B{self.octave}')])

        self.placeHolder = Label(self.pianoFrame, height=7, width=6, bg=self.frameColour)
        self.placeHolder.grid(row=1, column=14)

        self.CC_0_button = Button(self.pianoFrame, bg="black", fg="white", text="C#_0",
                                  command=lambda: [note_CC0(pianoFrame,2), record("C#"),
                                                   update_note_text(f'C#{self.octave}')], height=10, width=3)
        # self.CC_0_button.grid(row=1, columnspan=2)
        self.CC_0_button.place(x=385, y=40)
        self.master.bind('<w>',
                         lambda event: [note_CC0(pianoFrame,2), record("C#"), update_note_text(f'C#{self.octave}')])

        self.DD_0_button = Button(self.pianoFrame, bg="black", fg="white", text="D#_0",
                                  command=lambda: [note_DD0(pianoFrame,2), record("D#"),
                                                   update_note_text(f'D#{self.octave}')], height=10, width=3)
        # self.DD_0_button.grid(row=1, columnspan=4)
        self.DD_0_button.place(x=435, y=40)
        self.master.bind('<e>',
                         lambda event: [note_DD0(pianoFrame,2), record("D#"), update_note_text(f'D#{self.octave}')])

        self.AA_0_button = Button(self.pianoFrame, bg="black", fg="white", text="A#_0",
                                  command=lambda: [note_AA0(pianoFrame,2), record("A#"),
                                                   update_note_text(f'A#{self.octave}')], height=10, width=3)
        # self.AA_0_button.grid(row=1, column=5, columnspan=2)
        self.AA_0_button.place(x=640, y=40)
        self.master.bind('<u>',
                         lambda event: [note_AA0(pianoFrame,2), record("A#"), update_note_text(f'A#{self.octave}')])

        self.GG_0_button = Button(self.pianoFrame, bg="black", fg="white", text="G#_0",
                                  command=lambda: [note_GG0(pianoFrame,2), record("G#"),
                                                   update_note_text(f'G#{self.octave}')], height=10, width=3)
        # self.GG_0_button.grid(row=1, column=4, columnspan=2)
        self.GG_0_button.place(x=590, y=40)
        self.master.bind('<y>',
                         lambda event: [note_GG0(pianoFrame,2), record("G#"), update_note_text(f'G#{self.octave}')])

        self.FF_0_button = Button(self.pianoFrame, bg="black", fg="white", text="F#_0",
                                  command=lambda: [note_FF0(pianoFrame,2), record("F#"),
                                                   update_note_text(f'F#{self.octave}')], height=10, width=3)
        # self.FF_0_button.grid(row=1, column=3, columnspan=2)
        self.FF_0_button.place(x=540, y=40)
        self.master.bind('<t>',
                         lambda event: [note_FF0(pianoFrame,2), record("F#"), update_note_text(f'F#{self.octave}')])

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
            self.octave = o
            self.octavesliderLabel.config(text='octave: ' + o, fg=self.labelColour)
            print(self.octave)

        def octaveincrease():  # functions to decrease and increase octave for key binds
            if self.octave != 2:
                self.octave += 1
                print_octave(str(self.octave))
            print(self.octave)

        def octavedecrease():
            if self.octave != -2:
                self.octave -= 1
                print_octave(str(self.octave))
            print(self.octave)

        # initiate octave slider
        self.octaveSlider = tk.Scale(self.octaveframe, label='OCTAVE', from_=-2, to=2, orient=tk.HORIZONTAL, length=100,
                                     tickinterval=1, resolution=1, command=print_octave)
        self.octaveSlider.grid(row=1, column=2)
        self.octaveSlider.configure(fg=self.labelColour)
        self.octaveSlider.set(0)

        # key binds added to change octave slider with the keyboard
        self.master.bind('<.>', lambda event: octaveincrease())
        self.master.bind('<,>', lambda event: octavedecrease())

        self.octavesliderLabel = tk.Label(self.octaveframe, bg='white', fg=self.labelColour, width=20, text='octave:0')
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
        def playback():
            state = self.state.get()
            print(self.input_string)
            for i in range(1, len(self.input_string)):
                note = self.input_string[i]
                if i % 2 != 0:
                    note = pygame.mixer.Sound(f'wavsV3\\{state}\\octave{note[1:]}\\{state}{note[0]}.wav')
                    note.play()
                else:
                    time.sleep(self.input_string[i])

        self.record_btn = tk.Button(self.recordFrame, text="⏺", height=3, width=4, command=lambda: changeRecBtn())
        self.record_btn.grid(row=1, column=1)

        self.playback_btn = tk.Button(self.recordFrame, text="⏵", height=3, width=4, command=lambda: playback())
        self.playback_btn.grid(row=1, column=2)

        self.noteLabel = tk.Label(self.recordFrame, bg='white', fg='black', width=26, textvariable=self.noteShow)
        self.noteLabel.grid(row=1, column=5)

        def update_btn_text():  # changes text on a button
            if self.state.get() == "Piano":
                self.state.set("Guitar")
            else:
                self.state.set("Piano")

        def update_note_text(note):
            self.noteShow.set(note)
            self.noteLabel.configure(textvariable=self.noteShow)

        self.state = tk.StringVar()
        self.state_btn = tk.Button(self.controlFrame, textvariable=self.state, command=update_btn_text,
                                   fg=self.labelColour)
        self.state.set("Piano")
        self.state_btn.grid(row=5, column=7)

        self.Label = Label(self.controlFrame, text="change\n state", fg=self.labelColour)
        self.Label.grid(row=6, column=7)

    # uses configure to change all attributes

    def updateWindow(self):  # this function is used after UI colour changes are made
        self.master.configure(bg=self.backgroundColour)
        self.pianoFrame.configure(bg=self.frameColour)
        self.controlFrame.configure(bg=self.frameColour)

        self.sliderLabel.config(fg=self.labelColour, bg=self.frameColour)
        self.volumeSlider.configure(fg=self.labelColour, bg=self.frameColour)
        self.Label.configure(fg=self.labelColour, bg=self.frameColour)
        self.mainLabel.configure(fg=self.labelColour, bg=self.frameColour)
        self.state_btn.configure(fg=self.labelColour, bg=self.frameColour)
        self.placeHolder.configure(bg=self.frameColour)

        self.octaveSlider.configure(fg=self.labelColour, bg=self.frameColour)
        self.octaveframe.configure(bg=self.frameColour)
        self.octavesliderLabel.configure(fg=self.labelColour, bg=self.frameColour)

        self.recordFrame.configure(bg=self.frameColour)
        self.record_btn.configure(bg=self.frameColour, fg=self.labelColour)
        self.playback_btn.configure(bg=self.frameColour, fg=self.labelColour)
        self.noteLabel.configure(fg=self.labelColour, bg=self.frameColour)

    def themeChanger(self, value):  # window containing buttons that change attributes for colour
        darkList = ['#5A5A5A', '#FFA500', '#656565']
        highConTheme = ['#000000', '#39FF14', '#202020']
        defaultList = ['#d8d8d8', '#856ff8', '#F0F0F0']
        #  function uses lists for the hex codes of colour
        # the if statements then make the appropriate change followed by the update function

        if value == "1":
            self.backgroundColour = darkList[0]
            self.labelColour = darkList[1]
            self.frameColour = darkList[2]

            self.updateWindow()

        elif value == "2":
            self.backgroundColour = defaultList[0]
            self.labelColour = defaultList[1]
            self.frameColour = defaultList[2]

            self.updateWindow()

        elif value == "3":
            self.backgroundColour = highConTheme[0]
            self.labelColour = highConTheme[1]
            self.frameColour = highConTheme[2]

            self.updateWindow()


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


class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Main Window')
        self.geometry('750x600')  # 450 x 600


mainWindow = main_window()
pianoFrame = MyPianoGUI(mainWindow)
num1 = StringVar()
pygame.mixer.init()

mainWindow.mainloop()
