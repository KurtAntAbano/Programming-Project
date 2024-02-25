song3 = '1696600702.1202934,C0,0.2929251194000244,D0,0.24763083457946777,E0,0.27098608016967773,F0'
song2 = [1696600702.1202934, 'C0', 0.2929251194000244, 'D0', 0.24763083457946777, 'E0', 0.27098608016967773, 'F0']
song1 = [1700518497.0799303, 'E0', 1.1353676319122314, 'D0', 0.7319555282592773, 'C0', 0.35520434379577637, 'B-1', 1.5408971309661865, 'E-1', 0.3579287528991699, 'F#-1', 0.37304186820983887, 'G-1', 0.3585524559020996, 'A-1', 0.32934093475341797, 'B-1', 0.38792872428894043, 'A-1', 0.34629392623901367, 'G-1', 0.37407493591308594, 'E-1', 0.3712480068206787, 'G-1', 1.273707389831543, 'F#-1']



def stringtolist(songString):
    songList = list(songString.split(','))
    for i in range(0, len(songList)):  # converts a string to a list
        if i % 2 == 0:
            songList[i] = float(songList[i])

    return songList

def listtostring(songList):
    songString = ','.join(str(x) for x in songList)  # converts a list to a string

    return songString

if __name__ == "__main__":
    print(song1)
    print(listtostring(song1))

    # print(song1)
    # print(stringtolist(song1))
    # print()
    # print()

