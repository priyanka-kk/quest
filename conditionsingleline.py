"""Even and odd number"""
# num1 = int(input("Please enter a number:"))
# x= "Even number" if num1%2==0 else "Odd number"
# print(x)

"""largest of two numbers"""
# num1 = int(input("Please enter first number:"))
# num2 = int(input("Please enter second number:"))
# Large = "First numbe is largerr" if num1>num2 else "Second Number is larger"
# print (Large)

"""largeest of three numbers"""

num1 = int(input("Please enter first number:"))
num2 = int(input("Please enter second number:"))
num3 = int(input("Please enter third number:"))
x = num1 if num1>num2 and num1>num3 else(num2 if num2>num1 and num2>num3 else num3)
print(f"The larger number is {x}")