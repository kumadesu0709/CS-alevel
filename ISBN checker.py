isbn = []
for count in range (1,14):
    isbn += input("Please enter your next digit of ISBN:")
calculated_digit = 0
count = 0
while count<12:
    calculated_digit = calculated_digit + int(isbn[count])
    count = count + 1
    calculated_digit = calculated_digit + int(isbn[count])*3
    count = count + 1
while calculated_digit >= 10:
    calculated_digit = calculated_digit - 10
calculated_digit = 10 - calculated_digit
if calculated_digit == 10:
    calculated_digit = 0
if calculated_digit == int(isbn[12]):
    print("Valid ISBN")
else:
    print("Invalid ISBN")




    