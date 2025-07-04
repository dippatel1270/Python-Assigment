# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
try :
    num1 = int(input("Enter the number1 : "))
    num2 = int(input("Enter the number2 : "))
    ans = num1/num2
    print(ans)

except ZeroDivisionError:
    print("In zerodivition error")

except ValueError :
    print("Invalid input")

# Write a Python program to demonstrate handling multiple exceptions.
try :
    num1 = int(input("Enter the number1 : "))
    num2 = int(input("Enter the number2 : "))
    ans = num1/num2
    print(ans) 

except ZeroDivisionError:
    print("In zerodivition error")

except ValueError :
    print("Invalid input")

else :
    print("in else ")

finally :
    print("The end")
