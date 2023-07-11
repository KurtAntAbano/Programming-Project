from NoteClass import *



def note_C0(soundObj):
    if soundObj.state.get() == "Piano":
        noteToplay = r'wavs/wav-piano-sound-master_wav_c1.wav'
    else:
        noteToplay = r'wavs/56111__guitarmaster__c-note.wav'
    noteObject = note("C_0", noteToplay, soundObj.volume)
    noteObject.notePlay()


def note_CC0():
    #num1.set("C#_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_c1s.wav")
    sound.play()


def note_D0():
    #num1.set("D_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_d1.wav")
    sound.play()


def note_DD0():
    #num1.set("D#_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_d1s.wav")
    sound.play()


def note_E0():
    #num1.set("E_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_e1.wav")
    sound.play()


def note_F0():
    #num1.set("F_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_f1.wav")
    sound.play()


def note_FF0():
    #num1.set("F#_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_f1s.wav")
    sound.play()


def note_G0():
    #num1.set("G_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_g1.wav")
    sound.play()


def note_GG0():
    #num1.set("G#_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_g1s.wav")
    sound.play()


def note_A0():
    #num1.set("A_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_a1.wav")
    sound.play()


def note_AA0():
   # num1.set("A#_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_a1s.wav")
    sound.play()


def note_B0():
    #num1.set("B_0")
    sound = pygame.mixer.Sound("wavs/wav-piano-sound-master_wav_b1.wav")
    sound.play()