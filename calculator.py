from calculator_function import calculator
first_input = input("Enter the first number")
second_input = input("enter the second input")
operator=input("Enter the operator")
value,operator = calculator(int(first_input),int(second_input),operator)
print("The calculated value of "+first_input +' ' +operator+' ' +second_input +' ='+str(value))
