# pi=3.14
# def greet(name):
#     return f"welcome {name}"

# from testmodule import pi,greet
# print(pi)

# import math
# print(math.pi)
# print(math.sqrt(36))
# print(math.pow(2,3))
# print(math.factorial(5))
# print(math.ceil(3.25))
# print(math.floor(3.2z5))
# print(math.fabs(-7.5))
# print(math.trunc(3.25))
# print(math.trunc(3.60))

"""datetime()"""
from datetime import *
# print("Current Date and Time :",datetime.now()) #2026-05-07 20:55:23.381807
# print("Current Year :",datetime.now().year) #2026
# print("Current month :",datetime.now().month) #5
# print("Current day :",datetime.now().day) #7
# print(date.today()) #2026-05-07
# print(date.month)
# print("Current time :",datetime.now().time()) # 21:24:37.931912
# print("Current hour :",datetime.now().hour) #21
# print("Current minute :",datetime.now().minute) #33
# print("Current second :",datetime.now().second) #38
# print("Current microsecond :",datetime.now().microsecond) 
# dt=datetime.now()
# print(dt)
# print("%Y",dt.strftime("%Y")) #2026
# print("%y",dt.strftime("%y")) #26
# print("%m",dt.strftime("%m")) #05
# print("%B",dt.strftime("%B")) #May-Full month name
# print("%b",dt.strftime("%b")) #May
# print("%d",dt.strftime("%d")) #07-date
# print("%A",dt.strftime("%A")) #Thursday
# print("%a",dt.strftime("%a")) #Thu
# print("%H",dt.strftime("%H")) #21
# print("%I",dt.strftime("%I")) #09
# print("%p",dt.strftime("%p")) #pm
# print("%M",dt.strftime("%M")) #57
# print("%H",dt.strftime("%H")) 
# print("%f",dt.strftime("%f")) #368969-microsecond
# print("%z",dt.strftime("%z")) 
# print("%j",dt.strftime("%j")) #127-day of year
# print("%U",dt.strftime("%U")) #18
# print("%W",dt.strftime("%W")) #18
# print("%c",dt.strftime("%c")) #Thu May  7 22:03:25 2026
# print("%x",dt.strftime("%x")) # 05/07/26
# print("%X",dt.strftime("%X")) #22:05:01

""""""
# dt=datetime.now()
# print(dt)
# print("%Y")
# print(dt.strftime("%z"))
# br = dt + timedelta(weeks=3)
# print(br)

# dob = datetime(1980,10,2)
# dt = datetime.today()
# daysS = dt - dob
# age = daysS.days/365
 # print(daysS)
# print(age)

"""number guessing game"""
# import random
# secret_number = random.randint(1, 100)
# print("Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100")
# while True:
#     guess = int(input("Enter your guess: "))
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break

"""head or tail game"""
# import random
# print("Welcome to Head or Tail Game!")
# user_choice = input("Choose Head or Tail: ").lower()
# toss = random.choice(["head", "tail"])
# print("Coin toss result:", toss)
# if user_choice == toss:
#     print("You Win!")
# else:
#     print("You Lose!")

"""Question picker"""
# import random
# questions=['what is python','what are the features of python','Define OOPs','what is excdeption handling']
# print("Welcome to the Question Picker Game!")
# while True:
#     input("\nPress Enter to pick a question...")
#     # Pick random question
#     question = random.choice(questions)
#     print("Your Question:")
#     print(question)
#     # Ask to continue
#     choice = input("\nDo you want another question? (yes/no): ").lower()
#     if choice != "yes":
#         print("Thanks for playing!")
#         break

"""OTP generator """
# import random
# print("OTP Generator")
# otp = random.randint(1000, 9999)
# print("Your OTP is:", otp)

"""safety pin game"""
import random
print("Welcome to the Safety Pin Game!")
# Randomly hide the safety pin in one box
safe_pin = random.randint(1, 5)
print("There are 5 boxes.")
print("One box contains the safety pin.")
# User guess
guess = int(input("Choose a box number (1-5): "))
# Check result
if guess == safe_pin:
    print(" You found the safety pin! You Win!")
else:
    print(" Wrong box!")
    print("Safety pin was in box:", safe_pin)



