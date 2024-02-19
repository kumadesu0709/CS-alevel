import math
def convert_binary(x:int):
    result = ""
    while True:
        if x == 0:
            break
        else:
            result = f'{x%2}' + result
            x = x //2
    return int(result)

#print(convert_binary(10))

def convert_any_base(x:int, base:int):
    result = ""
    while True:
        if x == 0:
            break
        else:
            result = f'{x%base}' + result
            x = x // base
    return int(result)

#print(convert_any_base(1010,10))

def convert_decimal_to_hex(x:int):
    hex_list = ["0",'1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return_list = []
    result = ""
    while True:
        if x == 0:
            break
        else:
            return_list.append(hex_list[x%16])
            x = x //16
    return_list.reverse()
    for letter in return_list:
        result += letter
    return result

def convert_fraction(x:float):
    f = x
    digits = []
    recurs = []
    flag = False
    while f != 0 and flag == False:
        r = f * 2
        d = math.trunc(r)
        if f not in recurs:
            recurs.append(f)
        elif f in recurs:
            flag == True
            break   
        if d == 1:
            f = round((r - 1),2)
            digits.append(1)
        elif d == 0:
            f = r
            digits.append(0)
    adding_string = " "
    if flag == True:
        position = recurs.index(f)
        if position == 0:
            for i in range (1,len(digits)):
                adding_string += str(digits[i])
        else:
            for i in range (position,len(digits)):
                adding_string += str(digits[i])
    returnstring = "."
    for digit in digits:
        returnstring += str(digit)
    if adding_string != " ":
        returnstring += adding_string
        returnstring += "recurring"
    return returnstring

print(convert_fraction(0.5))


