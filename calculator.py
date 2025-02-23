print("---PYTHON CALCULATOR---")
number1 = int(input("Enter your first number "))
calc = input("Enter your operator  ")
number2 = int(input("Enter your second number "))
if calc == "+""a" :
    val = number1 + number2
elif calc == "-":
    val = number1 - number2
elif calc == "/":
    val = number1 / number2
elif calc == "*":
    val = number1 * number2
else:
    print("invalid operator, please restart code.")
print(val)