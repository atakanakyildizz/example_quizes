FILENAME = "characters.txt"
FILENAME2 = "question1.txt"
FILENAME3 = "question2.txt"


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


def function(FILENAME, FILENAME2):
    characters = read_file(FILENAME)
    quest1 = read_file(FILENAME2)

    characters[0] = characters[0].split(";")

    index = []
    result = []
    for elements in quest1:
        a = 0
        elements = elements.split("=")
        for words in characters[0]:
            if elements[0].replace(" ", "") == words.replace(" ", ""):
                index.append(int(a))
                result.append(elements[1])
            a = a + 1

    characters = characters[1:]
    for lines in characters:
        lines = lines.split(";")
        counter = []
        for i in index:
            for things in result:
                if things.replace(" ", "") == lines[i].replace(" ", ""):
                    counter.append(things)
                if len(counter) == len(result):
                    return lines


def main():
    characters = read_file(FILENAME)
    characters = characters[0].split(";")
    print("                ", characters)

    first_question = function(FILENAME, FILENAME2)
    print("First question: ", first_question)
    second_question = function(FILENAME, FILENAME3)
    print("Second question: ", second_question)


if __name__ == '__main__':
    main()
