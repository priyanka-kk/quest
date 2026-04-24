# def greet():
#     print("Hello welcome programmers")
# greet() 

# def greet(name):
#     print(f"Hello welcome {name}")
# greet("Dheeraj")
# greet("Thejas")  
# greet("Parthip") 

# def greet(m,n,o):
#     print(f"Hello welcome {m} {n} {o}")
# greet("Shony","Jasil","Shabin") 

# def to_upper(s):
#     return s.upper()
# print(to_upper("Thejas"))

# def to_upper(s:str)->str:
#     """this function converts the strings to upper case"""
#     return s.upper()
# print(to_upper("Thejas"))

# def details(name:str,age:int,phone:list)->str:
#     """this function is used to collect details from user """
#     return name,age,phone
# result=details("Dheeraj",14,[5555555555,777777777])
# print(result)


# def details(name:str,age:int,phone:list)->str:
#     """this function is used to collect details from user """
#     print(name)
#     print(age)
#     print(phone)
# result=details(age=14,name="Dheeraj",phone=[5555555555,777777777])

# def add(n2,n3):
#     return n2+n3
# print(add(2,6))

# def add(n2,n3):
#     return n2+n3
# result=add(2,6)
# print(result)

# def eligibility(age):
#     if age>18:
#         return "eligible"
#     else:
#         return "not eligible"
# print(eligibility(65))

# def add(a,b,c):
#     return a+b+c
# print(add(5,6,7))

# def add(a,b,c=8):
#     return a+b+c
# print(add(5,6))

# def add(a=5,b=6,c=8):
#     return a+b+c
# print(add())

# x=25
# def modify():
#     global x
#     print(x)
#     x=200
# modify()
# print(x)

"""Function to find factorial of a number"""
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

"""Function to find reverse of a string """
# def string_rev(s):
#     if len(s)==0:
#         return s
#     return string_rev(s[1 :])+s[0]
# print(string_rev("welcome"))

"""Function to find reverse of a number"""
# def find_rev(num):
#     s=0
#     while num>0:
#         d=num%10
#         s=s*10+d
#         num//=10
#     return s 
# print(find_rev(456))

# def square(a):
#     return a**2
# print(square(5))

# sq=lambda a:a**2
# print(sq(5))

# total=lambda a,b,c:a+b+c
# print(total(4,6,9))

# even_odd=lambda x:x**2 if x%2==0 else x**3
# print(even_odd(5))
# print(even_odd(8))









