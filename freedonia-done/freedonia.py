FILENAME = "rules.dat"
FILENAME2 = "dates.dat"

from pprint import pprint


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()
    except OSError as error:
        print(f"Whops we have a problem\n{error}")


def make_dict(file):
    foo = dict()
    for element in file:
        word = "".join(element)
        word = word.replace("\n","")
        word = word.split(" ")
        for i in range(len(word)):
            foo[word[0]] = word[1:i+1]
    return foo


def main():
    rules = read_file(FILENAME)
    rules_dict = make_dict(rules)

    dates = read_file(FILENAME2)
    rules_last = []

    foo = dict()

    for date, rule in rules_dict.items():
        rule_date = date.replace(":", "")
        rule_date = rule_date.split("-")
        for element in dates:
            element = "".join(element)
            element = element.replace("\n", "")
            date_in_file = element.split("-")

            if (rule_date[2] < date_in_file[2]) or (rule_date[2] == date_in_file[2] and rule_date[1] < date_in_file[1]) or (rule_date[2] == date_in_file[2] and rule_date[1] == date_in_file[1] and rule_date[0] < date_in_file[0]):
                for x in rule:
                    if x[0] == "+":
                        rules_last.append(x[1:])
                    elif x[0] == "-":
                        rules_last.remove(x[1:])
                foo[element] = rules_last
            else:
                foo[element] = []

    pprint(foo)



if __name__ == '__main__':
    main()
