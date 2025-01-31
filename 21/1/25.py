import ast
def evaluate_rpn(number_list : list):
    operators = ["+","-","*","/"]
    for i in range (len(number_list)):
        if number_list[i] in operators:
            operator = number_list[i:len(number_list)]
            numbers = number_list[0:i]
            break
    while len(numbers) > 1:
        if operator[0] == "+":
            add_on = ast.literal_eval(numbers[len(numbers)-1]) + ast.literal_eval(numbers[len(numbers)-2])
        elif operator[0] == "-":
            add_on = ast.literal_eval(numbers[len(numbers)-1]) - ast.literal_eval(numbers[len(numbers)-2])
        elif operator[0] == "*":
            add_on = ast.literal_eval(numbers[len(numbers)-1]) * ast.literal_eval(numbers[len(numbers)-2])
        elif operator[0] == "/":
            add_on = ast.literal_eval(numbers[len(numbers)-1]) / ast.literal_eval(numbers[len(numbers)-2])
        add_on = (ast.literal_eval(operator[0]))(ast.literal_eval(numbers[len(numbers)-1]), ast.literal_eval(numbers[len(numbers)-2]))
        operator.pop(0)
        numbers.pop()
        numbers.pop()
        numbers.append(str(add_on))
    return numbers

#print(evaluate_rpn(["8","7","10","+","*"]))

def evaluate(expr):
    stack = []
    while len(expr) != 0:
        if expr[0] in ["+","-","*","/"]:
            op = expr.pop(0)
            n1 = float(stack.pop(-1))
            print(n1)
            n2 = float(stack.pop(-1))
            print(n2)
            if op == "+":
                result = n1 + n2
            elif op == "-":
                result = n1 - n2
            elif op == "*":
                result = n1 * n2
            elif op == "/":
                result = n1 / n2
            stack.append(str(result))
        else:
            stack.append(expr.pop(0))
    return float(stack[0])

print(evaluate(["8","7","10","+","*"]))