

FILENAME = "scores.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()

    except OSError as error:
        print(f"Whops we have a problem\n{error}")


def make_dict(file):
    foo = dict()
    for lines in file:
        lines = "".join(lines)
        lines = lines.replace("\n", "")
        lines = lines.split(" ")
        foo[lines[0], lines[1]] = lines[2:]
    return foo


def female_winner(dictionary):
    temp_list = []
    for name, elements in dictionary:
        if elements[0] == "F":
            temp_list.append(float(elements[2]))
    temp_list = sorted(temp_list)

    for name, elements in dictionary:
        if temp_list[-1] == elements[2]:
            print(f"{name}, {elements[1]} - Score: {elements[2]}")

def overall_nations_ranking(dictionary):
    usa_score, ita_score, grb_score = 0,0,0

    for name, elements in dictionary:
        if elements[1] == "USA":
            usa_score = usa_score + elements[2]
        elif elements[1] == "ITA":
            ita_score = ita_score + elements[2]
        elif elements[1] == "GRB":
            grb_score = grb_score + elements[2]

    print(f"ITA = {ita_score}\n"
          f"USA = {usa_score}\n"
            f"GRB = {grb_score}")


def main():
    file = read_file(FILENAME)
    file_dict = make_dict(file)

    for name, elements in file_dict.items():
        elements[2] = float(elements[2])+float(elements[3])+float(elements[4])+float(elements[5])+float(elements[6])
        elements[3:] = ""

    female_winner(file_dict.items())
    overall_nations_ranking(file_dict.items())



if __name__ == '__main__':
    main()
