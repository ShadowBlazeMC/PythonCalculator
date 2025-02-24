print("---PYTHON CALCULATOR---")
number1 = int(input("Enter your first number "))
calc = input("Enter your operator  ")
number2 = int(input("Enter your second number "))
if calc == "+":
    val = number1 + number2
elif calc == "-":
    val = number1 - number2
elif calc == "/":
    val = number1 / number2
elif calc == "*":
    val = number1 * number2
elif calc == "x":
    val = number1 * number2
elif calc == "m":
    val = number1 * number2
elif calc == "d":
    val = number1 / number2
elif calc == "a":
    val = number1 + number2
elif calc == "s":
    val = number1 - number2
elif calc == "**":
    val = number1 ** number2
elif calc == "p":
    val = number1 ** number2
elif calc == "mm":
    val = number1 ** number2
else:
    print("invalid operator, type a,s,m,d or p. Please restart code.")
print(val)