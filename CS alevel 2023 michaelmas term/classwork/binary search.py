
def binary_search(item,list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    item_found = False
    lower = 0
    upper = len(list) - 1
    item_in_list = ""
    while (not item_found):
        midpoint = ((lower + upper) // 2)
        item_in_list = list[int(midpoint)]
        if item_in_list == item:
            item_found = True
        elif lower == upper:
            break
        else:
            first_letter_in_item = item[0].lower()
            first_letter_in_item_list = item_in_list[0].lower()
            if first_letter_in_item == first_letter_in_item_list:
                break
            for i in range (0,26):
                if alphabet[i] == first_letter_in_item:
                    first_letter_in_item = i
                    break
            for i in range (0,26):
                if alphabet[i] == first_letter_in_item_list:
                    first_letter_in_item_list = i
                    break
            if int(first_letter_in_item) > int(first_letter_in_item_list):
                lower = midpoint + 1
            if int(first_letter_in_item) < int(first_letter_in_item_list):
                upper = midpoint - 1
    return item_found

if binary_search("thing",["aardvark","bird","cat","dog","elephant","fish","giraff"]) == True:
    print("YAY")
if binary_search("thing",["aardvark","bird","cat","dog","elephant","fish","giraff"]) == False:
    print("BNO")
        

