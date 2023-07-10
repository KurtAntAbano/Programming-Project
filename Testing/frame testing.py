from tkinter import *
a= Tk()
a.geometry("400x400")
frame1=Frame(a,bg = "green",bd=10,width=100,
             height=50,cursor = "target").pack(side=TOP)
frame2=Frame(a,bg = "red",width=100,
             height=50,cursor = "target").pack(side=RIGHT)
frame3=Frame(a,bg = "yellow",bd=10,width=100,
             height=50,cursor = "target").pack(side=LEFT)
frame4=Frame(a,bg = "blue",bd=10,width=100,
             height=50,cursor = "target").pack(side=BOTTOM)
a.mainloop()  