ACTIONS = "actions.txt"
CARLFAIL = "actions-fail_carl.txt"
BOBFAIL = "actions-fail_bob.txt"

def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()
    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def Alice_box(name):
    alice_box = []
    actions = read_file(name)
    counter = 0
    for lines in actions:
        lines = lines.replace("\n", "")
        lines = lines.split(" ")
        try:
            if lines[1] == "gives":
                alice_box.append(lines[3])
            elif lines[1] == "takes":
                alice_box.remove(lines[3])
        except ValueError:
            counter = counter + 1
    if counter > 0:
        print(f"There is a error {counter}")
    print(alice_box)

def main():
    Alice_box(BOBFAIL)
    Alice_box(CARLFAIL)
    Alice_box(ACTIONS)



if __name__ == '__main__':
    main()
