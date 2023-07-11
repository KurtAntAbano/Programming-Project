from tkinter import *


def themeChangeWindow(object):
    win_theme = Tk()
    win_theme.title("Welcome")
    win_theme.geometry("350x100")


    dark_btn = Button(win_theme, text="dark", width=12, command=lambda:darkTheme(object))
    dark_btn.grid(row=1, column=1, padx=10, pady=10)

    default_btn = Button(win_theme, text="default", width=12)
    default_btn.grid(row=1, column=2, padx=10, pady=10)

    high_contrast_btn = Button(win_theme, text="high_contrast", width=12, command=lambda:highConTheme(object))
    high_contrast_btn.grid(row=1, column=3, padx=10, pady=10)



    exitButton = Button(win_theme, text="back", width=12, command=lambda: win_theme.destroy())
    exitButton.grid(row=2, column=2, pady=5)

    mainloop()

    #'#028A0F' green

def highConTheme(object):
    object.backgroundColour = '#5A5A5A'
    object.labelColour = '#FFA500'

def darkTheme(object):
    print(object.backgroundColour)
    # object.backgroundColour.set('#000000')
    # object.labelColour.set('#028A0F')





if __name__ == "__main__":
    themeChangeWindow("test")
