"""check the number is a prime number or not """
# num=int(input("Enter a number:"))
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

"""list the prime numbers up to a limit"""
# l=int(input("Enter the limit"))
# for i in range(2,l):
#     if l%i==0:
#         i+=1
#         print("not prime")
#         break
# else:
#     print("prime")    
# 
x=int(input("Enter the limit:"))   

for num in range(2,x+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)

# for num in range(2,x+1):
#     prime=True
#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#             break
#     if prime:
#         print(num)

""" Reverse a string"""

# name = input("Please Enater a name:")
# rever = ""

# for i in name:
#     rever = i + rever

# print (rever)

"""Check the entered number is a perfect square"""
sq=int(input("Enter a number:"))
sqrt=int(sq**0.5)
if sqrt*sqrt==sq:
    print("It is a perfect square")
else:
    print("It is not a perfect square")
