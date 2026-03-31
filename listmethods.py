
"""append"""
# sample_list=[4,7,9,6,1,2,3,4,7,20,10,100]
# sample_list.append(3000)
# sample_list.append('quest')
# sample_list.append(10.5)
# sample_list.append([100,200,300])
# print(sample_list)

"""insert"""
sample_list=[4,7,9,6,1,2,3,4,7,20,10,100]
# sample_list.insert('python') #eTypeError: insert expected 2 arguments, got 1
# sample_list.insert(1,'python')
# print(sample_list) #syntax listname.insert(index,value)

"""pop"""
# sample_list.pop()
# print(sample_list) #remove the last index value
# sample_list.pop(1) #here 1 is the index value
# print(sample_list)

"""remove"""
# sample_list.remove() #list.remove() takes exactly one argument (0 given)
# sample_list.remove(20) # here 20 is the value in a list
# sample_list.remove(7)  # here first occurence of 7 is removed
# print(sample_list)

"""clear"""
# sample_list.clear() # it gives the empty list clear all the values in a list
# print(sample_list)

"""count"""
# s=sample_list.count(7)
# print(s)

"""copy"""
copy_list=sample_list.copy
# print(copy_list)
# copy_list[3]=600

# print(copy_list)
# print(sample_list)
# numbers
#     print(numbers)

# square=[i**2 for i in range(1,11)]
# print(square)

# sq_cube=[]
# for i in range(1,11):
#     if i%2==0:
#         sq_cube.append(i**2)
#     else:
#         sq_cube.append(i**3)
# print(sq_cube)

new_list = [x**2 if x%2==0 else x**3 for x in range(1,11)]
print(new_list)

# s=['priyanka','dheeraj','thejas']

# up_list=[i.upper() for i in s]
# print(up_list)

# s=['priyanka','dheeraj','thejas']
# lengtht=[len(i) for i in s]
# print(lengtht)

"""start at vowels convert to uppercase  consonants to title case """
# s=['priyanka','dheeraj','thejas', "orange","ana"]

# my_list=[x.upper() if x[0] in "AEIOUaeiou" else x.title() for x in s]
# print(my_list)

"""in a list of +ve and _ve extract only +ve numbers """
# l=[2,4,8,-9,-7,-6]

# my_list = [x for x in l if x>0]

# print(my_list)

"""extract vowels in a string"""
# s="dheeraj"
# re=[i for i in s if i in 'AEIOUaeiou' ]
# print(re)

"""find the common elements"""

# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8,9]

# my_list = [x for x in list1 for y in list2 if x==y]

# print(my_list)

s=['1','2','3','4', "ss", "rd"]
my_list= [int(x) for x in s if x.isdigit()]

print(my_list)




     




