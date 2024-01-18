"""other_number = True
while other_number == True:
    is_prime = True
    input_number = int(input("Input your number (bigger than 1):"))
    if input_number<=1:
        print("Your number is smaller or equal to 1.")
    if input_number>1:
        for i in range(2,int(input_number-1)):
            if input_number % i == 0:
                is_prime = False 
        if is_prime == True:
            print("Your number is a prime")
        if is_prime == False:
            print("Your number isn't a prime")
    like_another = input("Would you like to try another number? (Yes or No)")
    if like_another == "Yes":
        other_number == True
    else:
        break"""

"""def is_prime(number):
    for i in range(2,int(number -1)):
        if number % i == 0:
            return False
    return True

max_number = 100000
primes = []
for i in range (max_number):
    if is_prime(i) == True:
        primes.append(i)   
print(primes)"""

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



"""sieve_of_erastothenes"""