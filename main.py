import re


def is_roman_number():
    while True:
        num = input("Please enter a valid Roman numeral: ")

        pattern = re.compile(r"""   
                                    ^M{0,3}
                                    (CM|CD|D?C{0,3})?
                                    (XC|XL|L?X{0,3})?
                                    (IX|IV|V?I{0,3})?$
                """, re.VERBOSE)

        if re.match(pattern, num):
            break

    return num


value_dict = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

letter_combos_dict = {
    "CM": 900,
    "CD": 400,
    "XC": 90,
    "XL": 40,
    "IX": 9,
    "IV": 4,
}


def roman_to_int(rom_num):
    converted_to_integer = 0
    temp_str = rom_num
    explanation = []

    for key in letter_combos_dict:
        if key in rom_num:
            explanation.append(key + ' = ' + str(letter_combos_dict[key]))
            converted_to_integer += letter_combos_dict[key]
            temp_str = temp_str.replace(key, '')

    for letter in temp_str:
        explanation.append(letter + ' = ' + str(value_dict[letter]))
        converted_to_integer += value_dict[letter]

    print(f'Roman numeral {rom_num} = {converted_to_integer}')
    print('Explanation: ', end='')
    print(*explanation, sep=", ")
    print()


def main():
    while True:
        roman_original = is_roman_number()
        roman_to_int(roman_original)
        answer = input("Press enter to continue or (q to quit).")
        if answer == "q":
            break


main()
