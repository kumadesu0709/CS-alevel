"""import random

total_points = 0
in_circle = 0
for i in range (0,9999999):
    x = random.random()
    y = random.random()
    magnitude = x ** 2 + y ** 2
    magnitude = magnitude ** 0.5
    if magnitude < 1:
        in_circle = in_circle +1
    total_points = total_points + 1
ratio = in_circle/total_points
pi = ratio * 4
print(pi)""" #monte carlo method

"""pi/4 = 1 - 1/3 + 1/5 - 1-7.."""
"""
def minusing_number(limit):
    minus = []
    first = 3
    while first < limit:
        minus.append(1/first)
        first = first + 4
    return minus

def plussing_number(limit):
    plus = []
    first = 1
    while first < limit:
        plus.append(1/first)
        first = first + 4
    return plus

minus_number = minusing_number(100000)
plus_number = plussing_number(100000)
result = 0
for number in plus_number:
    result = result + number
for number in minus_number:
    result = result - number
print(result*4)"""

#wallis product

n = 1
limit = 99999999
result = 1
while n < limit:
    first = 2*n/(2*n-1)
    second = 2*n/(2*n+1)
    result = result * first * second
    n = n + 1
print(2*result)

