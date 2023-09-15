#Import the required library
from tkinter import *
from tkinter import ttk
from Project_loginUI_windows import accountWindow
#Create an instance of tkinter frame
win = Tk()
win.geometry("750x250")
#Create a Notebook widget
my_notebook= ttk.Notebook(win)
my_notebook.pack(expand=1,fill=BOTH)
#Create Tabs
tab1= ttk.Frame(my_notebook)
my_notebook.add(tab1, text= "Tab 1")
tab2= ttk.Frame(my_notebook)
my_notebook.add(tab2, text= "Tab2")
#Create a Label in Tabs

Label(tab1, text= "Hello, Howdy?", font= ('Helvetica 20 bold')).pack()
Label(tab2, text= "This is a New Tab Context", font=('Helvetica 20 bold')).pack()

# def on_tab_change(event):
#   tab = event.widget.tab('current')['text']
#   if tab == 'Tab1':
#       pass
#
#   elif tab == 'Tab2':
#       accountWindow()
#
# my_notebook.bind('<<NotebookTabChanged>>', on_tab_change)

win.mainloop()