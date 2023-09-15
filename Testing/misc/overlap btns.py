import tkinter as tk
my_w = tk.Tk()
my_w.geometry("250x250")  # Size of the window


btn1=tk.Button(my_w,text='overlap me ',bg='yellow')
btn1.place(x=10,y=20)

btn2=tk.Button(my_w,text='hello ',bg='blue')
btn2.place(relx=.1,rely=.1)






my_w.mainloop()