# sample_set=set()
# sample_set={}
# sample_set={1,2,3,10.25,0.25,'Quest','python','Quest'}
# print(type(sample_set))
# print(type(sample_set))
# strings=set('Quest')
# print(strings)
# sample_set={1,2,3,10.5,0.25,'Quest','python','Quest',(10,20,30)}
# for index,value in enumerate(sample_set):
#     print(index,value)
    
# print(enumerate('Quest'))
# print(list(enumerate('Quest')))

"""add()"""
# person={'yaseen','Jasil','Priyanka','Shony'}
# person.add('Shabin')
# person.add('Shahal')
# person.add(tuple('shahal'))
# print(person)

"""update"""
# person.update('shahal')
# print(person)
# person.update(100,200,'shahal')
# person.update([100,200,300])
# print(person)

# s = {1, 2}
# s.update([3, 4], (5, 6), {7, 8})
# print(s)

"""exam"""
"""write a python program to 
take two sets 1)Employees who know python
2)Employees who know Django
find 1)Employees who know both
2)Employees who know only python
3)Employees who know either python or Django  """
# python_team={"Arun","Neha","Rahul","Meera"}
# django_team={"Rahul","Meera","Vishnu","Anu"}
# res=python_team.intersection(django_team)
# print("Employees with both skills :",res)
# res1=python_team.difference(django_team)
# print("Employees with only python :",res1)
# res2=res1=python_team.union(django_team)
# print("Employees with either skill :",res2)

""" Given a 3 by 3 matrix(list of lists),write a program to  
print the elements of the second row and the element at matrix[2][1]"""
# Input=[[1,2,3],[4,5,6],[7,8,9]]
# d = Input[1]
# print(f"Row 2:{d}, Element: {Input[2][1]}")

"""write a program to count the frequency of each character in astring "FullStack" 
using a dictionary"""
# s1 = "FullStack"
# freq = {}
# for ch in s1:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)

"""write a python program to:
Accept a list of numbers
Remove duplicates without changing the original order"""
nums = [10, 20, 10, 30, 40, 20, 50, 30]
unique = []
duplicates = []
seen = set()
for i in nums:
    # Remove duplicates (preserve order)
    if i not in unique:
        unique.append(i)

    # Find duplicates
    if i in seen and i not in duplicates:
        duplicates.append(i)
    else:
        seen.add(i)
print("Original list:",nums)        
print("Cleaned list:", unique)
print("Duplicate values:", duplicates)

"""write a program to rotate a list to the left by one position"""
l=[10,20,30,40]
s=l.pop(0)
c=l.append(s)
print(l)



