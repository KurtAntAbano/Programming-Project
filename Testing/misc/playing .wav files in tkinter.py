# Problems: small latency, repeatedly pressing a note does not sync
# possible Solutions: longer presses = longer note duration



from tkinter import *
from winsound import *

root = Tk() # create tkinter window

play = lambda: PlaySound('c note.wav', SND_FILENAME)

button = Button(root, text='c note', command=play)
button.pack()



#  ---------------------------KEY PRESS TEST------------------------------------------
def playNote(event):
    PlaySound('c note.wav', SND_FILENAME)

root.bind("<c>",playNote)




root.mainloop()