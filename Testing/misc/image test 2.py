#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x270")

#Create a canvas
canvas= Frame(win, width= 500, height= 100)
canvas.pack()

#Load an image in the script
img= (Image.open(r"/Testing/piano_testing_and_files/virtupiano_logo.png"))

#Resize the Image using resize method
resized_image= img.resize((205,30))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
# canvas.create_image(1,1, anchor=NW, image=new_image)
photo_lbl=Label(canvas, image=new_image)
photo_lbl.place(x=0, y=60)

win.mainloop()