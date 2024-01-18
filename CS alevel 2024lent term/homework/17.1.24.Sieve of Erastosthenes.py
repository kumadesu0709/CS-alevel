max_number = 10000
prime_bools = [True] * (max_number+1)
prime_bools[0] == False
prime_bools[1] == False
for i in range (2, max_number):
    if prime_bools[i] == True:
        for j in range (2,(max_number//2+1)):
            multiple = j * i
            if multiple <= max_number:
                prime_bools[multiple] = False
for item in range (2, len(prime_bools)):
    if prime_bools[item] == True:
        print(item)