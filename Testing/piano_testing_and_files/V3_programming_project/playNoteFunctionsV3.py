from NoteClassV3 import *


def note_C0(soundObj,keysection):
    # this function takes the object piano along with all its current attributes
    # the function then creates an object from the note class, passing each parameter and calls the noteplay method

    #  the piano object is passed since the object posseses attributes of the note, whether the key is in the
    #  first half or second half is also passed (since this affects the octave)
    state = soundObj.state.get()
    noteObject = note("C", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()
    # time.sleep(0.5)
    # print("stop")
    #noteObject.noteStop()



def note_CC0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("C#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()


def note_D0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("D", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()



def note_DD0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("D#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    #noteObject.change_channel()



def note_E0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("E", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()



def note_F0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("F", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()


def note_FF0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("F#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()

def note_G0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("G", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()



def note_GG0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("G#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()


def note_A0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("A", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()


def note_AA0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("A#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()

def note_B0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("B", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection, soundObj)
    noteObject.notePlay()
    noteObject.change_channel()