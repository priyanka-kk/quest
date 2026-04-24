"""1. Create a set containing 5 numbers and print the set."""
# s={1,2,3,4,5}
# print(s)

"""2. Create a set with mixed data types and print each element."""
# s={1,2.5,'Priyanka',(4,5,6)}
# for i in s:
#     print(i)

"""3. Write a program to create a set from a list."""
# l=[1,2.5,'Priyanka',(4,5,6)]
# s=set(l)
# print(s)

"""4. Write a program to remove duplicate elements from a list using a set."""
# l=[1,2,3,4,5,6,1,2,3]
# s=list(set(l))
# print(s)

"""5. Create an empty set and add three elements to it."""
# s=set()
# s.update({1,2,3})
# print(s)

"""6. Write a program to check if an element exists in a set."""
# s={1,2,3,4,5,6}
# e=int(input("Enter the number to search :"))
# if e in s:
#     print("present")
# else:
#     print("not present")

"""8. Write a program to find the length of a set without using len()."""
# l=0
# s={1,2,3,4,5,6,7,8,9}
# for i in s:
#     l+=1
# print(f"length={l}")

"""9. Write a program to convert a tuple into a set."""
# t=(1,2,3,4,5,6,7,8,9)
# s=set(t)
# print(s)

"""10. Write a program to convert a set into a list."""
# s={1,2,3,4,5,6,7,8,9}
# l=list(s)
# print(l)

"""11. Create a set and add a new element using add()."""
# s={1,2,3,4,5,6,7,8,9}
# s.add(10)
# print(s)

"""12. Write a program to add multiple elements to a set using update()."""
# s={1,2,3,4,5,6,7,8,9}
# s.update({11,12,13})
# print(s)

"""13. Write a program to remove an element using remove()."""
# s={1,2,3,4,5,6,7,8,9}
# s.remove(7)
# print(s)

"""14. Write a program to remove an element using discard()."""
# s={1,2,3,4,5,6,7,8,9}
# s.discard(5)
# print(s)

"""15. Write a program to remove a random element using pop()."""
# s={1,2,3,4,5,6,7,8,9}
# s.pop()
# print(s)

"""16. Write a program to clear all elements from a set."""
# s={1,2,3,4,5,6,7,8,9}
# s.clear()
# print(s)

"""17. Write a program to copy a set into another set."""
# s={1,2,3,4,5,6,7,8,9}
# c=s.copy()
# print(c)

"""18. Write a program to add elements from a list into a set."""
# l=[1,2,3,4,5,6,7,8,9]
# s=set(l)
# print(s)

"""19. Write a program to add elements from a tuple into a set."""
# t=(1,2,3,4,5,6,7,8,9)
# s=set(t)
# print(s)

"""20. Write a program to update a set with another set."""
# s={1,2,3,4,5,6,7,8,9}
# s.update({10,11,12,13})
# print(s)

"""21. Write a program to find the union of two sets."""
# s1={1,2,3,4,5}
# s2={6,7,8,9,10}
# print(s1.union(s2)) # or s1|s2

"""22. Write a program to find the intersection of two sets."""
# s1={1,2,3,4,5,6,7}
# s2={6,7,8,9,10}
# print(s1.intersection(s2)) # s1&s2

"""23. Write a program to find the difference between two sets."""
# s1={1,2,3,4,5,6,7}
# s2={6,7,8,9,10}
# print(s1.difference(s2)) # s1-s2

"""24. Write a program to find the symmetric difference between two sets."""
# s1={1,2,3,4,5,6,7}
# s2={6,7,8,9,10}
# print(s1.symmetric_difference(s2)) #s1^s2

"""25. Write a program to update a set using intersection_update()."""
# s1={1,2,3,4,5,6,7}
# s2={6,7,8,9,10}
# s1.intersection_update(s2)
# print(s1)

"""26. Write a program to update a set using difference_update()."""
# s1={1,2,3,4,5,6,7}
# s2={6,7,8,9,10}
# s1.difference_update(s2)
# print(s1)

"""27. Write a program to update a set using symmetric_difference_update()."""
# s1={1,2,3,4,5,6,7}
# s2={6,7,8,9,10}
# s1.symmetric_difference_update(s2)
# print(s1)

"""28. Write a program to check if one set is a subset of another set."""
# s1={1,2,3,4,5,6,7}
# s2={6,7}
# print(s2.issubset(s1))

