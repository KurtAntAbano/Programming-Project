import tkinter

def quit():
    global tkTop
    tkTop.destroy()

def savepick(event):
    global colornumber
    colornumber = tkScale.get()
    print (colornumber)
    return (colornumber)

def doscale(tkScale):
    savepick(tkScale)
    quit()


tkTop = tkinter.Tk()
tkTop.geometry('300x200')

tkButtonQuit = tkinter.Button(tkTop, text="Enter", command=quit)
tkButtonQuit.pack()

tkScale = tkinter.Scale(tkTop, from_=0, to=5, orient=tkinter.HORIZONTAL)
tkScale.pack(anchor=tkinter.CENTER)

tkTop.bind("<Left>", lambda e: tkScale.set(tkScale.get()-1))
tkTop.bind("<Right>", lambda e: tkScale.set(tkScale.get()+1))
tkTop.bind("<Up>", doscale)

tkinter.mainloop()