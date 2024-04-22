orig_denary = int(input("what denary number would you like to convert?"))
denary = orig_denary
binary = ""
while denary > 0:
    denary = denary //2
    binary = binary + str(orig_denary%2)
    orig_denary = denary
print(f'The binary equivalent of this number is {binary}')