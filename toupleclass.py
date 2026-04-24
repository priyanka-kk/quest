t = ("python",[10,20,30],(5,15,25),"sree")
s = ["python",[10,20,30],(5,15,25),"sree"]
# print(id(t))
# print(id(s))

# x,*y,z = t
# print (x)
# print(y)
# print(z)

# t[0]= 10

# print(t)
# print(len(t))
# print(t[0])
# print(t[-1])

# t=10,20,30 
# t+=(40,) 
# sample_list=list(t)
# sample_list.append(50)
# # t+=40
# t1=tuple(sample_list)
# print(t1)

"""list unpacking"""
# sample_list=['apple','banana','mango']
# x,y,z=sample_list
# print(x,y,z)

# sample_list=['apple','banana','mango','grapes']
# del sample_list
# x,y,*z=sample_list
# print(x,y,z)
# x,*y,z=sample_list
# print(x,y,z)
# *x,y,z=sample_list
# print(x,y,z)

# t=['apple','banana','mango','grapes']
# t=[*t,'kiwi','strawberry']
# print(t)

"""slicing"""
# person=('dheeraj','shony','thejas')
# print(person[1:])

# for p in person:
#     print(p)

# for p in range(len(person)):
#     # print(p)
#     print(f"{person[(p)]} : {len(person[(p)])}")

# i=0
# person=('dheeraj','shony','thejas')
# while i<len(person):
#     print(person[i])
#     i+=1

# print(dir(person))
# print(person.count('dheeraj'))
# # print(person.count('priya'))
# print(person.index('shony'))
# print(person.index('priya'))
