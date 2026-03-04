"""1) To check a number is odd or even """
# a=int(input("Enter a number:"))
# if a%2==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

"""2) Check the number is positive,negative or zero"""
# a=int(input("Enter a number:"))
# if a>=0:
#     if a==0:
#         print("the entered number is zero")
#     else:
#         print(f"{a} is a posive number")
# else:
#     print(f"{a} is a negative number")

"""3)Largest of two numbers"""
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# if a>b:
#     print(f"{a} is the largest number")
# else:
#    print(f"{b} is the largest number")

"""4) Largest of three numbers"""
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# if a>b and a>c:
#     print(f" {a}  is larger")
# elif b>c and b>a:
#     print(f" {b}  is larger")
# else:
#     print(f"{c} is larger")

"""5) Check the person is eligible to vote"""
# age=int(input("Enter the age:"))
# if age>=18:
#     print("The person is Eligible to vote")
# else:
#     print("The person is not Eligible to vote")

"""6) Check the student is passed or failed in the exam"""
# m=float(input("Enter the mark"))
# if m>=40:
#     print("passed")
# else:
#     print("failed")

"""7) find the grades"""
# m=int(input("Enter the mark:"))
# if m>90:
#     print("A grade")
# elif m>=80 and m<=89:
#     print("B grade")
# elif m>=70 and m<=79:
#     print("C grade")
# elif m>=60 and m<=69:
#     print("D grade")
# else:
#     print("fail")

"""8) Check the entered year is leap year or not"""
# year=int(input("Enter the year:"))
# if ((year%4==0 and year%100!=0) or year%400==0):
#     print("The entered year is a leap year")
# else:print("The entered year is not a leap year")

"""9) Check the number is divisible by both 5 and 11"""
# x=int(input("Enter a number:"))
# if x%5==0 and x%11==0:
#     print(f"the number {x} is divisible by both 5 and 11")
# elif x%11==0:
#     print(f"the number {x} is divisible by 11")
# else:
#     print(f"the number {x} is divisible by 5 ")

"""10) Check the entered character is a vowel or cosonant"""
# c=input("Enter a ckaracter:")
# if (c in "aeiou" or c in "AEIOU"):
#      print(f"The entered character {c} is a vowel")
# else:
#      print(f"The entered character {c} is a consonant")

"""11) login check"""
# user_name="Priyanka"
# password="1234"
# username=input("Enter a username:")
# pwd=input("Enter a password:")
# if username==user_name and pwd==password:
#     print("login successful")
# else:
#     print("login failed")

"""12) greater of two numbers"""
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# greater = f"{a} is greater" if a>b else f"{b} is greater"
# print (greater)

"""13) Check the temperature"""
# temp=int(input("Enter the temperature"))
# if temp>30:
#     print("Hot")
# elif temp>=20 and temp<=30:
#     print("warm")
# else:
#     print("cold")

"""14) check salary bonus and total salary"""
# salary=int(input("Enter the salary:"))
# print("the total salary is",salary+5000) if salary>50000 else print("the total salary is",salary+2000)

"""15) check shopping discount"""
# bamt=float(input("enter the bill amount:"))
# if bamt>1000:
#     total=bamt-(bamt*10)/100
#     print(f"bill={total}")
# else:
#     print(f"bill={bamt}")

"""16) Check the age category"""
# age=int(input("Enter the age:"))
# if age<13:
#     print("child")
# elif age>=13 and age<=19:
#     print("Teen")
# else:
#     print("Adult")

"""17) Electricity bill calculator"""
# units=int(input("Enter the units:"))
# if units<=100:
#     bill=units*2
#     print(f"bill amount={bill}")
# elif units>=101 and units<=200:
#     bill=units*3
#     print(f"bill amount={bill}")
# else:
#     bill=units*5
#     print(f"bill amount={bill}")

"""18) Check the number is multiple of 3 or 7"""
# n=int(input("enter a number"))
# if n%3==0 or n%7==0:
#     print(f"{n} is a mutiple of 3 or 7")
# else:
#     print(f"{n} is not a mutiple of 3 or 7 ")

"""19) Check the password strength"""
# pwdlen=int(input("Enter the password length:"))
# if pwdlen>=8:
#     print("strong password")
# else:
#     print("weak password")

"""20) ind the smallest of 2 numbers"""
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
smaller = f"{a} is smaller" if a<b else f"{b} is smaller"
print(smaller)























