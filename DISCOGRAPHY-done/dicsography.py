FILENAME = "artists.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            my_file = my_file.readlines()
            my_return = []
            for element in my_file:
                element = element.replace("\n", "")
                my_return.append(element)
            return my_return
    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def main():
    file = read_file(FILENAME)
    foo = dict()
    for lines in file:
        lines = lines.split(";")
        foo[lines[0]] = lines[1]

    songs = []
    for codes, files in foo.items():
        grups = read_file(files)
        for element in grups:
            element = element.split(";")
            songs.append((element[0], element[1], codes))

    songs = sorted(songs)

    t = 0
    for element in songs:
        if element[0] != t:
            print(element[0])
            t = element[0]
        print(element[1], element[2])


if __name__ == '__main__':
    main()
