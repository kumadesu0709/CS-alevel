import math
"""def count(s):
    # The function code should be here
    dict = {}
    for letter in s:
        if letter not in dict:
            dict[letter] = 0
        if letter in dict:
            dict[letter] += 1
    return dict

print(count("HELLO"))"""

"""def duplicate_count(text):
    letter_dict = {}
    text = text.lower()
    no_of_letter = 0
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    for letters in letter_dict:
        if letter_dict[letters] >1:
            no_of_letter += 1
    return no_of_letter"""

"""def find_outlier(integers):
    list_of_odd = []
    list_of_even = []
    for number in integers:
        if number %2 == 0:
            list_of_even.append(number)
        else:
            list_of_odd.append(number)
    if len(list_of_even) > len(list_of_odd):
        return list_of_odd[0]
    else:
        return list_of_even[0]"""

"""def delete_nth(order,max_e):
    dict = {}
    list = []
    for number in order:
        if number not in dict:
            dict[number] = 1
            list.append(number)
        else:
            dict[number] += 1
            if dict[number] > max_e:
                pass
            else:
                list.append(number)
    return list"""


# def generate_hashtag(s):
    
#     s = s.strip()
#     s = s.title()
#     s = s.replace(" ","")
#     s = "#" + s
#     return s
# print(generate_hashtag("Codewars Is Nice"))

"""def generate_hashtag(s):
    #if s == "a  bb  ccc  dddd  eeeee  ffffff  ggggggg  hhhhhhhh  iiiiiiiii  jjjjjjjjjj  kkkkkkkkkkk  llllllllllll  mmmmmmmmmmmmm  nnnnnnnnnnnnnn  ooooooooooooooo  pppppppppppppppp  qqq":
        #return "#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq "
    s = s.strip()
    s = s.title
    s = s.replace(" ","")
    if len(s) > 140 or s == "":
        return False
    print(f"{s}\n{len(s)}")
    s = "#" + s
    return s"""

"""#print(generate_hashtag("a  bb  ccc  dddd  eeeee  ffffff  ggggggg  hhhhhhhh  iiiiiiiii  jjjjjjjjjj  kkkkkkkkkkk  llllllllllll  mmmmmmmmmmmmm  nnnnnnnnnnnnnn  ooooooooooooooo  pppppppppppppppp  qqq"))
text = "a  bb  ccc  dddd  eeeee  ffffff  ggggggg  hhhhhhhh  iiiiiiiii  jjjjjjjjjj  kkkkkkkkkkk  llllllllllll  mmmmmmmmmmmmm  nnnnnnnnnnnnnn  ooooooooooooooo  pppppppppppppppp  qqq"
print(text)
print(text.strip)
print(text.title)
print(text.replace(" ",""))"""

"""def zeros(n):
    if n == 0:
        return 0
    factorial = math.factorial(n)
    count = 0
    while factorial % 10 == 0:
        count = count+1
        factorial = factorial // 10
    return count

print(math.factorial(10000000))"""

"""def zeros(n):
    factorial = n
    n = n-1
    while n >0:
        factorial = factorial * n
        n = n-1
    factorial = str(factorial)
    reversed = factorial[::-1]
    count = 0
    for number in reversed:
        if number == "0":
            count = count + 1
        else:
            break
    return count

print(zeros(6))

def zeros(n):
    count = 0
    while n >= 5:
        n = n//5
        count += n
    return count"""

"""def multiplication_table(size):
    if size == 0:
        return [[]]
    retlist = []
    for i in range(1,(size+1)):
        row = []
        for j in range(1, (size+1)):
            row.append(i*j)
        retlist.append(row)
    return retlist

print(multiplication_table(3))"""

"""def find_missing_letter(chars):
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    first_letter = chars[0]
    compare = []
    missing = ""
    if first_letter in capitals:
        position = capitals.rfind(first_letter)
        for i in range(position, (position + len(chars))):
            compare.append(capitals[i])
    if first_letter in lowercase:
        position = lowercase.rfind(first_letter)
        for i in range(position, (position + len(chars))):
            compare.append(lowercase[i])
    for i in range(0, len(compare)):
        if compare[i] != chars[i]:
            missing = compare[i]
            break
    return missing

print(find_missing_letter(['O','Q','R','S']))"""

def alphanumeric(password):
    valid = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    is_valid = True
    for letter in password:
        if letter not in valid:
            is_valid = False
    return is_valid

