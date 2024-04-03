from re import search


def match_or_not(character:str):
    pattern_1 = search(r"(..).*\1",character)
    pattern_2 = search(r"(.).\1",character)

    match = pattern_1 and pattern_2
    if match :
        return "MATCH"
    else:
        return "NOT MATCH"

with open('input.txt','r') as file :
    puzzle = file.read().splitlines()

count = 0
for i , line in enumerate(puzzle,start=1):
    print(i,line ,sep=":")
    print(match_or_not(line))
    verdict = match_or_not(line)
    if verdict == "MATCH":
        count +=1
    else:
        pass

print(f'MATCH {count}')


