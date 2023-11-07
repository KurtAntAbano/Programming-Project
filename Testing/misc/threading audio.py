from tkinter import *
import pyaudio
import wave
import sys
import threading

# --- classes ---

def play_audio():
    global is_playing
    chunk = 1024
    wf = wave.open('../piano_testing_and_files/V3_programming_project/PianoC.wav', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)

    data = wf.readframes(chunk)

    while data != '' and is_playing: # is_playing to stop playing
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()

# --- functions ---

def press_button_play():
    global is_playing
    global my_thread

    if not is_playing:
        is_playing = True
        my_thread = threading.Thread(target=play_audio)
        my_thread.start()

def press_button_stop():
    global is_playing
    global my_thread

    if is_playing:
        is_playing = False
        my_thread.join()

# --- main ---

is_playing = False
my_thread = None

root = Tk()
root.title("Compose-O-Matic")
root.geometry("400x300")

button_start = Button(root, text="PLAY", command=press_button_play)
button_start.grid()

button_stop = Button(root, text="STOP", command=press_button_stop)
button_stop.grid()

root.mainloop()