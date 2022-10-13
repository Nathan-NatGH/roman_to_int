import re


def is_roman_number():  # TODO add exception for null input
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


def roman_to_int(rom_num: str):
    arabic_num = 0
    explanation = []
    rom_num_as_list = []
    used_temp_elements = []

    for _ in range(len(rom_num) + 1):
        if rom_num[:2] in value_dict.keys():     # test first 2 letters
            rom_num_as_list.append(rom_num[:2])  # special? add double letter combo to list
            rom_num = rom_num[2:]               # and remove first 2 letters from beginning
        else:
            rom_num_as_list.append(rom_num[:1])  # not special? add single letter to list
            rom_num = rom_num[1:]               # and remove single letter from beginning

    # TODO figure out why getting blank items so I can delete this filter
    rom_num_as_list = list(filter(None, rom_num_as_list))  

    for element in rom_num_as_list:
        element_value = value_dict[element]
        arabic_num += element_value

        if element not in used_temp_elements:
            num_appearances = rom_num_as_list.count(element)
            explanation.append(num_appearances * element + ' = ' + str(num_appearances * element_value))
            used_temp_elements.append(element)

    return arabic_num, explanation


def main():
    while True:
        roman_original = is_roman_number()
        arabic_num, explanation = roman_to_int(roman_original)
        print(f'\nRoman numeral {roman_original} = {arabic_num}')
        print(*explanation, sep=", ")

        answer = input("\nPress enter to continue or (q to quit).")
        if answer == "q":
            break


main()
