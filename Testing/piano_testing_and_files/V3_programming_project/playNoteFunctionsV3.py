from NoteClassV3 import *


def note_C0(soundObj,keysection):
    # this function takes the object piano along with all its current attributes
    # the function then creates an object from the note class, passing each parameter and calls the noteplay method

    state = soundObj.state.get()
    noteObject = note("C", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 0)
    noteObject.notePlay()
    # time.sleep(0.5)
    # print("stop")
    #noteObject.noteStop()



def note_CC0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("C#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 1)
    noteObject.notePlay()


def note_D0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("D", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 2)
    noteObject.notePlay()



def note_DD0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("D#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 3)
    noteObject.notePlay()



def note_E0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("E", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 4)
    noteObject.notePlay()



def note_F0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("F", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 5)
    noteObject.notePlay()


def note_FF0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("F#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 6)
    noteObject.notePlay()

def note_G0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("G", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 7)
    noteObject.notePlay()



def note_GG0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("G#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 8)
    noteObject.notePlay()


def note_A0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("A", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 9)
    noteObject.notePlay()


def note_AA0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("A#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 10)
    noteObject.notePlay()

def note_B0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("B", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, 11)
    noteObject.notePlay()