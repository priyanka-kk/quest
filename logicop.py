"""26) To check a number is divisible by both 3 & 5"""
n=int(input("Enter a number:"))
if n%3==0:print("The number is divisible by 3")
if n%5==0:print("The number is divisible by 5")
if (n%3==0 and n%5==0):print("The number is divisible by both 3 and 5")

"""27) Check if a number is between 10 and 50(inclusive) """
# n=int(input("Enter a number:"))
# if n>=10 and n<=50:print("number between 10 and 50")
# else:print("number is not between 10 and 50")

"""28) login check"""
# username=input("Enter user name:")
# password=input("Enter password:")
# if username=="admin" and password=="1234":print("login success")
# else:print("incorrect username and password")

"""29) Use the not operator to reverse the boolean result of a comparison"""
# print(not(6**2==36))

"""30) To check a person is eligible to vote"""
# age=int(input("Enter the age:"))
# id=input("Enter voter id:")
# if age>=18 and id!="":print("The person is eligible to vote")
# else:print("The person is not eligible to vote")

"""31) Check if a number is either positive or even"""
# n=int(input("Enter a number:"))
# if n>0 or n%2==0:print("the number is positive or even")
# else:print("the number is negative or even")

"""33) Check the character is a vowel using or operator"""
# c=input("Enter a character:")
# if (c=='a' or c=='e' or c== 'i' or c=='o' or c=='u') or (c=='A' or c=='E' or c== 'I' or c=='O' or c=='U'):print("vowel")
# else:print("not a vowel")

"""34) check if a number is not divisible by 7"""
n=int(input("Enter a number:"))
if n%7!=0:print("the number is not divisible by 7")
else:print("the number is divisible by 7")