from timeit import default_timer
from tkinter import *

key_pressed = False
last_start = 0
heldtime_array = []

def start_stop_timer(key_pressed=False, last_start=0):
    if key_pressed == False:
       last_start = default_timer()
       key_pressed = True
    else:
        heldtime_array[len(heldtime_array)] = default_timer() - last_start

root = Tk()

frame = Frame(root, width=100, height=100)
# This will work with any key. See above link for specific keys.
frame.bind("<Key>", start_stop_timer)
frame.pack()

# Do other customisation/setup of your window here.

root.mainloop()