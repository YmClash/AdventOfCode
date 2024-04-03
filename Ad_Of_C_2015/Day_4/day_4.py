import hashlib

key = 'bgvyzdsv'
key_2 = b'bgvyzdsv254575'
subkey = 0


def hex(key):
    md = hashlib.md5()
    md.update(key)
    hexa = md.hexdigest()
    return hexa


cle_1 = "00000"
cle_2 = "000000"

def bf(key_input,cle:str):
    brute_force = True
    subkey = 0

    while brute_force:
     key_input = key + str(subkey)
     hash_resultat = hex(key_input.encode())
     if hash_resultat.startswith(cle):
         # print(subkey)
         brute_force = False
         return subkey
     subkey += 1


print("---------------------Advent of code 2015--Day 4--------------------------------------\n")

print("Reponse part 1 : ")
print(f'Secret key : {key}')
haxa = hex(key.encode())
print(f'Secret key hexadecimal: {haxa}')
hash_key = bf(key,cle=cle_1)
print(f'Hash key : {hash_key}')
reponse = key+str(hash_key)
print("Reponse :",reponse)
new_hexa = hex(reponse.encode())
print("New Hex :",new_hexa)
print("\n")

print("Reponse part 2 : ")
print(f'Secret key : {key}')
haxa_2 = hex(key.encode())
print(f'Secret key hexadecimal: {haxa_2}')
hash_key_2 = bf(key,cle=cle_2)
print(f'Hash key : {hash_key_2}')
reponse_2 = key+str(hash_key_2)
print("Reponse :",reponse)
new_hexa_2 = hex(reponse_2.encode())
print("New Hex :",new_hexa_2)











#
#
#
# print(hex(key_2))


#
#
# hex = hex(key_2)
# print(hex)
# print(hex[:5])
# print(len(hex))
# print(type(hex))