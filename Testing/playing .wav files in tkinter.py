from tkinter import *
from winsound import *

root = Tk() # create tkinter window

play = lambda: PlaySound('c note.wav', SND_FILENAME)
button = Button(root, text = 'c note', command = play)

button.pack()
root.mainloop()