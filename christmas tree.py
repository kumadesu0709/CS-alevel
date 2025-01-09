number_of_layers = int(input("How many layers do you want?"))
string = ""

for number in range (number_of_layers):
    layer = ""
    for i in range (number+1):
        layer += "*"
        layer.center(30)
    string += layer
    string += "\n"
    

print(string)