
def binary_search(item,list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    item_found = False
    lower = 0
    upper = len(list) - 1
    item_in_list = ""
    repeated_time = 0
    need_to_break = False
    while not item_found or need_to_break == True or repeated_time == len(list):
        midpoint = (lower + upper) // 2 + lower
        item_in_list = list[int(midpoint)]
        if item_in_list == item:
            item_found = True
        if midpoint == lower:
            if list[lower] == item:
                item_found = True
        else:
            first_letter_in_item = item[0].lower()
            first_letter_in_item_list = item_in_list[0].lower()
            if first_letter_in_item == first_letter_in_item_list:
                need_to_break == True
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
            repeated_time = repeated_time + 1
    return item_found

if binary_search("cat",["aardvark","bird","cat"]) == True:
    print("YAY")
        

