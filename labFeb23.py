
# x = int (input("Please enter a number:"))
# s=0
# while x>0:
#     s=s+x%10
#     x=x//10

# print(f" {s}")

""" Amstrong number"""
# x = int (input("Please enter a number:"))
# pow=len(str(x))
# s=0
# num1=x
# while x>0:
#     s=s+(x%10)**pow
#     x=x//10

# if s==num1:
#     print(" amstrong num")
# else:
#     print ("not an amstrong num")

# print(f" {s}")

"""" first and last"""


# x = int (input("Please enter a number:"))
# a=x%10
# while x>0:
#     b=x
#     x=x//10

# print(f" {b} and {a}")

""" squre root"""

# x = int (input("Please enter a number:"))
# print(f" The squre root of the number is {x**0.5}")

"""age calculation"""
# name=input("Enter a name:")
# age=int(input("Enter the age:"))
# year=2026
# age=100-age
# year=year+age
# print(f"The year {name} turned in to 100years = {year}")

"""swapping of two numbers"""
# a=30
# b=45
# a,b=b,a
# print(a,b)

"""swapping of two numbers using a third variable"""
# a=30
# b=45
# temp=a
# a=b
# b=temp
# print(a,b)

"""Find the square and square root of a number"""
# n=int(input("Enter a number:"))
# square=n**2
# print(f"the square of the given number is {square}")
# sqroot=n**0.5
# print(f"the squareroot of the given number is {sqroot}")

"""Find the first and last digit of a number"""
# n=int(input("Enter a number:"))
# temp=n
# last_digit=temp%10
# while temp>=10:
#     temp//=10
# print(f"first digit is {temp}")
# print(f"The last digit is {last_digit}")

"""sum of digits of a number"""
# num=int(input("Enter a number:"))
# temp=num
# sum_num=0
# while temp>0:
#     digit=temp%10
#     sum_num+=digit
#     temp//=10
# print(f"The sum of digits are {sum_num} ")

"""amstrong number 153=1^3+5^3+3^3"""
# num=int(input("Enter a number:"))
# power=len(str(num))
# temp=num
# s_num=0
# while temp>0:
#     digit=temp%10
#     s_num+=digit**power
#     temp//=10
# if s_num==num:
#     print("Amstrong number")
# else:
#     print("Not an Amstrong number")

"""The given number is a palindrome number(reverse of the number=number) or not"""
num=int(input("Enter a number:"))
reverse=0
temp=num
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10
if reverse==num:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")









