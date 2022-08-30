from albums import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("please choose your album (invalid choice exit):")
    for index, (title, artist, years, songs) in enumerate(albums):
        print("{} : {}" .format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{} : {}".format(index + 1, song))

    choice_song = int(input())
    if 1 <= choice_song <= len(songs_list):
        title = songs_list[choice_song - 1][SONG_TITLE_INDEX]
    else:
        break

    print("playing {}".format(title))
    print("=" * 40)