def CarMatch(x):
    CapitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Numbers = "1234567890" 
    space = " "
    valid_or_not = ""
    if len(x) != 8:
        valid_or_not = "No"
    if x[0] in CapitalLetters and x[1] in CapitalLetters and x[2] in Numbers and x[3] in Numbers and x[4] == space and x[5] in CapitalLetters and x[6] in CapitalLetters and x[7] in CapitalLetters:
        valid_or_not = "Yes"
    else:
        valid_or_not = "No"
    return valid_or_not
def validate_car():
    tests = [('AB12 CDE', True),
             ('AB1234455', False),
             ('CD34 HFE', True),
             ('EI39 EFH', True),
             ("DE98 UHE", True),
             ('de98 uhe', False),
             ("EDUHED", False)]
    for test in tests:
        message = f"Validating {test[0]}, Expecting: "
        returnResult = ""
        result = CarMatch(test[0])
        if test[1]:
            message += "True"
            if result == "No":
                returnResult += "ERROR"
            else:
                returnResult += "Pass"
        else:
            message += "False"
            if result == "No":
                returnResult += "Pass"
            else:
                returnResult += "ERROR"
        print(f"{message}\n{returnResult}\n")
validate_car()