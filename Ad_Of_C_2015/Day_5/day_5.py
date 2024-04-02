from re import search


# text  = "Hello World 9"
# text_2 = "toure@mohamed.mc"
# pattern = r'[\d+]'
# yes_or_not = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#
#
# match = search(yes_or_not,text_2)
# if match:
#     print("Match Found")
# else:
#     print('Match not Found')


def nice_or_not(character:str):
    pattern_1 = search("([aeiou].*){3}",character)
    pattern_2 = search(r"(.)\1",character)
    pattern_3 = search("ab|cd|pq|xy",character)
    # pattern_uni = if search(pattern_1,character) and search(pattern_2,character) and not search(pattern_3,character):


    match =  search(pattern_1,character) and search(pattern_2,character) and not pattern_3
    if match:
        return ("NICE")
    else:
        return ("Match not found")


match = 0
unmatch = 0
MATCH = []
UNMATCH = []



with open('test.txt','r') as file:
    puzzle = file.read().splitlines()
    # print(puzzle)

for i ,line in enumerate(puzzle,start=1):
    print(f'{i} : {line}')

    # verdict = nice_or_not(line)
    if search("([aeiou].*){3}",line) and search(r"(.)\1",line) and not  search("ab|cd|pq|xy",line):
        print("Nice")
        match += 1
        MATCH.append(line)
    else:
        print("Unmatch")
        unmatch += 1
        UNMATCH.append(line)


print(f'match: {match}')
print(f'unmatch: {unmatch}')
print(MATCH)
print("MATCH LENGHT:",len(MATCH))
print(UNMATCH)
print("UNMATCH LENGHT :",len(UNMATCH))

# print(puzzle)
print(len(puzzle))