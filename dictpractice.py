# details={}
# print(type(details))

# details={'name':'Thejas','age':22,'place':'clt'}
# print(details)

# sample_dict={1:'a',2:'b',3:'a'}
# print(sample_dict)

# sample_dict={1:'a',2:'b',3:'a',4.5:'d',(1,2.3):'tuple'}
# print(sample_dict)

# sample_dict={1:[10,20,30,'ABC'],2:{100,200,300,'ABC'},3:{40,50,'ABC'},4.5:{'name':'Shony'},10:1}
# print(sample_dict)

# student1={'name':'shahal','age':24,'batch':'python'}
# print(student1)
# student1['place']='calicut'
# print(student1)

# student1['name']='Yaseen'
# print(student1)

# student1.update(rollno=25, domain=['python'])
# # student1['domain'].append("MERN")
# # print(student1)
# print(student1['rollno'])
# print(student1.get('name',"key doesn't exist"))
# print(student1.get('teacher',"key doesn't exist"))

# del student1
# del student1['rollno']

# student1.pop('place')
# student1.popitem()
# print(student1)

# for key,value in student1.items():
#     print(key,value)
# a=[1,2,3]
# b=[10,20,30]
# c=zip(a,b)
# print(c)

"""Print two list as key value pairs"""
# a=[1,2,3]
# b=[10,20,30]
# c=dict(zip(a,b)) 
# print(c)