song1 = '1696600702.1202934,C0,0.2929251194000244,D0,0.24763083457946777,E0,0.27098608016967773,F0'
song2 = [1696600702.1202934, 'C0', 0.2929251194000244, 'D0', 0.24763083457946777, 'E0', 0.27098608016967773, 'F0']


def stringtolist(songString):
    songList = list(songString.split(','))
    for i in range(0, len(songList)):
        if i % 2 == 0:
            songList[i] = float(songList[i])

    return songList

def listtostring(songList):
    songString = ','.join(str(x) for x in songList)

    return songString

if __name__ == "__main__":
    print(song1)
    print(stringtolist(song1))
    print()
    print()
    print(song2)
    print(listtostring(song2))
