import math
"""sequence = [0,1]
while sequence[len(sequence)-1] < 4000000:
    number_1 = sequence[len(sequence)-1]
    number_2 = sequence[len(sequence)-2]
    next_number = number_1 + number_2
    sequence.append(next_number)
even_numbers = []
for number in sequence:
    if number%2==0:
        even_numbers.append(number)
print(sum(even_numbers))"""
"""import math
n = 600851475143
factor = 2
lastFactor = 1
while n>1:
    if n % factor == 0:
        lastFactor = factor
        n=n//factor
        while n%factor == 0 :
            n = n//factor
    factor = factor + 1
print(lastFactor)"""

largest_number = 9998001
palindromes = []
for num in range (10000, 9998001):
    if str(num) == str(num)[::-1]:
        palindromes.append(num)
print(palindromes)