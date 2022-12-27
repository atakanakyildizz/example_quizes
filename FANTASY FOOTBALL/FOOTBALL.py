FILENAME = "fantafoot.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()
    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def main():
    file = read_file(FILENAME)

    defender = []
    forward = []
    midfielder = []
    goalkeeper = []
    foo = dict()

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(", ")
        foo[lines[0]] = lines[3]
        if int(lines[3]) <= 20:
            if lines[2] == "goalkeeper":
                goalkeeper.append(lines[0])

    for elements in goalkeeper:
        for keys, values in foo.items():
            if elements == keys:
                print(f"{keys} --> {values}")
    #print(goalkeeper)

if __name__ == '__main__':
    main()
