"""def descending_order(nums):
    # Bust a move right here
    numbers = []
    for num in str(nums):
        numbers += num
    descend = ""
    while len(numbers) >> 0:
        for number in numbers:
            descend = descend + str(max(numbers))
            numbers.remove(str(max(numbers)))
    return int(descend)
print(descending_order(3445433))"""

def duplicate_encode(word):
    #your code here
    letters = []
    for letter in word.lower():
        letters += letter
    letter_frequency = {}
    for letter in letters:
        if letter not in letter_frequency:
            letter_frequency[letter] = 1
        else:
            letter_frequency[letter] = letter_frequency[letter] + 1
    result = ""
    for letter in letters:
        if letter_frequency[letter] == 1:
            result += "("
        else:
            result += ")"
    return result
print(duplicate_encode("hello"))