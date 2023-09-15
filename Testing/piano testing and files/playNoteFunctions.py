from NoteClass import *
import time


def note_C0(soundObj,keysection):

    state = soundObj.state.get()


    noteObject = note("C", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()
    # time.sleep(0.5)
    # print("stop")
    #noteObject.noteStop()



def note_CC0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("C#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()


def note_D0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("D", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()



def note_DD0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("D#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()



def note_E0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("E", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()



def note_F0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("F", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()


def note_FF0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("F#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()

def note_G0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("G", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()



def note_GG0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("G#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()


def note_A0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("A", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()


def note_AA0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("A#", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()

def note_B0(soundObj,keysection):
    state = soundObj.state.get()

    noteObject = note("B", state, soundObj.volume,soundObj.octave, soundObj.secondoctave, keysection)
    noteObject.notePlay()