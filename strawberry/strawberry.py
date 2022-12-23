
strawberry_file = "strawberry.txt"
strawberry_shorts = "strawberry-short.txt"

from pprint import pprint

def read_file(filename):
    try:
        with open(filename) as my_file:
            my_file = my_file.read()
            my_file = my_file.upper()
            my_file = my_file.replace(",","")
            my_file = my_file.replace("...", "")
            my_file = my_file.split("\n")
            return my_file

    except OSError as error:
        print(f"Whops we have a problem\n{error}")


def finding_the_words(filename):

    strawberry_short = read_file(filename)
    word_ = []
    for element in strawberry_short:
        sentences = []
        sentence = "".join(element)
        sentences.append(sentence.split(" "))
        for words in sentences:
            for i in range(len(words)):
                if len(words) >= i+3:
                    if len(words[i]) == len(words[i+1]) and len(words[i+2]) == len(words[i+1]):
                        word_.append(f"'{words[i]}', '{words[i + 1]}', '{words[i + 2]}'")
    return word_

def main():
    the_list = finding_the_words(strawberry_file)
    for element in the_list:
        print(f"({element})")

if __name__ == '__main__':
    main()
