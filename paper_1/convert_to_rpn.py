import re

def ConvertToRPN(UserInput):
    Position = 0
    Precedence = {"+": 2, "-": 2, "*": 4, "/": 4}
    Operators = []
    Operand, Position = GetNumberFromUserInput(UserInput, Position)
    UserInputInRPN = []
    UserInputInRPN.append(str(Operand))
    Operators.append(UserInput[Position - 1])
    while Position < len(UserInput):
        Operand, Position = GetNumberFromUserInput(UserInput, Position)
        UserInputInRPN.append(str(Operand))
        if Position < len(UserInput):
            CurrentOperator = UserInput[Position - 1]
            while len(Operators) > 0 and Precedence[Operators[-1]] > Precedence[CurrentOperator]:
                UserInputInRPN.append(Operators[-1])
                Operators.pop()                
            if len(Operators) > 0 and Precedence[Operators[-1]] == Precedence[CurrentOperator]:
                UserInputInRPN.append(Operators[-1])
                Operators.pop()    
            Operators.append(CurrentOperator)
        else:
            while len(Operators) > 0:
                UserInputInRPN.append(Operators[-1])
                Operators.pop()
    return UserInputInRPN

def GetNumberFromUserInput(UserInput, Position):
    Number = ""
    MoreDigits = True
    while MoreDigits:
        if not(re.search("[0-9]", str(UserInput[Position])) is None):
            Number += UserInput[Position]
        else:
            MoreDigits = False            
        Position += 1
        if Position == len(UserInput):
            MoreDigits = False
    if Number == "":
        return -1, Position
    else:
        return int(Number), Position    

def EvaluateRPN(UserInputInRPN):
    operator = ["+","-","*","/"]
    stack = []
    for i in range (len(UserInputInRPN)):
        if UserInputInRPN[i] not in operator:
            stack.append(UserInputInRPN[i])
        else:
            num_one = int(stack.pop())
            num_two = int(stack.pop())
            if UserInputInRPN[i] == "+":
                stack.append(float(num_one+num_two))
            elif UserInputInRPN[i] == "-":
                stack.append(float(num_two-num_one))
            elif UserInputInRPN[i] == "*":
                stack.append(float(num_two*num_one))
            elif UserInputInRPN[i] == "/":
                number = num_two/num_one
                if int(number) != number:
                    return "Result is not an integer."
                else:
                    stack.append(float(num_two/num_one))
    if len(stack) == 1:
        return stack[0]
    else:
        return "More than one number left in stack. Please Check."

while True:
    inp = input("Input: ")
    print("RPN:", ConvertToRPN(inp))
    print("Evaluated:", EvaluateRPN(ConvertToRPN(inp)))