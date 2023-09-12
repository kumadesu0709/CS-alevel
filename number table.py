x = input ("Which number would you like to check")
for y in range(1,13):
    answer = y * int(x)
    print( str(y) + "X" + str(x) + "=" + str(answer))