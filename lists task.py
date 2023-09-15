name_list = ['Ed', 'William', 'Toby', 'Freddie', 'Rohan', 'Ian', 'Matthew', 'Gavin', 'Lenny', 'Thomas', 'Jake']

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(", ".join(name_list[:-1]) + ' and ' + name_list[-1])
print("The third name is: " + name_list[2])
last_seven = []
for i in range(7,14):
    last_seven.append(name_list[i])
print("The last seven names are " + str(last_seven))
