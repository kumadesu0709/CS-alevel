import random
import time
x = str(random.randint(1000,9999)) #generating random number
easyornot = str(input("would you like to turn on easy mode (answer yes or no):"))
tries = 0
print(x)
l2 = []
l4 = []
for nc in (x):
    l2 = l2 + [nc]
if easyornot == "no":
    while True:
        tries = tries + 1
        y = str(input("guess a 4 digit number:"))#allowing player to input
        correct_number = 0
        l1 = []
        for ng in (y):
            l1 = l1 + [ng]
        if l1 == l2:
            break
        for z in range (0,4):
            if l1[z] == l2[0] or l1[z] == l2[1] or l1[z] == l2[2] or l1[z] == l2[3]:
                correct_number = correct_number + 1
        print("You haven't guess the correct number, but " + str(correct_number) + " of your numbers are correct. Try again...")
        time.sleep(3)
    print ("Congrates! You've guessed it right! This takes you " + str(tries) + " tries!")
if easyornot == "yes":
    while True:
        tries = tries + 1
        y = str(input("guess a 4 digit number:"))#allowing player to input
        correct_number = 0
        correct_digit = " "
        iscorrect = " is correct"
        l1 = []
        for ng in (y):
            l1 = l1 + [ng]
        if l1 == l2:
            break
        for z in range (0,4):
            if l1[z] == l2[0] or l1[z] == l2[1] or l1[z] == l2[2] or l1[z] == l2[3]:
                correct_number = correct_number + 1
        if l1[0] == l2[0]:
            correct_digit = correct_digit + " your first digit,"
        if l1[1] == l2[1]:
            correct_digit = correct_digit + " your second digit,"
        if l1[2] == l2[2]:
            correct_digit = correct_digit + " your third digit,"
        if l1[3] == l2[3]:
            correct_digit = correct_digit + " your forth digit"
        if l1[0] != l2[0] and l1[1] != l2[1] and l1[2] != l2[2] and l1[3] != l2[3]:
            iscorrect = " none of your digits is correct"
            correct_number = "none"

        if correct_number == "none": 
            print("You haven't guess the correct number, and none of your numbers is correct")
            time.sleep(3)
        if correct_number != "none":
            print("You haven't guess the correct number, but " + str(correct_number) + " of your numbers are correct, and " + correct_digit + "Try again...")
            time.sleep(3)
    print ("Congrates! You've guessed it right! This takes you " + str(tries) + " tries!")