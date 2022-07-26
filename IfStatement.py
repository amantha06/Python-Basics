is_male = True
is_tall = True

if is_male and is_tall:
    print("You are male and tall ")
else:
    print("Nor male nor tall nor both")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num2:
        return num2
    else:
        return num3

print(max_num(5, 6, 2))
