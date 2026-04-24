"""1. Create a tuple containing five different data types (int, float, string, list, boolean)"""
# t=(2,4.5,'dheeraj',[1,2,3],True)
# print(t)

"""2. Write a script to check the type of a tuple with a single element. Show the difference
between (5) and (5,)."""
# t=(5)
# print(type(t))
# t=(5,)
# print(type(t))

"""3. Access the last element of a tuple without knowing its length."""
# t=(1,2,4,'Thejas',[1,4,8,9],(10,20,30))
# print(t[-1])

"""4. Access the second to last element of a tuple using negative indexing."""
# t=(1,2,4,'Thejas',[1,4,8,9],(10,20,30))
# print(t[-2])

"""5. Given nested_tuple = ("Python", [10, 20, 30], (5, 15, 25)), print the number 20."""
# nested_tuple = ("Python", [10, 20, 30], (5, 15, 25))
# print(nested_tuple[1][1])

"""6. Check if the element 'Sreeraj' exists in a tuple using a membership operator."""
# t=('Sreeraj','Dheeraj','Thejas','Shony')
# if 'Sreeraj' in t:
#     print("exist")
# else:
#     print("not exist")

"""7. Find the memory size of a list vs. a tuple with the same elements using the sys module."""
# import sys
# list1=[1,2,3,4,5,6,7,8,9]
# tup1=(1,2,3,4,5,6,7,8,9)
# lsize=sys.getsizeof(list1)
# tsize=sys.getsizeof(tup1)
# print(f"Memory size of list={lsize} bytes")
# print(f"Memory size of tuple={tsize} bytes")

"""8. Unpack a tuple of 3 elements into three variables: x, y, and z"""
# t=('Elephant','Giraffe','Tiger')
# x,y,z=t
# print(x,y,z)

"""9. Demonstrate what happens if you try to unpack a tuple of 4 elements into 3 variables."""
# t=('Elephant','Giraffe','Tiger','lion')
# x,y,z=t
# print(x,y,z) #ValueError: too many values to unpack (expected 3, got 4)

"""10. Use the 'extended iterable unpacking' (using *) to grab the first element and the rest into a
list."""
t=('Elephant','Giraffe','Tiger')
x,*y=t
print(x,y)

"""11. Write code that attempts to change the first element of a tuple and handle the resulting
TypeError gracefully."""




"""12. Given a tuple: t = (1, 2, [3, 4]). Change the value 3 to 30. Explain why this works despite
tuples being immutable."""
# t = (1, 2, [3, 4])
# t[2][0]=30
# print(t)
#tuple is immutable.But here [3,4] is a list inside the tuple.list is mutable.hence changed 

"""13. Create two tuples, concatenate them, and assign them to a new variable."""
# t1=(1,2,3,4)
# t2=(5,6,7,8)
# con=t1+t2
# print(con)

"""15. Swap two variables a and b using tuple unpacking logic in a single line."""
# a = 5
# b = 10
# a, b = b, a
# print(a, b)

"""16. Write a program to "add" an item to a tuple by converting it to a list first."""
# t=(1,2,3,4,5)
# l=list(t)
# l.append(6)
# print(tuple(l))

"""17. Write a program to "remove" an item from a tuple."""
# t=(1,2,3,4,5)
# l=list(t)
# l.remove(3)
# print(tuple(l))

"""Delete an entire tuple variable from memory and verify its absence using a try-except
block."""
# t=(1,2,3,4,5)
# del t
# try:
#     print(t)
# except NameError:
#     print("Tuple has been deleted and is no longer in memory.")

"""19. Sort a tuple of integers and return the result as a new tuple."""
# t=(9,7,5,6,3,4)
# l=list(t)
# l.sort()
# print(tuple(l))

"""20. Reverse a tuple using the slicing method [::-1]."""
# t=(9,7,5,6,3,4)
# print(t[::-1])

"""21. Find the index of the first occurrence of the number 10 in a tuple."""
# t=(1,2,3,4,10,5,6,7,10,8,9,10)
# print(t.index(10))

"""22. Count how many times the string "Python" appears in a tuple of job roles."""
# job_roles=('python','java','html','Django','python','bootstrap','python','javascript')
# print(job_roles.count('python'))

"""23. Find the maximum and minimum values in a tuple of stock prices."""
# stock_prices=(30,50,70,100,15,700,1000)
# print(max(stock_prices))
# print(min(stock_prices))

"""24. Calculate the sum of all numeric elements in a tuple."""
# t=(34,5.6,3.6,23,45,67,89)
# print(sum(t))

"""25. Given a tuple of tuples: ((1, 2), (3, 4), (5, 6)), calculate the sum of the second element of
each internal tuple."""
# t=((1, 2), (3, 4), (5, 6))
# total=0
# for i in t:
#     total+=i[1]
# print(f"the sum of second element in the tuple is {total}")

