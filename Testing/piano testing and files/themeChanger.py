from tkinter import *
from piano_Test import *





def themeChangeWindow(object):
    win_theme = Tk()
    win_theme.title("Welcome")
    win_theme.geometry("350x100")


    dark_btn = Button(win_theme, text="dark", width=12, command = lambda:object.themeChanger("1"))
    dark_btn.grid(row=1, column=1, padx=10, pady=10)

    default_btn = Button(win_theme, text="default", width=12)
    default_btn.grid(row=1, column=2, padx=10, pady=10)

    high_contrast_btn = Button(win_theme, text="high_contrast", width=12)
    high_contrast_btn.grid(row=1, column=3, padx=10, pady=10)



    exitButton = Button(win_theme, text="back", width=12, command=lambda: win_theme.destroy())
    exitButton.grid(row=2, column=2, pady=5)

    mainloop()

darkList = ['#5A5A5A', '#FFA500']
highConTheme = ['#000000', '#028A0F']




# USE LISTS, each theme can be a list, bg can be assigned to list[0], fg can be list[1] etc...




if __name__ == "__main__":
    themeChangeWindow("test")
