import re

def extract_digits(word):
    for digit_word, digit in DIGITS.items():
        word = word.replace(digit_word, digit)
    return  [char for char in word if char.isdigit()]


calib_vals = []


DIGITS = {'zero':'0',
          'one':'1',
          'two':'2',
          'three':'3',
          'four':'4',
          'five':'5',
          'six':'6',
          'seven':'7',
          'eight':'8',
          'nine':'9'}


lettre = ['two1nine',
          'eightwothree',
          'abcone2threexyz',
          'xtwone3four',
          '4nineeightseven2',
          'zoneight234',
          '7pqrstsixteen']

lettre_1 =['eightwothree',
           'xtwone3four',]

for word in lettre_1:
    print(word)

    digits = extract_digits(word)

    if digits:
        calib_val = int(digits[0]  + digits[-1])
        calib_vals.append(calib_val)

    print(f'Mot: {word}')
    print(f'Extract: {digits}')
    print(f'Valeur de calibration : {calib_val}')
    print(f'Somme Total : " {sum(calib_vals)}')



print(f'Somme Total : {sum(calib_vals)}')