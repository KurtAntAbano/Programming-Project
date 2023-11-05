# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
#frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = (Image.open(r"/Testing/piano testing and files/virtupiano_logo.png"))
resized_img = img.resize((205, 30))
new_img = ImageTk.PhotoImage(resized_img)
photo_lbl = Label(frame, image=new_img)
# self.canvas.create_image(200, 40, anchor=NW, image=new_img)

# self.photo_lbl.pack(side="bottom", fill="both", expand=True)
photo_lbl.pack(side="right")

win.mainloop()