import re
import string

calib_vals = []
calib_vals_2 = []

DIGITS = {'zero' : '0',
          'one' : '1',
          'two' : '2',
          'three' : '3',
          'four' : '4',
          'five' : '5',
          'six' : '6',
          'seven' : '7',
          'eight' : '8',
          'nine' : '9'}


# def extract_digits(word) :
#     for digit_word, digit in DIGITS.items() :
#         if digit_word in word :
#             start_index = word.find(digit_word)
#             end_index = start_index + len(digit_word)
#             word = word[:start_index] + digit + word[end_index :]
#         word = word.replace(digit_word, digit)
#     return ''.join([char for char in word if char.isdigit()])


# def extract_digits(word):
#     for digit_word, digit in DIGITS.items():
#         word = word.replace(digit_word, digit)
#     return word   # [char for char in word if char.isdigit()]

def calculate_sum(data: list):
    sum = 0
    for word in data:
        match = re.findall("(?=(zero|one|two|three|four|five|six|seven|eight|nine))|(\d)", word)
        matches = [
            item[0] if item[0] != "" else item[1]
            for item in match
            if item[0] != "" or item[1] != ""
        ]

        matches = [
            DIGITS[item] if item in DIGITS.keys() else item
            for item in matches
        ]

        matches = [int(digit) for digit in matches]
        sum += int(f"{matches[0]}{matches[-1]}")

    return sum

with open('puzzle_1', 'r') as file :
    pazz = file.read().split('\n')

for word in pazz :
    print(word)

    valu = [e for e in word if e.isnumeric()]
    #
    # digits = extract_digits(word)
    # numbers = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine))|(\d)', word)
    # matches = [
    #     item[0] if item[0] != "" else item[1]
    #     for item in numbers
    #     if item[0] != "" or item[1] != ""
    # ]
    #
    # matches = [DIGITS[item] if item in DIGITS.keys() else item
    #            for item in matches]

    print(f'Extract: {valu}')

    if valu :
        calib_val = int(valu[0] + valu[-1])
        calib_vals.append(calib_val)
    #
    # if numbers:
    #     calib_val_2 = [int(numbers[0]  + numbers[-1])]
    #     calib_vals_2.append(calib_val_2)

    print(f'Valeur de calibration : {calib_val}')
    # print(f'Valeur de calibration : {calib_val_2}')
    print(f'Somme Total part 1 :{sum(calib_vals)}')
    # print(f'Somme Total_digit :{sum(calib_vals_2)}')
    # print(f'Somme totals : {sum(calib_vals + calib_val_2)}')

somme = calculate_sum(pazz)
print(f'Somme Total Part 2 :{somme}')


print(f'Advent of code day 1 by YmC')
