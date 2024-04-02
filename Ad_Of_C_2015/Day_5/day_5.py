from re import search

with open('input.txt','r') as file:
    puzzle = file.read().splitlines()
    # print(puzzle)

for i ,line in enumerate(puzzle,start=1):
    print(f'{i} : {line}')
# print(puzzle)
print(len(puzzle))