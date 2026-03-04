"""salary calculation"""
# salary=float(input("Enter the basic salary:"))
# years=int(input("Enter the years of service:"))
# if years > 5:
#     bonus = (salary*10)/100
# else:
#     bonus = (salary*5)/100
# salary = salary + bonus
# print(f"Bonus Awarded:{bonus}")
# print(f"Total salary:{salary}")

"""Check the number is palindrome number or not"""
num=int(input("Enter a 3 digit number:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if temp==rev:
    print("it is palindrome number")
else:
    print("Not a palindrome number")

"""Multiplication table of a number upto a limit"""
# num=int(input("Enter a table number:"))
# limit=int(input("Enter a limit:"))
# i=1
# while i<=limit:
#    p=num*i
#    print(f"{num}*{i}={p}")
#    i+=1
