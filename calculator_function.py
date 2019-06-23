def calculator(a,b,operator):
    flag=True
    while(flag):
        if operator is '+':
            return a+b,operator
            break
        elif operator is '-':
            return a-b,operator
            break
        elif operator is '/':
            return a/b,operator
            break
        elif operator is '*':
            return a*b,operator
            break
        else:
            operator =input("enter a valid operator")
