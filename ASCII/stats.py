FILENAME = "landscape.txt"
FILENAME2 = "landscape2.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()
    except OSError as error:
        print(f"We have a problem{error}")


def main():
    file = read_file(FILENAME)
    matrix = []
    for lines in file:
        lines = lines.replace("\n", "")
        matrix.append(lines)

    coordinate_x = int(input("Enter the x value: "))
    coordinate_y = int(input("Enter the y value: "))
    square_size = int(input("Enter the square size: "))

    try:
        letters = []
        for y in range(square_size):
            line = ''
            for x in range(square_size):
                line = line + "".join(matrix[coordinate_y + y][coordinate_x + x])
                letters.append(matrix[coordinate_y + y][coordinate_x + x])
            print(line)

        letters.sort()
        letters.append("asidfhbasidbf")
        counter = 0
        my_dict = dict()

        for a in range(len(letters)-1):
            counter = counter + 1
            if letters[a] != letters[a+1]:
                my_dict[letters[a]] = counter*100/(len(letters)-1)
                counter = 0

        for keys, items in my_dict.items():
            print(f"{keys}->{items}%")

    except IndexError as error:
        print(f"ERROR!! the square to analyze is out of limits.\n{error}")


if __name__ == '__main__':
    main()
