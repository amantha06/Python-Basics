
num1 = float(input("Enter your number here: "))
oper = input("What operation do you want to use? Use either +, -, *, /:  ")
num2 = float(input("Enter your second number here: "))

if(oper == "+"):
    print(num1 + num2)
elif(oper == "-"):
    print(num1 - num2)
elif(oper == "*"):
    print(num1 * num2)
elif(oper == "/"):
    print(num1 / num2)
else:
    print("no valid operator, please use +, -, *, / ")