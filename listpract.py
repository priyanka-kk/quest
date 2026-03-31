""" 16. Write a program to remove duplicates from a list.
2
17. Find the second largest element in a list.
3
18. Write a program to rotate a list to the left by one position.
4
19. Write a program to rotate a list to the right by one position.
5
20. Move a specific element (e.g., 50) to the first position of a list.
6
21. Create a list of squares of numbers from 1–10 using list comprehension.
7
22. Create a list containing only odd numbers from 1–50 using list comprehension.
8
23. Write a program to merge two lists and remove duplicates.
9
24. Find the sum of all elements in a list without using sum()
"""

"""1. Create a list of five integers and print all elements using a for loop."""
# numbers=[1,2,3,4,5]
# for i in numbers:
#     print(i)

"""2. Write a program to find the length of a list without using len()."""
# cnt=0
# numbers=[1,2,3,4,5]
# for i in numbers:
#     cnt+=1
# print(f"the length of the list is {cnt}")

""" 3. Create a list of numbers and print the maximum and minimum values."""
# numbers=[3,7,9,5,2]
# print(f"the maximum value in the list is {max(numbers)}")
# print(f"the minimum value in the list is {min(numbers)}")

"""4. Write a program to append a new element to a list entered by the user."""
# numbers=[3,7,9,5,2]
# numbers.append(34)
# print(numbers)

"""5. Insert an element at a specific position in a list."""
# numbers=[3,7,9,5,2]
# numbers.insert(0,67)
# print(numbers)

"""6. Remove an element from a list using remove() and pop(). """
# numbers=[3,7,9,5,2]
# numbers.pop(1) #value in index 1 is removed
# numbers.remove(9) #number 9 is removed
# print(numbers)

"""7. Write a program to check whether a given element exists in a list. """
# numbers=[3,7,9,5,2]
# snum=int(input("Enter the number to search :"))
# if snum in numbers:
#     print(f"{snum} exist in the list")
# else:
#     print(f"{snum} not exist in the list")

"""8. Reverse a list without using reverse()."""
# numbers=[1,2,3,4,5,6]
# print(f"reversed list is {numbers[::-1]}")

"""9. Sort a list of numbers in ascending and descending order."""
# numbers=[7,5,8,2,4,3,45,67,98]
# numbers.sort()
# print(f"the numbers in ascending order are {numbers}")
# numbers.sort(reverse=True)
# print(f"the numbers in desscending order are {numbers}")

"""10. Create a list of numbers and print only the even numbers."""
# s=[]
# numbers=[7,5,8,2,4,3,45,67,98]
# for i in numbers:
#     if i%2==0:
#         s.append(i)
# print(f"the even numbers are {s}")

"""11. Count how many times a specific element appears in a list. """
# numbers=[7,5,8,2,4,3,45,67,98,2,2,4]
# snum=int(input("The search element"))
# print(f"{snum} appeared in {numbers.count(snum)} times")

"""12. Write a program to copy one list into another list. """
# numbers=[7,5,8,2,4,3,45,67,98,2,2]
# copy_list=numbers.copy()
# print(copy_list)

"""13. Concatenate two lists using the + operator."""
# num1=[1,2,3,4,5,6,7,8]
# num2=[9,10,11,12,13,14]
# print(f"the concatenated list is {num1+num2}")

"""14. Repeat a list three times using the * operator."""
# num1=[1,2,3,4,5,6,7,8]
# print(num1*3)

"""15. Demonstrate positive and negative indexing in a list."""
# num1=[1,2,3,4,5,6,7,8]
# print(num1[0::]) # positive indexing
# print(num1[::-1]) # negative indexing

"""Intermediate level"""
"""16. Write a program to remove duplicates from a list."""
# numbers=[7,5,8,2,4,3,45,67,98,2,2]
# print(list(set(numbers)))

"""17. Find the second largest element in a list."""
large=0
s_large=0
numbers=[7,5,8,2,4,3,45,67,98,2,2]
for i in range(len(numbers)):
    if i>large:
        s_large=large
        large=numbers[i]
    elif large>numbers[i]>s_large:
        s_large=numbers[i]
print(s_large)
    













  
    







