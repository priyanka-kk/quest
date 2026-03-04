"""1.  Write a program to print numbers from 1 to 10 using a for loop."""
# for i in range(1,11):
#     print(i)

"""2.  Write a program to print numbers from 1 to 20 using range()."""
# for i in range(1,21):
#     print(i)

"""3.  Write a program to print even numbers from 1 to 50."""
# for i in range(2,51,2):
#     print(i)

"""4.  Write a program to print odd numbers from 1 to 50."""
# for i in range(1,51,2):
#     print(i)

"""5.  Write a program to print numbers from 10 to 1 in reverse order."""
# for i in range(10,0,-1):
#     print(i)

"""6.  Write a program to print the multiplication table of a given number."""
# num=int(input("Enter a number:"))
# for i in range (1,11,1):
#     print(f"{i} x {num} = {i*num}")

"""7.  Write a program to find the sum of numbers from 1 to N."""
# n=int(input("Enter a number:"))
# s=0
# for i in range (1,n+1,1):
#     s=s+i 
# print(s)

"""8.  Write a program to find the factorial of a number."""
# f=1
# n=int(input("Enter a number:"))
# for i in range (n,1,-1):
#     f=f*i
# print(f)

"""9.  Write a program to print the square of numbers from 1 to 10."""
# for i in range (1,11,1):
#     print(f"{i**2}")

"""10. Write a program to print the cube of numbers from 1 to 10."""
# for i in range (1,11,1):
#     print(f"{i**3}")

"""11. Write a program to count numbers from 1 to 100."""
# for i in range (1,101,1):
#     print(f"{i}")

"""12. Write a program to print all multiples of 3 between 1 and 50."""
# for i in range (3,51,3):
#     print(f"{i}")

"""13. Write a program to print numbers divisible by both 2 and 5 between 1 and 100."""
# for i in range (10,101,10):
#     print(f"{i}")
    
"""14) characters of a string"""
# str=input("Enter a string:")
# for i in str:
#     print(i)

"""15) count the number of characters in a string"""
# str=input("Enter a string:")
# num = 0
# for i in str:
#     num+=1
# print(num)

"""16) count vowels in a string"""
# str=input("Enter a string:")
# vcount=0
# for ch in str:
#     if (ch in 'aeiou' or ch in 'AEIOU'):
#         vcount=vcount+1
# print(vcount)  

"""17) Print number from n to 1"""    
# n=int(input("Enter a number"))
# for i in range(n,0,-1):
#     print(i)

"""18) sum of even numbers from 1 t0 100"""
# s=0 
# for i in range(0,101,2):
#     s=s+i
# print(f"sum of even numbers from 1 t0 100 are {s}")

"""19) sum of odd numbers from 1 t0 100"""
# s=0 
# for i in range(1,101,2):
#     s=s+i
# print(f"sum of odd numbers from 1 t0 100 are {s}")

"""20) Print first 10 natural numbers"""
# for i in range(1,11,1):
#     print(i)

"""21)  print numbers from 1 to 100 with a step of 5 """
# for i in range(1,101,5):
#     print(i)

"""22) print the following pattern - ** """
# for i in range(1,2,1):
#     print("**")

"""23)print the following pattern  1 12 123 1234 12345"""
# pat=0
# for i in range(1,6,1):
#     pat = 10*pat + i
#     print(pat, end=" ")

"""24) check the given number is prime or not"""
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is Not a prime number")
            break
    else:
        print(f"{num} is a Prime number")


 

 






 
