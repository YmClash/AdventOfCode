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


    match =  pattern_1 and pattern_2  and not pattern_3
    if match:
        return ("NICE")
    else:
        return ("Match not found")

def nice_or_non(character:str):
    pattern_1 = search(r"(..).*\1", character)
    pattern_2 = search(r"(.).\1",character)

    match = pattern_1 and pattern_2
    if match:
        return ("NICE")
    else:
        return "NON"







match_1 = 0
unmatch_1 = 0
match_2 = 0
unmatch_2 = 0

MATCH_1 = []
UNMATCH_1 = []
MATCH_2 = []
UNMATCH_2 = []




with open('input.txt','r') as file:
    puzzle = file.read().splitlines()
    # print(puzzle)

for i ,line in enumerate(puzzle,start=1):
    print(f'{i} : {line}')
    print(nice_or_not(line))
    verdict = nice_or_not(line)
    if verdict == "NICE":
        match_1 += 1
        MATCH_1.append(line)
    else:
        unmatch_1 += 1
        UNMATCH_1.append(line)

for e ,ligne in enumerate(puzzle,start=1):
    print(f'{e} : {ligne}')
    print(nice_or_non(ligne))
    verdict = nice_or_non(ligne)
    if verdict == "NICE":
        match_2 += 1
        MATCH_2.append(ligne)
    else:
        unmatch_2 += 1
        UNMATCH_2.append(ligne)




print("---------------------Advent of code 2015--Day 5--------------------------------------\n")

print("woowowowoowowowoowowowowowowowowowowowowowowowowowowowowowowowowowowowoowowowowowowowowo")
print("Part 1: Done ")
print()
print(f'match: {match_1}')
print(f'unmatch: {unmatch_2}')
print("\n")
# print(MATCH)
print("MATCH LENGHT:",len(MATCH_1))
# print(UNMATCH)
print("UNMATCH LENGHT :",len(UNMATCH_2))

print("woowowowoowowowoowowowowowowowowowowowowowowowowowowowowowowowowowowowoowowowowowowowowo")
print("Part 2: Done ")
print()
print(f'match: {match_2}')
print(f'unmatch: {unmatch_2}')
print("\n")
# print(MATCH)
print("MATCH LENGHT:",len(MATCH_2))
# print(UNMATCH)
print("UNMATCH LENGHT :",len(UNMATCH_2))



# print(puzzle)
# print(len(puzzle))