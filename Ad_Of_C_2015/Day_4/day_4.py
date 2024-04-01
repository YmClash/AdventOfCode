import hashlib



def hex(key):
    md = hashlib.md5()
    md.update(key)
    hexa = md.hexdigest()
    return hexa

key = b'bgvyzdsv'
key_2 = b'pqrstuv1048970'
subkey = str
key_3 = b'bgvyzdsvs'+str(subkey[0])
print(key_3)


brute_force = True

while brute_force:
    subkey += 1



hex = hex(key_2)
print(hex)
print(hex[:5])
print(len(hex))
print(type(hex))