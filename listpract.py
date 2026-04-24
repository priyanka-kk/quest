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
# large=0
# s_large=0
# numbers=[7,5,8,4,28,45,67,98,76]
# for i in range(len(numbers)):
#     if numbers[i]>large:
#         s_large=large
#         large=numbers[i]
#     elif large>numbers[i]>s_large:
#         s_large=numbers[i]
# print("second largest number is",s_large)

"""18. Write a program to rotate a list to the left by one position."""
# numbers=[7,5,8,4,28,45,67,98,76]
# s=numbers.pop(0)
# numbers.append(s)
# print(numbers)

"""19. Write a program to rotate a list to the right by one position."""
# numbers=[7,5,8,4,28,45,67,98,76]
# s=numbers.pop()
# numbers.insert(0,s)
# print(numbers)

"""20. Move a specific element (e.g., 50) to the first position of a list."""
# numbers=[7,5,8,4,28,50,67,98,76]
# s=numbers.pop(5)
# numbers.insert(0,s)
# print(numbers)
    
"""21. Create a list of squares of numbers from 1–10 using list comprehension."""
# squares=[i**2 for i in range(1,11)]
# print(squares)

"""22. Create a list containing only odd numbers from 1–50 using list comprehension."""
# odd_numbers=[i for i in range(1,51) if i%2!=0]
# print(odd_numbers)

"""23. Write a program to merge two lists and remove duplicates."""
# list1=[1,2,3,4,5,6,2,4]
# list2=[6,7,8,9,10,8,9,10]
# s=list1+list2
# res=list(set(s))
# print(res)

"""24. Find the sum of all elements in a list without using sum()"""
# nums=[1,2,3,4,5,6,7,8,9,10]
# tot=0
# for i in nums:
#     tot+=i
# print(tot)

"""25. Write a program to find common elements between two lists."""
# re_list=[]
# list1=[1,2,3,4,10,9,6,2,4,7]
# list2=[6,7,8,9,10,8,9,10]
# for i in list1:
#     if i in list2:
#         re_list.append(i)
# print(re_list)

"""26. Write a program to split a list into two halves."""
# list1=[1,2,3,4,5,6,7,8,9,10]
# l=int(len(list1)/2)
# a=list1[0:l]
# b=list1[l:]
# print("a=",a,"\n","b=",b)

"""27. Find the index of a given element without using index(). """
# list1=[1,2,3,4,5,6,7,8,9,10]
# print(list1)
# num = int(input("Please select the number you want to know the index:"))
# for i in range(len(list1)):
#     if list1[i]==num:
#         break
# print(i)

""" 28. Write a program to flatten a nested list."""
# nums=[1,[2,3],4,5,[6,7],9,8,10]
# s=[]
# for i in nums:
#     if type(i)==list:
#         for x in i:
#             s.append(x)
#     else:
#         s.append(i)
# print(s)

"""29. Create a program to find the frequency of each element in a list."""
# nums=[1,2,3,4,5,6,7,8,9,10,5,6,7,8]
# for i in set(nums):
#     print(f"{i} : {nums.count(i)}")

"""30. Reverse each element of a list of strings"""
# lstr=['cat','rat','dog','goat','lion']
# rev_str=[]
# for i in lstr:
#     rev_str.append(i[::-1])
# print(rev_str)

"""31. Implement a matrix using nested lists and print it in matrix format."""
# matrix=[[0,1,2],[3,4,5],[6,7,8]]
# for i in matrix:
#     for j in i:
#         print(j,end=" ")
#     print()

"""32. Write a program to add two matrices using nested lists."""
# matrrix1=[[0,1,2],[3,4,5],[6,7,8]]
# matrix2=[[4,5,6],[8,9,10],[1,2,3]]
# s = []
# for i in range(len(matrrix1)):
#     b = []
#     for j in range(len(matrix2)):
#         a = matrrix1[i][j] + matrix2[i][j]
#         b.append(a)
#     s.append(b)
# for x in s:
#     print(x)

"""33. Write a program to transpose a matrix."""
# matrrix1=[[0,1,2],[3,4,5],[6,7,8]]
# s=[]
# for i in range(len(matrrix1)):
#     b=[]
#     for j in range (3):
#         b.append(matrrix1[j][i])
#     s.append(b)
# for x in s:
#     print(x)

"""34. Flatten a 2D list into a single list using list comprehension."""
# list1=[[0,1,2],[3,4,5],[6,7,8]]
# list2=[x for i in list1 for x in i]
# print(list2)

""" 35. Find the largest sublist length in a nested list.
6
36. Write a program to find the intersection of multiple lists.
7
37. Write a program to group list elements by their length (strings).
8
38. Implement a simple stack using a Python list.
9
39. Implement a queue using a Python list.
10 40. Write a program to shuffle elements in a list.
11 41. Write a program to find the kth largest element in a list.
12 42. Write a program to check whether a list is a palindrome.
13 43. Write a program to generate all possible pairs from a list.
14 44. Create a list of prime numbers within a given range using list comprehension.
15 45. Write a program to remove all negative numbers from a list."""

""" 35. Find the largest sublist length in a nested list."""
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9,10], [11,12]]
# max_len = 0
# for i in nested:
#     if len(i) > max_len:
#         max_len = len(i)
# print(max_len)






        

    
    
    
















  
    







