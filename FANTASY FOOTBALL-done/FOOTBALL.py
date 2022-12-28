FILENAME = "fantafoot.txt"


def read_file(filename):
    try:
        with open(filename) as my_file:
            return my_file.readlines()
    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def goalkeepers():
    file = read_file(FILENAME)

    goalkeeper = []
    budget = 20
    number_of_goalkeepers = 3

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(", ")
        if int(lines[3]) <= 40:
            if lines[2] == "goalkeeper":
                temp = lines[0], int(lines[3])
                goalkeeper.append(temp)
    my_goalkeepers = []
    pricelist = []
    for name, price in goalkeeper:
        pricelist.append(price)
    pricelist.sort(reverse=True)

    for elements in pricelist:
        for name, price in goalkeeper:
            if price == elements:
                temp = name, price
                if len(my_goalkeepers) < number_of_goalkeepers:
                    if budget >= (number_of_goalkeepers-len(my_goalkeepers)-1) + price:
                        my_goalkeepers.append(temp)
                        budget = budget - price
    print(f"Defenders: {my_goalkeepers}")


def defenders():
    file = read_file(FILENAME)

    defender = []
    budget = 40
    number_of_defenders = 8

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(", ")
        if int(lines[3]) <= 40:
            if lines[2] == "defender":
                temp = lines[0], int(lines[3])
                defender.append(temp)
    my_defenders = []
    pricelist = []
    for name, price in defender:
        pricelist.append(price)
    pricelist.sort(reverse=True)

    for elements in pricelist:
        for name, price in defender:
            if price == elements:
                temp = name, price
                if len(my_defenders) < number_of_defenders:
                    if budget >= (number_of_defenders-len(my_defenders)-1) + price:
                        my_defenders.append(temp)
                        budget = budget - price
    print(f"Defenders: {my_defenders}")


def midfielders():
    file = read_file(FILENAME)

    midfielders = []
    budget = 80
    number_of_defenders = 8

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(", ")
        if int(lines[3]) <= budget:
            if lines[2] == "midfielder":
                temp = lines[0], int(lines[3])
                midfielders.append(temp)
    my_midfielders = []
    pricelist = []
    for name, price in midfielders:
        pricelist.append(price)
    pricelist.sort(reverse=True)

    for elements in pricelist:
        for name, price in midfielders:
            if price == elements:
                temp = name, price
                if len(my_midfielders) < number_of_defenders:
                    if budget >= (number_of_defenders-len(my_midfielders)-1) + price:
                        my_midfielders.append(temp)
                        budget = budget - price
    print(f"Midfielders: {my_midfielders}")


def forwards():
    file = read_file(FILENAME)

    forwards = []
    budget = 120
    number_of_defenders = 6

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(", ")
        if int(lines[3]) <= budget:
            if lines[2] == "forward":
                temp = lines[0], int(lines[3])
                forwards.append(temp)
    my_forwards = []
    pricelist = []
    for name, price in forwards:
        pricelist.append(price)
    pricelist.sort(reverse=True)

    for elements in pricelist:
        for name, price in forwards:
            if price == elements:
                temp = name, price
                if len(my_forwards) < number_of_defenders:
                    if budget >= (number_of_defenders-len(my_forwards)-1) + price:
                        my_forwards.append(temp)
                        budget = budget - price
    print(f"Forwards: {my_forwards}")


def main():
    goalkeepers()
    defenders()
    midfielders()
    forwards()


if __name__ == '__main__':
    main()
