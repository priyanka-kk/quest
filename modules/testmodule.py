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
# import random
# print("Welcome to the Safety Pin Game!")
# # Randomly hide the safety pin in one box
# safe_pin = random.randint(1, 5)
# print("There are 5 boxes.")
# print("One box contains the safety pin.")
# # User guess
# guess = int(input("Choose a box number (1-5): "))
# # Check result
# if guess == safe_pin:
#     print(" You found the safety pin! You Win!")
# else:
#     print(" Wrong box!")
#     print("Safety pin was in box:", safe_pin)

"""display the current date and time"""
# import datetime 
# now=datetime.datetime.now()
# print(now) # 2026-05-11 21:21:46.383365

"""format the date as DD-MM-YYYY"""
# import datetime 
# today=datetime.datetime.now()
# formatted_date=today.strftime("%d-%m-%Y")
# print(formatted_date) #11-05-2026

"""find the number of days between two dates"""
# import datetime
# date1=datetime.date(2026,5,1)
# date2=datetime.date(2026,5,11)
# difference=date2-date1
# print("number of days :",difference.days)

"""Online Shopping Analytics System 
1. use map() to add 18% GST to each product price
2.use filter() to find products costing above Rs.1000/-
3.use reduce to calculate the total bill amount"""
# prices=[1200,450,800,1500,3000,650]
# print("Online Shopping Analytics System")
# GST_price=list(map(lambda x:x-(x*18)/100,prices ))
# print("GST price :",GST_price)
# cost_above_1000=list(filter(lambda x: x>1000,prices))
# print("Products costing above 1000 :",cost_above_1000)
# from functools import reduce
# total_bill_amount=reduce(lambda x,y:x+y,prices)
# print("Total bill amount :",total_bill_amount)

"""Appointment Token Generator"""
# import random 
# print("Appointment Token Generator")
# token_number=random.randint(1000,9999)
# print("random token number :",token_number)
# import datetime
# today=datetime.datetime.now()
# print("current date and time :",today)
# ids=["APT101","APT102","APT103","APT104","APT105","APT106"]
# random_ids = random.sample(ids, 5)
# print("5 random appointment ids are ",random_ids)






