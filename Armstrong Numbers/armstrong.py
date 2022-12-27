FILENAME = "numbers.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()
    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def main():
    file = read_file(FILENAME)
    for numbers in file:
        counter = 0
        numbers = numbers.replace("\n", "")
        n = len(numbers)
        for element in numbers:
             counter = int(element)**n + counter

        if counter == int(numbers):
            print(counter)


if __name__ == '__main__':
    main()
