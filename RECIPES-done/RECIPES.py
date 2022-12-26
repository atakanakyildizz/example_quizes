FOODS = "foods.txt"
FUSILLI_ALLE_OLIVE = "fusilli_alle_olive.txt"
POLENTA_CONCIA = "polenta_concia.txt"


def readfile(filename):
    try:
        with open(filename) as file:
            return file.readlines()
    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def make_dict(file):
    my_list = []
    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(";")
        my_list.append(lines)
    my_list.pop(0)
    my_list.pop(-1)

    for elements in my_list:
        if len(elements) < 2:
            my_list.remove(elements)
    my_list.pop(-1)

    foo = dict()
    for elements in my_list:
        foo[elements[0]] = float(elements[1])
    return foo


def food_dict(food_list):
    foo = dict()
    for lines in food_list:
        lines = lines.replace("\n", "")
        lines = lines.split(";")
        foo[lines[0]] = lines[1], lines[2]
    return foo


def main():
    foods = readfile(FOODS)
    foods = food_dict(foods)

    fusulli = make_dict((readfile(FUSILLI_ALLE_OLIVE)))
    polenta = make_dict(readfile(POLENTA_CONCIA))

    cost = 0
    calories = 0

    for elements, grams in polenta.items():
        for a, b in foods.items():
            if elements == a:
                print(f"{a} - {grams}")
                cost = cost + (float(b[0])*grams/1000)
                calories = calories + (float(b[1])*grams/1000)
    print(f"\nNumber of ingredients: {len(polenta)}\n"
          f"Recipe cost: {cost}\n"
          f"Recipe calories: {calories}\n\n")

    cost = 0
    calories = 0
    for elements, grams in fusulli.items():
        for a, b in foods.items():
            if elements == a:
                print(f"{a} - {grams}")
                cost = cost + float(b[0])*grams/1000
                calories = calories + float(b[1])*grams/1000
    print(f"\nNumber of ingredients: {len(fusulli)}\n"
          f"Recipe cost: {cost}\n"
          f"Recipe calories: {calories}")


if __name__ == '__main__':
    main()
