# while condition:
#     body
#     increment/decrement

"""print the name 10 times"""
# i=0
# while i< 10:
#     print("priyanka")
#     i+=1
"""print numbers from 1 to 20"""
# x=1
# while x<21:
#     print(x)
#     x+=1
"""even numbers from 1 to 20"""
# x=0
# while x < 20:
#     x+=2
#     print(x)

"""sum of numbers from 1 t0 10"""
# x=1
# s=0
# while x < 11:
#     s=s+x
#     x+=1
# print(s)

"""print numbers from 20 to 1"""   
# x=20
# while x>=1:
#     print(x)
#     x-=1

"""print the count of mutiple of 3 """
# count=0
# x=int(input("Enter a limit:"))
# while x>0:
#     if x%3==0:
#         count+=1
#     x-=1
# print(count)

"""print multiplication table of 2"""
# x=1
# while x<=20:
#     print(f"{x}*2={x*2}")
#     x+=1

"""print multiplication table of a user input number"""
# n=int(input("Enter a number:"))
# x=1
# while x<=10:
#     print(f"{x}*{n}={x*n}")
#     x+=1

"""find the reverse of an entered number"""
x=int(input("Enter a number:"))
num=0
while x>0:
    y=x%10
    num=num*10 + y
    x=x//10
print(num)






