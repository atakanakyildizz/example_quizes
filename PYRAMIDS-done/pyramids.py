FILENAME = 'map.txt'


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()

    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def main():
    file = read_file(FILENAME)

    for a in range(4):
        row = 0
        colum = 0
        a = int(input(""))
        b = int(input(""))
        if a <= 10 and b <= 10:
            for lines in file:
                lines = lines.split(" ")
                if row == a:
                    for words in lines:
                        if colum == b:
                            print(words, row, colum)
                        colum = colum + 1
                row = row + 1
        else:
            print("Error: You enter wrong number ")


if __name__ == '__main__':
    main()