"""26. Use the index() method to find the position of 'Apple' starting from index 3 in a large fruit
tuple."""
# fruits=('mango','banana','grapes','guava','Apple','orange','papaya')
# pos=fruits.index('Apple',3)
# print(f"positon of Apple : {pos}")

"""27. Write a function that takes a tuple and returns a new tuple containing only the even
numbers."""
# t=(1,2,3,4,5,6,7,8,9,10)
# for i in t:
#     if i%2==0:
#         print(i)
#         # or
# t=(1,2,3,4,5,6,7,8,9,10)
# even=(i for i in t if i%2==0)
# print(tuple(even))

"""28. Convert a list of tuples into a single flat list."""
# l=[(1,2),(3,4),(5,6),(7,8),(9,10)]
# s=[]
# for i in l:
#     for j in i:
#         s.append(j)
# print(s)

"""29. Create a tuple from a user-input string where each character is an element."""
# s=input("Enter a string :")
# print(tuple(s))

"""30. Check if all elements in a tuple are truthy using the all() function."""
# t=(1,2,3,4)
# if all(t):
#     print("all elements are truthy")
# else:
#     print("some elements are falsy")
#falsy values in python are 0,none,"",{},[],(),false

"""31. Extract a sub-tuple containing the elements from index 2 to 5 (inclusive)."""
# t=(1,2,3,4,5,6,7,8,9,10)
# sub_tup=t[2:6]
# print(sub_tup)

"""32. Use slicing to get every second element of a tuple."""
# t=(1,2,3,4,5,6,7,8,9,10)
# sub_tup=t[1::2]
# print(sub_tup)

"""33. Write a 'for' loop to print each element of a tuple with its corresponding index number."""
# t=(1,2,3,4,5,6,7,8,9,10)
# for index,value in enumerate(t):
#     print(f"{index} : {value}")

"""34. Use a 'while' loop to iterate through a tuple backwards."""
# t=(1,2,3,4,5,6,7,8,9,10)
# i=len(t)-1
# while(i>=0):
#     print(t[i])
#     i-=1

"""35. Create a tuple of 10 numbers and slice it to get the last 3 elements."""
# t=(1,2,3,4,5,6,7,8,9,10)
# s=t[-3:]
# print(s)

"""36. Slice a tuple to remove the first and last elements."""
# t=(1,2,3,4,5,6,7,8,9,10)
# s=t[1:-1]
# print(s)

"""37. Use a for loop to concatenate all strings in a tuple into a single sentence."""
# t=('welcome', 'to', 'my', 'home')
# for i in t:
#     print(i,end=" ")

"""38. Compare two tuples (1, 2, 3) and (1, 2, 4). Explain the logic of how Python compares
them."""
# t1=(1,2,3)
# t2=(1,2,4)

"""39. Write a program to find duplicate elements in a tuple."""
# t=(1,2,3,4,5,6,7,8,9,10,4,5,6)
# s=[]
# for i in t:
#     if t.count(i)>1 and i not in s :
#         s.append(i)
#         print(i)

"""40. Zip two tuples together to create a list of coordinate pairs."""
# t1=(1,2,3,4,5,6)
# t2=(11,12,13,14,15,16)
# co=list(zip(t1,t2))
# print(co)

"""41. Create a tuple of numbers and find the second largest number."""
# largest=0
# slargest=0
# t=(23,56,34,67,78,39,42)
# for i in range(len(t)):
#     if t[i]>largest:
#         s_large=largest
#         largest=t[i]
#     elif largest>t[i]>s_large:
#         s_large=t[i]
# print(s_large)

"""42. Write a program to remove duplicate elements from a tuple."""
# t=(1,2,3,4,5,6,7,8,9,10,4,5,6)
# res=tuple(set(t))
# print(res)

"""43. Write a program to find the frequency of each element in a tuple. """
# t=(1,2,3,4,5,6,7,8,9,10,4,5,6)
# for i in set(t):
#     print(f"{i} : {t.count(i)}")

"""45. 35. Write a program to sort a tuple of numbers."""
# t=(23,56,34,67,78,39,42)
# print(tuple(sorted(t)))

"""46. Write a program to sort a tuple of tuples based on the second element.
Example:
((1,5),(3,2),(4,8))"""



"""47. Write a program to find common elements between two tuples."""
# t1=(1,2,3,4,5,6)
# t2=(5,6,7,8,9,10)
# s=[]
# for i in t1:
#     if i in t2 and i not in s:
#         s.append(i)
# print(tuple(s))

"""48. Write a program to convert a tuple into a string."""
# t=('welcome', 'to', 'my', 'home')
# for i in t:
#     print(i,end=" ")

"""49. 39. Write a program to count vowels present in a tuple of characters."""
# t=('t','u','v','a','q','w','e','i','o')
# cnt=0
# for i in t:
#     if i in 'aeiouAEIOU':
#         cnt+=1
# print(cnt)

"""50. Write a program to find the product of all numbers in a tuple. """
# p=1
# t=(1,2,3,4,5)
# for i in t:
#     p=p*i
# print(f"product is {p}")
    

    

        



    
    
















