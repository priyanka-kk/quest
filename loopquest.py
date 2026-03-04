""" Python Lab Practical Questions: For Loop and Range Function Level:
Beginner to Intermediate


14. Write a program to print characters of a string using a for loop.

15. Write a program to count the number of characters in a string.

16. Write a program to count vowels in a string.

17. Write a program to print numbers from N to 1.

18. Write a program to find the sum of even numbers from 1 to 100.

19. Write a program to find the sum of odd numbers from 1 to 100.

20. Write a program to print the first 10 natural numbers.

21. Write a program to print numbers from 1 to 100 with a step of 5.

22. Write a program to print the following pattern:

-    **

23. Write a program to print the following pattern: 1 12 123 1234 12345

24. Write a program to check whether a number is prime or not.

25. Write a program to print Fibonacci series up to N terms.
"""

""" 1.  Write a program to print numbers from 1 to 10 using a for loop."""

# for num in range (1,11,1):
#     print(num)

""" 2.  Write a program to print numbers from 1 to 20 using range()."""

# for num in range (1,21,1):
#     print(num)

""" 3.  Write a program to print even numbers from 1 to 50."""

# for num in range (2,51,2):
#     print(num)

""" 4.  Write a program to print odd numbers from 1 to 50."""

# for num in range (1,51,2):
#     print(num)

""" 5.  Write a program to print numbers from 10 to 1 in reverse order."""

# for num in range (10,0,-1):
#     print(num)

""" 6.  Write a program to print the multiplication table of a given number."""

# num1=int(input("Please enter a number for multiplcation table:"))

# for i in range (1,11,1):
#     print(f"{i} x {num1} = {i*num1}")

""" 7. Write a program to find the sum of numbers from 1 to N."""

# num1=int(input("Please enter a number to sum from 1:"))

# s=0
# for i in range (1,num1+1,1):
#     s+=i
# print(s)

""" 8.  Write a program to find the factorial of a number."""

# num1=int(input("Please enter the factorial:"))

# s=1
# for i in range (num1,1,-1):
#     s=s*i
# print(s)

""" 9.  Write a program to print the square of numbers from 1 to 10. """

# for num in range (1,11,2):
#     print(num*num)

""" 10. Write a program to print the cube of numbers from 1 to 10."""

# for num in range (1,11,2):
#     print(num**3)

""" 11. Write a program to count numbers from 1 to 100."""

# for num in range (1,101,1):
#     print(num)

""" 12. Write a program to print all multiples of 3 between 1 and 50."""

# for num in range (3,50,3):
#     print(num)

""" 13. Write a program to print numbers divisible by both 2 and 5 between 1  and 100."""

# for num in range (10,101,10):
#     print(num)