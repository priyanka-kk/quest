# vegetables=['tomato','carrot','beetroot']
# print(vegetables)
# print(vegetables[0])
# print(vegetables[1])


# sample_list=[1,2,3,'Quest',10.25,[7,8,9,10],True,None]
# print(type(sample_list))
# print(sample_list)
# print(sample_list[5][1]) #gives the element 8 in list
# print(len(sample_list))

# sample_list2=list(1,2,3)
# print(type(sample_list2))

# sample_list2=list[(1,2,3)]
# print(type(sample_list2))
# print(sample_list2)
# # print(len(sample_list2))
# print(sample_list2([5]))

# path = "C:/Users/Documents/report.pdf"
# extension = path.rsplit(".", 1)[1]
# print(extension)

# path = "C:/Users/Documents/report.pdf"
# extension = path.split('/')
# # res=extension[3].split('.')[1]
# res=extension[3].removeprefix('report.')
# print(res)

"""operators"""
numbers=[1,2,3,4,5,6,7,8,9]
# sample_list=[10,20,30,40,50]
# updated_list=numbers+sample_list #concatenation
# print(updated_list)
# numbers+=10
# print(numbers)

# numbers *=2
# print(numbers)

# numbers=[1,2,3,4,5,6,7,8,9,[10,20,30]]
# print(30 in numbers[9])
# print(len(numbers[-1]))
# print(numbers[7])
# print(numbers[8])
# # print(numbers[10])
# print(numbers[-5])
# print(numbers[-1][-1])

# numbers=[1,2,3,4,5,6,7,8,9,[10,20,30],[100,200,300,[400,500,600],700,800,900]]
# print(numbers[-1][3][1])
# print(numbers[-1][5])

# numbers[3]=400
# # numbers[3]+=400
# numbers[3]*=400
# print(numbers)

"""list slicing"""
# numbers=[1,2,3,4,5,'quest','thejas','richu',6,7,8,9,[10,20,30]]
# print(numbers[6][1:4])

"""3 by 3 matrix printing"""
# matrix = [[0,1,2],[3,4,5],[6,7,8]]
# for i in matrix:
#     for j in i:
#         # print(i)
#       print(j, end=" ")
#     print()

# matrices = [[0,1,2],[3,4,5],[6,7,8]]
# for matrix in matrices:
#     for m in matrix:
#         print(m,end=" ")
#     print()

# a=[1,2,3]
# b=a*2
# print(b)

# t=(10,20,30,40)
# print(t[-2])

# t=(1,2,3)
# t[0]=10
# print(t) #TypeError: 'tuple' object does not support item assignment

# l=[i for i in range(1,21)]
# print(l)
# even_numbers=[i for i in l if i%2==0]
# print(f"Even numbers : {even_numbers}")
# sq_odd=[i**2 for i in l if i%2!=0]
# print(f"Squares of odd numbers : {sq_odd}")

"""program to remove duplicates from a list and maintain original order"""
# Input=[1,2,2,3,4,3,5]
# s=[]
# for i in Input:
#     if i not in s:
#         s.append(i)
# print(s)
   
"""print the list in the matrix format and find the sum of
all elements in the matrix"""
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for i in matrix:
#     for j in i:
#         print(j, end=" ")
#     print()
# total=0
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         total+=matrix[i][j]
# print(f"Sum: {total}")

"""write a python program to 
1.Accept a list of numbers from the user
2.maximum value
3.minimum value
4.sum of elements(without using sum())"""
# total=0
# n=int(input("How many numbers?"))
# nums=[]
# for i in range(n):
#     num=int(input("Enter a number :"))
#     nums.append(num)
# print(f"Enter list:{nums}")
# print(f"Max:{max(nums)}")
# print(f"Min:{min(nums)}")
# for i in nums:
#     total+=i
# print(f"Sum:{total}")

"""Create a list of numbers from 1 to 20 and 
1. Generate a new list containing only even numbers using list comprehension
Also create another list of squares of odd numbers"""
# numbers =list(range(1,21))
# print(numbers)
# ev_num=[i for i in numbers if i%2==0]  
# print(f"Even numbers :{ev_num}")
# od_squres=[i**2 for i in numbers if i%2!=0]
# print(f"Squares of odd numbers:{od_squres}")

"""Write a program to
1.create a tuple 
reverse it using slicing
count occurences of a given element"""
# Tuple=(1,2,3,2,4,2)
# print(f"Tuple:{Tuple}")
# rev=Tuple[::-1]
# print(f"Reversed:{rev}")
# cnt=Tuple.count(2)
# print(f"Count of 2:{cnt}")
      
"""Given data=[(1,5),(3,2),(4,8)]
write a program to 
1.sort the list based on the second element of tuple
2.convert result into a tuple"""
# data=[(1,5),(3,2),(4,8)]
# for i in range(len(data)):
#     for j in range(1,len(data)):
#         if data[j][1]<data[j-1][1]:
#             c=data[j]
#             data[j]=data[j-1]
#             data[j-1]=c
# print(data)
# d=tuple(data)
# print(d)

"""examq"""
# a=[1,2,3]
# b=a
# b.append(4)
# print(a)

# s={1,2,2,3,4,4}
# print(len(s))

# x=(1,2,[3,4])
# x[2].append(5)
# print(x)

