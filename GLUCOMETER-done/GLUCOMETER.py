
FILENAME = "glucometers.txt"
from pprint import pprint


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()

    except OSError as error:
        print(f"Whops we have a problem\n{error}")
def main():
    file = read_file(FILENAME)
    ide_code = []
    acq_time = []
    blood_glucose =[]
    body_temp = []
    heart_rate = []

    foo = dict()

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(" ")
        temp_list = []
        for elements in lines:
            temp_list.append(elements)
            foo[temp_list[0]] = temp_list[1:]

    pprint(foo)

if __name__ == '__main__':
    main()
