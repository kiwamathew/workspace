#code/program to intepret.
num1 = int(input("input your first number: "))
num2 = int(input("input your second number: "))

#operator = input("choose the operator: ")

#if statement ends with a full colon.
if num1 >= num2: 
#After the if statement, the following statement starts after four indents.
    print("Error: First number should be less than the second number.")
#
if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")
#
if num1 != 0:
    num2 += num1
    print(num2)