import re
#match = re.search(reg_exp, str)

#txt = "The rains in Spain falls mainly"

#match1 = re.search("H", txt) #finds the first match, returning match object + the position
#print(match1)
#match2 = re.findall("O", txt)
#print(match2)

#matches = re.finditer("L",txt)
#for match in matches:
    #print(match.group())
#match = re.search("[A-Za-z]{2}" ,txt)#the {2} means 2 consecutive
#print (match)
#texts = ["IW91 IEW", "EI00 IEF", "EREE ERD", "ABC12 DEF", "BC12 EUHE"]
#for text in texts:
    #match = re.search("^[A-Z]{2}[0-9]{2} [A-Z]{3}$",text)#^ is matching the start of the string, $ is matching the end of the string
    #if match != "None":
        #print(match)
def numMatch(x):
    y = str(x)
    return re.search("^[0-9]{1,3}(,[0-9]{3})*[.][0-9]{2}$", y)
def validate_number():
    tests = [('123,456.78', True),
             ('1230.89', False),
             ('1,000,000.12', True),
             ('56.78', True),
             ("21,000,000.12", True),
             ('1,000,000.120', False),
             ("123,15.13", False)]
    for test in tests:
        message = f"Validating {test[0]}, Expecting: "
        returnResult = ""
        result = numMatch(test[0])
        if test[1]:
            message += "True"
            if result == None:
                returnResult += "ERROR"
            else:
                returnResult += "Pass"
        else:
            message += "False"
            if result == None:
                returnResult += "Pass"
            else:
                returnResult += "ERROR"
        print(f"{message}\n{returnResult}\n")
validate_number()