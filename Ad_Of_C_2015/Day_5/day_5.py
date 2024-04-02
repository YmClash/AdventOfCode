from re import search


text  = "Hello World 9"
pattern = r'[\d+]'

match = search(pattern,text)
if match:
    print("Match Found")
else:
    print('Match not Found')


def nice_or_not(character:str):
    pattern_1 = "([aeiou].*){3}"
    pattern_2 = r"(.)\1"
    pattern_3 = "ab|cd|pq|xy"

    match = search()



with open('test.txt','r') as file:
    puzzle = file.read().splitlines()
    # print(puzzle)

for i ,line in enumerate(puzzle,start=1):
    print(f'{i} : {line}')
# print(puzzle)
print(len(puzzle))