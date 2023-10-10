def ReadAndDisplay(filename):
    with open(filename, 'r') as file:
        text = file.read()
        print(text)

def AppendThings(filename):
    file = open(filename, "w")
    thing=""
    things=[]
    while True:
        if thing == "I'm done":
            break
        else:
            thing = input("What would you like to add into the file (if done, type I'm done)")
            things.append(thing)
    things.remove("I'm done")
    for i in things:
        file.write(i)
        file.write("\n")
ViewOrWrite = ""
while ViewOrWrite != "I want to quit":
    ViewOrWrite = input("Would you like to view or write a file?(answer view or write, or I want to quit)")
    if ViewOrWrite == "view":
        filename = input("name your file:")
        print(ReadAndDisplay(filename))
    if ViewOrWrite == "write":
        filename = input("name your file:")
        print(AppendThings(filename))