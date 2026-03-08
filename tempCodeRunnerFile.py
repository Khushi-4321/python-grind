try:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    result = num1/num2
except ValueError: 
    print("Enter a integer")
except ZeroDivisionError:
    print("Cannot divide by zero")