"""29. Write a program to check if one set is a superset of another set."""
# s1={1,2,3,4,5,6,7}
# s2={6,7}
# print(s1.issuperset(s2))

"""30. Write a program to check if two sets are disjoint."""
# s1={1,2,3,4,5,6,7}
# s2={8,9,10}
# print(s1.isdisjoint(s2))

"""31. Write a program to find common elements between two lists using sets."""
# l1=[1,2,3,4,5,6,7]
# s1=set(l1)
# l2=[6,7,8,9,10]
# s2=set(l2)
# print(s1.intersection(s2))

"""32. Write a program to find unique elements from two lists."""
# l1=[1,2,3,4,5,6,7]
# l2=[6,7,8,9,10]
# print((set(l1)).union(set(l2)))

"""33. Write a program to find elements present in the first list but not in the second list."""
# l1=[1,2,3,4,5,6,7]
# l2=[6,7,8,9,10]
# print((set(l1)).difference(set(l2)))

"""34. Write a program to remove duplicates from a sentence using sets."""
# s="baby is cute baby is healthy"
# res=s.split()
# print(set(res))

"""35. Write a program to find unique characters in a string using sets."""
# s="welcome"
# print(set(s))

"""36. Write a program to count unique words in a sentence."""
# s="baby is cute baby is healthy"
# res=s.split()
# cnt=0
# for i in set(res):
#     cnt+=1
# print(cnt) # print(len(s.split())))

"""37. Write a program to find the difference between two strings using sets."""
# str1="this is cat"
# str2="this is rat"
# print(set(str1)^set(str2))

"""38. Write a program to find vowels present in a string using sets."""
# str1="welcome"
# set1= set()
# for i in str1:
#     if i in 'AEIOUaeiou':
#         set1.add(i)
# print(set1)

"""39. Write a program to check whether two strings contain the same characters."""
str1="welcome"
str2="melcowe"
if set(str1) == set(str2):
    print("True")
else:
    print("False")

"""40. Write a program to find common characters between two strings."""
str1="welcome"
str2="awesome"
print(set(str1)&set(str2))

""" 
48. Given two sets representing available skills and required job skills, find missing skills.
49. Create a set representing product categories in an e-commerce system and remove a
category dynamically.
50. Given two datasets of email IDs, remove duplicates and print all unique email IDs.
Bonus Interview Questions
1. Why are sets unordered in Python?
2. What is the difference between remove() and discard()?
3. Why can't sets contain mutable elements like lists?
4. What is the difference between difference() and difference_update()?
5. When should sets be used instead of lists in real-world applications?"""

"""41. Write a program to create a set of squares from numbers 1–10 using set
comprehension."""
# squares={i**2 for i in range(1,11)}
# print(squares)

"""progeram to find common elements in two lists """
# s=[]
# lst1=[1,2,3,4,5,6,7,8]
# lst2=[6,7,8,9,10,11,12]
# for i in lst1:
#     if i in lst2 and i not in s:
#         s.append(i)
# print(s)

"""42. Write a program to create a set of cubes using set comprehension."""
# cubes={i**3 for i in range(1,11)}
# print(cubes)

"""43. Write a program to create a set of even numbers from 1–20 using set comprehension."""
# even_numbers={i for i in range(1,21) if i%2==0}
# print(even_numbers)

"""44. Write a program to create a set of odd numbers using set comprehension."""
# odd_numbers={i for i in range(1,21) if i%2!=0}
# print(odd_numbers)

"""45. Write a program to create a set containing lengths of words in a sentence."""
# str1="welcome to Bangalore"
# s=str1.split()
# set_len=set()
# for i in s:
#     set_len.add(len(i))
# print(set_len)

"""46. Given two sets representing students enrolled in Python and Java, find students
enrolled in both courses."""
# java_studs={'Deepa','Vidya','Smitha','Remya','Hima','Sharanya'}
# python_studs={'Vidya','Sharanya','sithara','Sunitha'}
# both=java_studs & python_studs
# print(both)

"""47. Given two sets representing users who logged in today and yesterday, find new users
today."""
# log_today={'Deepa','Vidya','Smitha','Remya','Hima','Sharanya'}
# log_yest={'Vidya','Sharanya','Sithara','Sunitha'}
# print(log_today-log_yest)

""""""


