def get_starting_number():
    answer = input("How many bottles of beer on the wall? ")
    while answer.isnumeric() == False or int(answer) < 1:
        answer = input("How many bottles of beer on the wall? ")
    return int(answer)

def sing(starting_number):
    song_lyrics = ""
    bottles = starting_number
    while bottles > 0:
        if bottles == 1:
            song_lyrics = (
                song_lyrics
                + "1 bottle of beer on the wall, 1 bottle of beer.\n"
            )
            song_lyrics = (
                song_lyrics
                + "Take it down, pass it around, "
                + "no more bottles of beer on the wall!\n"
            )
        elif bottles == 2:
            song_lyrics = (
                song_lyrics
                + "2 bottles of beer on the wall, 2 bottles of beer.\n"
            )
            song_lyrics = (
                song_lyrics
                + "Take one down, pass it around, "
                + "1 bottle of beer on the wall.\n"
            )
            song_lyrics = song_lyrics + "\n"
        else:
            song_lyrics = (
                song_lyrics
                + str(bottles)
                + " bottles of beer on the wall, "
                + str(bottles)
                + " bottles of beer.\n"
            )
            song_lyrics = (
                song_lyrics
                + "Take one down, pass it around, "
                + str(bottles - 1)
                + " bottles of beer on the wall.\n"
            )
            song_lyrics = song_lyrics + "\n"
        bottles = bottles -1
    print (song_lyrics, end="")