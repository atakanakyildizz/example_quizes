FILENAME = "diabetes.csv"


def readfile(filename):
    try:
        with open(filename) as my_file:
            my_file = my_file.readlines()
            my_file.pop(0)
            return my_file
    except OSError as error:
        print(f"Probably, you have a name problem \n{error}")


def average_values_of_diabets(file):
    pregnancies = []
    glucose = []
    blood_pressure = []
    skin_thickness = []
    insulin = []
    bmi = []
    diabetes_pedigree_function = []
    age = []
    outcome = []

    pregnancies_counter = 0
    glucose_counter, blood_pressure_counter, skin_thickness_counter, insulin_counter = 0, 0, 0, 0
    bmi_counter, diabetes_pedigree_function_counter, age_counter, outcome_counter = 0, 0, 0, 0

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(",")
        pregnancies.append(lines[0])
        glucose.append(lines[1])
        blood_pressure.append(lines[2])
        skin_thickness.append(lines[3])
        insulin.append(lines[4])
        bmi.append(lines[5])
        diabetes_pedigree_function.append(lines[6])
        age.append(lines[7])
        outcome.append(lines[8])

    for x in pregnancies:
        x = int(x)
        pregnancies_counter = pregnancies_counter + x
    for x in blood_pressure:
        x = int(x)
        blood_pressure_counter = blood_pressure_counter + x
    for x in glucose:
        x = int(x)
        glucose_counter = glucose_counter + x
    for x in skin_thickness:
        x = int(x)
        skin_thickness_counter = skin_thickness_counter + x
    for x in insulin:
        x = int(x)
        insulin_counter = insulin_counter + x
    for x in bmi:
        x = float(x)
        bmi_counter = bmi_counter + x
    for x in diabetes_pedigree_function:
        x = float(x)
        diabetes_pedigree_function_counter = diabetes_pedigree_function_counter + x
    for x in outcome:
        x = int(x)
        outcome_counter = outcome_counter + x
    for x in age:
        x = int(x)
        age_counter = age_counter + x

    return pregnancies_counter / len(file), glucose_counter / len(file), blood_pressure_counter / len(file), \
           skin_thickness_counter / len(file), insulin_counter / len(file), bmi_counter / len(file), \
           diabetes_pedigree_function_counter / len(file), age_counter / len(file), outcome_counter / len(file)


def predict_diabets(file):
    pregnancies = (input("Enter your Number of pregnancies level: "))
    glucose = (input("Enter your Glucose level in blood level: "))
    blood_pressure = (input("Enter your Blood pressure level: "))
    skin_thickness = (input("Enter your thickness of the skin level: "))
    insulin = (input("Enter your Insulin level in blood: "))
    bmi = (input("Enter your Body mass index level: "))
    age = (input("Enter your age: "))

    for lines in file:
        lines = lines.replace("\n", "")
        lines = lines.split(",")
        if (lines[0]) == pregnancies:
            if (lines[1]) == glucose:
                if (lines[2]) == blood_pressure:
                    if (lines[3]) == skin_thickness:
                        if (lines[4]) == insulin:
                            if (lines[5]) == bmi:
                                if (lines[7]) == age:
                                    if lines[8] == 1:
                                        teshis = "You have diabet"
                                    else:
                                        teshis = "You don't have diabet"
                                    print(f"Your Diabetes percentage: {lines[6]}\n"
                                          f"{teshis}")
    else:
        print("\nWe don't have any information that you entered\n"
              "Please be sure the correct answers that you entered\n")


def main():
    file = readfile(FILENAME)
    pregnancies_counter, glucose_counter, blood_pressure_counter, skin_thickness_counter, insulin_counter, \
        bmi_counter, diabetes_pedigree_function_counter, age_counter, outcome_counter = average_values_of_diabets(file)

    predict_diabets(file)

    print(f"\nAverage values of diabets\n"
          f"---------------------------\n"
          f"pregnancies = {pregnancies_counter} \n"
          f"glucose = {glucose_counter} \n"
          f"blood_pressure = {blood_pressure_counter} \n"
          f"skin_thickness = {skin_thickness_counter} \n"
          f"insulin = {insulin_counter} \n"
          f"bmi = {bmi_counter} \n"
          f"diabetes_pedigree_function = {diabetes_pedigree_function_counter} \n"
          f"age = {age_counter} \n"
          f"outcome = {outcome_counter}\n"
          f"---------------------------\n")


if __name__ == '__main__':
    main()
