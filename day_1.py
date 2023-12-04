import string


calib_vals = []
calib_vals_2 = []
DIGITS = {'0':'zero',
          '1':'one',
          '2':'two',
          '3':'three',
          '4':'four',
          '5':'five',
          '6':'six',
          '7':'seven',
          '8':'eight',
          '9':'nine'
          }

with open('puzzle_1','r') as file:
    pazz = file.read().split('\n')


for word in pazz:
    print(word)

    valu = [e for e in word if a.isnumeric()]
    valu_2 = []
    print(f'Extract: {valu}')

    if valu:
        calib_val = int(valu[0] + valu[-1])
        calib_vals.append(calib_val)


    print(f'Valeur de calibration : {calib_val}')
    print(f'Somme Total :{sum(calib_vals)}')




