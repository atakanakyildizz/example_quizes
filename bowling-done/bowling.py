
from pprint import pprint
FILENAME = "bowling-done.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()

    except OSError as error:
        print(f"Whops we have a probblem\n{error}")


def make_dict(file):
    foo = dict()
    temp_list = []
    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(";")
        temp_list.append(lines)

    for i in range(len(temp_list)):
        foo[temp_list[i][0], temp_list[i][1]] = temp_list[i][2:]
    return foo


def main():
    file = read_file(FILENAME)
    file_dict = make_dict(file)

    for name, scores in file_dict.items():
        temp_list = []
        score = 0
        temp_list.append(scores)
        for i in temp_list:
            for j in i:
                score = score + int(j)
        file_dict[name] = score
    pprint(sorted(file_dict.items()))


if __name__ == '__main__':
    main()
