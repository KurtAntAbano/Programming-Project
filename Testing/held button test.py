# Import required libraries
from tkinter import *

# Create an instance of tkinter frame
win = Tk()

# Define the geometry of the window
win.geometry("750x250")

# Define a function
def handler1(e):
   print("You are moving the Mouse with the Left Button Pressed.")

def handler2(e):
   print("Button Released")

# Define a Label in Main window
Label(win, text="Move the Mouse with the Left Button Pressed", font='Helvetica 15 underline').pack(pady=30)

# Bind the Mouse events with the Handler
win.bind('<B1-Motion>', handler1)
win.bind('<ButtonRelease-1>', handler2)

win.mainloop()