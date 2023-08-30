import time

import keyboard

flag = False
inputlist = [[]]

while not flag:
    start = time.time()
    if keyboard.read_key() == "esc":
        flag = True

    else:
        for i in range(0,2):
            inputlist[0].append(keyboard.read_key())
            end = time.time()
            lengthBetween = end - start
            inputlist[0].append(lengthBetween)

print(inputlist)


