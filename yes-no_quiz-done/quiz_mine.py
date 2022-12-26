import random

FILENAME = "S08_question_answer_pairs.txt"


def read_line(filename):
    try:
        with open(filename) as my_file:
            my_file = my_file.readlines()
            my_file.pop(0)
            return my_file
    except OSError as error:
        print(f"Probably, you enter the wrong files name \n{error}")


def main():
    file = read_line(FILENAME)
    question = dict()
    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split("\t")
        lines[2] = lines[2].replace(".", "").lower()
        if lines[2] == "yes":
            question[lines[1]] = lines[2:]
        elif lines[2] == "no":
            question[lines[1]] = lines[2:]

    number_list = []
    a = int(input("Enter the amount that you want to play: "))
    for i in range(a):
        number_list.append(random.randint(0, len(question)))

    question_counter = 1
    point = 0
    for questions, answer in question.items():
        for x in number_list:
            if x == question_counter:
                print("\n****** ****** ****** ******")
                print(questions)
                input_answer = input("Enter the answer: ")
                input_answer = input_answer.lower()
                if answer[0] == input_answer:
                    print("You're correct ")
                    point = point + 1
                else:
                    print("You are wrong")
                print(f"Correct answer is: {answer[0]} \nYour point is: {point}")
                print("****** ****** ****** ******")
        question_counter = question_counter + 1


if __name__ == '__main__':
    main()
