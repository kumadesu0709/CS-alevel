#filename = "text.txt"
#file = open(filename, 'w')#may choose "w" (i.e. write), "a"(i.e. append), "r"(i.e. read)
#file.write("testing...")
#file.close()

#filename="test"
#file = open(filename, "wb")
#int_list = [x for x in range(256)]
#print("Int list:", int_list)
#file.write(bytes(int_list))
#file.close

filename = "Squidward.txt"
#with open(filename, 'r') as file:
    #text = file.read() #readlines = deconstructed in a line(?), readline = first line of the text, read = return the entire text as a string
    #print(text)

with open(filename, "r") as file:
    for line in file:
        print(line, end = "")