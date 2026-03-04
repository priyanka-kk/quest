"""triangle types based on sides"""
# a=int(input("Enter first side:"))
# b=int(input("Enter second side:"))
# c=int(input("Entethird side:"))
# if a==b==c:
#     print("Equilateral triangle") 
# elif a==b or a==c or b==c:
#     print("Isosceles triangle") 
# else:
#     print("Scalene triangle")

"""21. Implement a simple calculator (+, -, *, /) using if-elif-else."""
n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
operator=input("Enter the operator:")
if operator== "+":
    total=n1+n2
    print(f"the sum is {n1+n2}")
elif operator=="-":
    differnce=n1-n2
    print(f"the differnce is {n1-n2}")
elif operator== "*":
    product=n1*n2
    print(f"the product is {n1*n2}")
elif operator== "/":
    if n2!=0:
        quotient=n1/n2
        print(f"the quotient is {n1/n2}")
    else:
        print("The division by zero is not defined")
else:
    print("invalid operator")
        

    