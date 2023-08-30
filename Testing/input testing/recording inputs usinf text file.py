open('data.txt', 'w').close() #erases the old data.txt file

import keyboard
from functools import partial

def print_pressed_keys(f,e):
    a = str(e.time) + "," + str(e) + "," #+ str(e.scan_code)
    f.write(a)
    f.write('\r')

f = open("data.txt", "a")
keyboard.hook(partial(print_pressed_keys,f))
keyboard.wait('esc')
f.close()
keyboard.unhook_all()