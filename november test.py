def two_words():
    fileName = 'words.txt'
    with open (fileName, 'rb') as file:
        pass
    word1 = input("Enter your first word:")
    word2 = input("Enter your second word:")
    word1_dict = {}
    word2_dict = {}
    for letter1 in word1:
        if letter1 in word1_dict:
            word1_dict[letter1] += 1
        else:
            word1_dict[letter1] = 1
    for letter2 in word2:
        if letter2 in word2_dict:
            word2_dict[letter2] += 1
        else:
            word2_dict[letter2] = 1
    can_create_word = True
    for letter in word1_dict:
        if letter not in word2_dict or word1_dict[letter] > word2_dict[letter]:
            can_create_word = False
    if can_create_word == True: 
        return "The first word can be created using the second word"
    if can_create_word == False:
        return "The first word can't be created using the second word"
    
print(two_words())
print(two_words())



"""def wordContains(word1: str, word2: str) -> bool:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_counts1 = [0] *26
    for i in range(26):
        for letter in word1:
            if letter == alphabet[i]:
                letter_counts1[i] += 1
    letter_counts2 = [0] * 26
    for i in range(26):
        for letter in word2:
            if letter == alphabet[i]:
                letter_counts2[i] +=1
    for i in range(26):
        if letter_counts1[i] > letter_counts2[i]:
            return False
        return True

def is_wordable(word1, word2):
    pool_of_letters = list(word2)
    first_word_letters = list(word1)
    for letter in first_word_letters:
        if letter in pool_of_letters:
            pool_of_letters.remove(letter)
        else:
            return False
        return True

def wordContains2(word1, word2)-> bool:
    for letter in set(word1):
        if word1.count(letter) > word2.count(letter):
            return False
        return True
word1 = input("Enter the first word:").upper()
word2 = input("Enter the second letter:").upper()
if wordContains2(word1,word2):
    print(f'You can make {word1} using {word2}')
else:
    print(f'You can NOT make {word1} using {word2}')"""

