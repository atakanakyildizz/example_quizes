FILENAME = "characters.txt"
from pprint import pprint



def read_file(filename):
    try:
        my_return = []
        with open(filename) as file:
            file = file.readlines()
            for elements in file:
                elements = elements.replace("\n", "")
                my_return.append(elements)
        return my_return
    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def main():
    characters = read_file(FILENAME)
    foo = dict()
    mynames = []
    property = characters[0].split(";")
    for i in range(len(property)):
        foo[property[i]] = mynames

    characters = characters[1:]
    for lines in characters:
        lines = lines.replace("\n", "")
        lines = lines.split(";")
        for words in lines:
            mynames.append(words)

    for num_lines in range(len(characters)):
        i = 0
        templist = []
        foo[property[i]] = templist

        for numbers in range(9):
            templist.append(mynames[numbers*i])
        i = i + 1



    pprint(foo)
    

if __name__ == '__main__':
    main()
