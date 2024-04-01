import hashlib

key = 'bgvyzdsv'
key_2 = b'bgvyzdsv254575'
subkey = 0


def hex(key):
    md = hashlib.md5()
    md.update(key)
    hexa = md.hexdigest()
    return hexa

def bf(key_input):
    brute_force = True
    subkey = 0

    while brute_force:
     key_input = key + str(subkey)
     hash_resultat = hex(key_input.encode())
     if hash_resultat.startswith("00000"):
         # print(subkey)
         brute_force = False
         return subkey
     subkey += 1


print("Reponse part 1 : ")
print(f'Secret key : {key}')
haxa = hex(key.encode())
print(f'Secret key hexadecimal: {haxa}')
hash_key = bf(key)
print(f'Hash key : {hash_key}')
reponse = key+str(hash_key)
print("Reponse :",reponse)
new_hexa = hex(reponse.encode())
print("New Hex :",new_hexa)











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