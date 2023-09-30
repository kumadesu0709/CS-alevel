import re
filename = "dracula.txt"
#with open(filename, "r") as text:
   # matches = re.finditer("([A-Z]\w+)", text.read())#the "?:"

   # count = 0
    #for match in matches:
        #count += 1
        #print(match.span())#location
        #print(match.groups())#thing that's found
    #print(f'{count} matches found.')
    #for matche in startofsentence:
       # print(matche.group())

with open(filename, "r") as text:
    re_capitalised = "(([^.!?] )([A-Z]\w+))"

    matches = re.finditer(re_capitalised, text)

    proper_nouns = set()
    for match in matches:
        for group in match.groups():
            proper_nouns.add(group)
    print(proper_nouns)
    print(len(proper_nouns))