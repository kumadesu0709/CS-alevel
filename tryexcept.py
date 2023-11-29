usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    division = 301 / number
    print(f"301 divided by {number} = {division}")


def login_handled(usernumber):
    print("\n -- The Better Version --\n")
    try:
        number = int(usernumber)
    except ValueError:
        print("This is not a valid number...")
        number = 2
    try:
        user = usernames[number]
    except IndexError:
        print("User doesn't exist")
        user = 'unknown'
    print("Welcome", usernames[number], "user number", number,".")
    try:
        division = 301 / number
    except ZeroDivisionError:
        print("Don't divide a number by 0...")
        division = "is not really a number..."
    print(f"301 divided by {number} = {division}")



def login_handled2(usernumber):
    print("\n -- The Better Version --\n")
    if usernumber.isdigit() == False:
        return print("Don't divide a number by a string...")
    number = int(usernumber)
    if number >5:
        return print(f"User {number} doesn't exist...")
    print("Welcome", usernames[number], "user number", number,".")
    if number == 0:
        return print("Don't try to divide a number by 0...")
    division = 301 / number
    print(f"301 divided by {number} = {division}")

while True:
    inp = input("\nType in a number: ")
    login_handled2(inp)
