

PRODUCTS = 'products.txt'
PURCHASES = "purchases.txt"


def read_file(filename):
    try:
        with open(filename, encoding="UTF8") as my_file:
            my_file = my_file.readlines()
            return my_file

    except OSError as error:
        print(f"Whops we have a problem \n{error}")


def make_dict(file):
    foo = dict()
    for element in file:
        element = "".join(element)
        element = element.replace("\n", "")
        key, value = element.split(" ", maxsplit=2)
        foo[key] = value
    return foo


def main():
    products = read_file(PRODUCTS)
    purchases = read_file(PURCHASES)

    products = make_dict(products)
    purchases = make_dict(purchases)

    for product_code, offical_dealer in products.items():
        for purchase_code, dealer in purchases.items():
            if product_code == purchase_code:
                if offical_dealer != dealer:
                    print(f"Product code is: {product_code}\n"
                          f"Offical dealer is: {offical_dealer}\n"
                          f"Dealer list is: {dealer}\n")


if __name__ == '__main__':
    main()
