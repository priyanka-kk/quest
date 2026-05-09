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

# string_length=lambda x:len(x)
# print(string_length("Dheeraj"))

# greater_two=lambda a,b:a if a>b else b
# print(greater_two(4,7))

# gratest_of_three=lambda x,y,z:x if x>y and x>z else(y if y>x and y>z else z)
# print(gratest_of_three(35,63,2))

# greater_and_equal=lambda a,b:f"greatest number is {a}" if a>b else(f"greatest number is {b}" if b>a else "both are equal")
# print(greater_and_equal(235,235))   

# multiple_3and5=lambda x: "multiple of 3 and 5" if x%3==0 and x%5==0 else ("multiple of 5" if x%5==0 else  "multiple of 3" )
# print(multiple_3and5(20))   

"""square of a number"""
# def square(nums:int)->int:
#     return nums**2  
# print(square(5))

"""square of a numbers using map()"""
# numbers=[2,5,25,9,7,6,3,2]  
# result2= list(map(lambda x:x**2,numbers))  
# print(result2)  

"""square of aeven numbers """
# elements=[8,92,5,6,7,50,20,30,7,5,68,25]
# result=list(map(lambda x:x**2,filter(lambda y:y%2==0,elements)))
# print(result)

"""Extract the string contains vowels"""
# def has_vowel(word):
#     for ch in word:
#         if ch in 'AEIOUaeiou':
#             return True
#     return False
# names=["welcome","ooty","carrot", 'hhh', 'jjj']   
# r=list(filter(has_vowel,names))       
# print(r)
                # or
# names=['Dheeraj','Thejas','sss']
# result=list(filter(lambda x:any(ch in "AEIOUaeiou" for ch in x),names))
# print(result)

"""Extract only the gmail.com mail ids from user input emails"""
# emails=[]
# for i in range(3):
#     email=input("Enter the emails :")
#     emails.append(email)
# print(emails)
# r=list(filter(lambda x:any(x.endswith(d) for d in ["gmail.com"]),emails))
# print(r)

"""If the number is multiple of 3 then find the cube"""
# l=[3,7,9,12,16,21,15]
# r=list(map(lambda x: x**3,filter(lambda y:y%3==0,l))) 
# print(r) 

"""filter words with length>4 and convert to uppercase"""
# names=["lion","giraffe","elephant","dog"]
# r=list(map(lambda x:x.upper(),filter(lambda y:len(y)>4,names)))
# print(r)

"""reduce function  to find sum of numbers in a list"""
# from functools import reduce
# numbers=[2,5,6,8,9,2,3]
# result=reduce(lambda x,y:x+y,numbers)
# print(result)

"""list of words into a sentence"""
# from functools import reduce
# lst1 = ['hello', ' ' 'world']
# r2 = reduce(lambda x,y: x+y, lst1)
# print(r2)

"""Find maximum value"""
# from functools import reduce
# list1=[1,5,56,34,67,21,89]
# max_value=reduce(lambda x,y:x if x>y else y,list1)
# print(max_value) 
   

"""Find minimum value"""
# from functools import reduce
# list=[1,5,56,34,67,21,89]
# min_value=reduce(lambda x,y:x if x<y else y,list)
# print(min_value) 

"""find highest length word in alist"""
# from functools import reduce
# text=["welcome", "to", "ooty"]
# res=reduce(lambda x,y: x if len(x)>len(y) else y,text)
# print(res)

"""remove duplicate values from a list"""
# from functools import reduce
# numbers=[1,2,3,4,5,6,1,2,3]
# res=reduce(lambda x,y:x+[y] if y not in x else x,numbers,[])
# print(res)

"""decorators"""
# def mydecor(func):
#     def wrapper():
#         print("Function execution started")
#         func()
#         print("Function execution started")
#     return wrapper
# @mydecor
# def greet():
#     print("Hello welcome ...........")
# greet()

"""sttring to uppercase"""
def to_upper(najad_functions):
    def modify(*args):
        print("najad Function execution started ")
        result=najad_functions(*args).upper()
        print("Successfully converted to upper case")
        return result
    return modify
@to_upper
def strings(s):
    return s
print(strings("My name is Najad and i'm a python developer"))