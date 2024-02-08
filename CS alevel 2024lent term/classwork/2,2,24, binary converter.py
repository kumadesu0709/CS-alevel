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

print(convert_decimal_to_hex(999999999999999999))