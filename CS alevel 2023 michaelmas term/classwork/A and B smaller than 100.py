for a in range (1,100):
    for b in range (1,100):
        csquared = a**2 + b **2
        c = csquared**0.5
        if c.is_integer() == True:
            print(f'a={a},b={b},c={c}')

print("hi")