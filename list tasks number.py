
first = input("put in your first number:")
second = input("put in your second number:")
third = input("put in your third number:")
forth = input("put in your forth number:")
fifth = input("put in your fifth number:")
biggestnumber = ""
if int(first) >= int(second) and int(first) >= int(third) and int(first) >= int(forth) and int(first) >= int(fifth):
    biggestnumber = first
if int(second) >= int(first) and int(second) >= int(third) and int(second) >= int(forth) and int(second) >= int(fifth):
    biggestnumber = second
if int(third) >= int(first) and int(third) >= int(second) and int(third) >= int(forth) and int(third) >= int(fifth):
    biggestnumber = third
if int(forth) >= int(first) and int(forth) >= int(second) and int(forth) >= int(third) and int(forth) >= int(fifth):
    biggestnumber = forth
if int(fifth) >= int(first) and int(fifth) >= int(second) and int(fifth) >= int(forth) and int(third) <= int(fifth):
    biggestnumber = fifth
print("the biggest number is " + biggestnumber)
smallest = ""
if int(first) <= int(second) and int(first) <= int(third) and int(first) <= int(forth) and int(first) <= int(fifth):
    smallest = first
if int(second) <= int(first) and int(second) <= int(third) and int(second) <= int(forth) and int(second) <= int(fifth):
    smallest = second
if int(third) <= int(first) and int(third) <= int(second) and int(third) <= int(forth) and int(third) <= int(fifth):
    smallest = third
if int(forth) <= int(first) and int(forth) <= int(second) and int(forth) <= int(third) and int(forth) <= int(fifth):
    smallest = forth
if int(fifth) <= int(first) and int(fifth) <= int(second) and int(fifth) <= int(forth) and int(third) <= int(fifth):
    smallest = fifth
print("the smallest number is " + smallest)
total = int(first) + int(second) + int(third) + int(forth) + int(fifth)
print("the total for these numbers is " + str(total))
mean = int(total)/5
print("the mean for these numbers is " + str(mean))