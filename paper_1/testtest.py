import bracket as br

# print(tc.ConvertToRPN("2+4"))
tests = [("8*(2+2)", "8 2 2 + *"),
         ("(5+1)*8", "5 1 + 8 *")
         ]
         
for test in tests:
    infix = test[0]
    rpn_string = ' '.join(br.ConvertToRPN(test[0]))
    print(f'{infix:>25} => {rpn_string}')
    print(' '.join(br.ConvertToRPN(test[0])))
    assert test[1] == rpn_string
    assert br.ConvertToRPN(test[0]) == test[1].split(' ')
# print(tc.ConvertToRPN("(7*(1+3)+2)*3"))