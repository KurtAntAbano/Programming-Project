from tkinter import Canvas, PhotoImage, Tk

root = Tk()

root.geometry("1230x750")
bg = PhotoImage(file="../piano_testing_and_files/V3_programming_project/virtupiano_logo.png")

canvas1 = Canvas(root)
canvas1.pack(fill="both",expand=True)

canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

root.mainloop()