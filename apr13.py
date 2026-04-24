# classqis = {"std1":{"name":"ff","age":22},"std2":{"name":"kf","age":27}}
# print(classqis["std1"]["age"])

"""nested dictionary"""
# nested_dict={
#     'student1':{'name':'abc','age':24,'batch':'stack'},
#     'student2':{'name':'efg','age':29,'batch':'python','phone':[8547,1234]}
#     }
# print(nested_dict) 
# print(nested_dict['student1']['batch']) #stack
# print(nested_dict['student2']['phone'][1]) #1234    
# nested_dict['student1']['phone']=[8481,6421]
# print(nested_dict)
# print(nested_dict['student1']['phone'][0])

"""list comprehension"""
"""squares"""
# square_dict ={x:x**2 for x in range(1,11)}
# print(square_dict)

"""even numbers"""
# ev_squares={x:x**2 for x in range(1,21) if x%2==0}
# print(ev_squares)

"""alphabets and numbers"""
# alpnum={'a':1,'b':2,'c':3,'d':4}
# res={k:v for k,v in alpnum.items() if v%2==0}
# print(res)#{'b':2,'d':4}

"""swapping"""
# alpnum={'a':1,'b':2,'c':3,'d':4}
# res={v:k for k,v in alpnum.items()}
# print(res)

"""ASCII values of alphabets"""
alpha={'a','b','c','d','e'}
alpa_dict={x:ord(x) for x in alpha}
print(alpa_dict)

"""cubes and squares"""
list1=[1,2,3,4,5,6]
res={i**3 if i%2!=0 else i**2 for i in list1}
print(res)