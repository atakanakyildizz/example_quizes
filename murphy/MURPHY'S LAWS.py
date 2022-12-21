FILENAME = "Murphy_reads.txt"
ARGUMENTS = "arguments.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            my_file = my_file.read()
            my_file = my_file.split('\n\n')
            return my_file

    except OSError as error:
        print(f"Whops we have a problem\n{error}")


def main():
    arguments = read_file(ARGUMENTS)
    murphy_law = read_file(FILENAME)

    my_result = ""
    for element in murphy_law:
        element = "".join(element)
        element = element.split("\n")
        my_result = my_result + "".join(element) + "\n"

    my_result_list = my_result.split("\n")

    for element in my_result_list:
        if len(element) > 60:
            print(element[0: 60] + "...")
        else:
            print(element)


if __name__ == '__main__':
    main()
