"""1. Write a function greet() that prints Hello, Welcome to Python."""
# def greet():
#     print("Hello,Welcome to Python")
# greet()

"""2. Write a function display_name(name) that prints the given name."""
# def display_name(name):
#     print(name)
# display_name("Priyanka")

"""3. Write a function add(a, b) to return the sum of two numbers."""
# def add(a,b):
#     return a+b
# print(add(6,7))

"""4. Write a function is_even(num) that returns whether a number is even or odd."""
# def is_even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# print(is_even(7))
# print(is_even(8))

"""5. Write a function square(n) that returns the square of a number."""
# def square(n):
#     return n**2
# print(square(6))

"""6. Write a function find_largest(a, b) to return the larger number."""
# def find_largest(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(find_largest(7,9))

"""7. Write a function check_positive(num) to check whether a number is positive, negative, or zero."""
# def check_positive(num):
#     if num>0:
#         return "Positive"
#     elif num<0:
#         return "Negative"
#     else: 
#         return "Zero"
# print(check_positive(-7))

"""8. Write a function multiply(a, b) and call it using user input."""
# def multiply(a,b):
#     return a*b
# print(multiply(9,8))

""" 9. Write a function full_name(first, last) that returns the full name."""
# def full_name(first,last):
#     return f"{first} {last}" 
# print(full_name("Dheeraj","Shony"))

"""10. Write a function calculate_area(length, width) to return the area of a rectangle."""
# def calculate_area(length,width):
#     return length*width
# print(calculate_area(6,8))

"""1.Write a function to return the cube of a number."""
# def cube(num):
#     return num**3
# print(cube(7))

"""2. Write a function to return the reverse of a string."""
# def string_rev(text):
#      return text[::-1]
# print(string_rev("welcome"))

"""3.Write a function to count the number of vowels in a given string."""
# def count_vowels(text):
#     cnt=0
#     for i in text:
#         if i in 'AEIOUaeiou': 
#             cnt+=1
#     return cnt
# print(count_vowels("heater"))

"""4. Write a function to return the factorial of a number."""
# def fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
# print(fact(5))  
    
"""5. Write a function to return the sum of digits of a number."""
# def sum_digits(n):
#     s=0
#     while n>0:
#         d=n%10
#         s=s+d
#         n//=10
#     return s
# print(sum_digits(1234))

"""6.Write a function to return the smallest element in a list."""
# def smallest_element(lst):
#     smallest = lst[0]
#     for num in lst:
#         if num < smallest:
#             smallest = num
#     return smallest
# print(smallest_element([5, 2, 9, 1, 7]))

"""7.Write a function to return the second largest number in a list."""
# def second_largest(lst):
#     unique = list(set(lst)) 
#     unique.sort()
#     return unique[-2]
# print(second_largest([5, 2, 9, 1, 7]))

"""8.Write a function to return the number of words in a sentence."""
# def num_words(text):
#     return len(text.split())
# print(num_words("welcome to ooty delhi bombay"))

"""9.Write a function to return True if a number is a palindrome, otherwise False."""
# def is_palindrome(num):
#     temp = num
#     s = 0
#     while num > 0:
#         d = num % 10
#         s = s * 10 + d
#         num //= 10
#     if temp == s: 
#         return True
#     else:
#          return False
# print(is_palindrome(342))

"""10.  Write a function to return the common elements from two lists."""
# def com_el_lst(list1,list2):
#     res=[]
#     for i in list1:
#         if i in list2 and i not in res:
#             res.append(i)
#     return res
# print(com_el_lst([10,20,30,40,50,60,70],[60,70,80,90,100,10,20]))

"""1.Write a function student_info(name, age, course) and call it using positional arguments."""
# def student_info(name, age, course):
#     print(f"Name: {name}, Age: {age}, Course: {course}")
# student_info("smitha",46,"Python")

"""2. Write the same function and call it using keyword arguments."""
# def student_info(name, age, course):
#     print(f"Name: {name}, Age: {age}, Course: {course}")
# student_info(age=46,name="Smitha",course="Python")

"""3. Write a function power(base, exp=2) that returns the power of a number using a default argument."""
# def power(base,exp=2):
#     return base**exp
# print(power(10))

"""4. Write a function discount(price, percent=10) to calculate discounted price."""
# def discount(price,percent=10):
#     return price - (price * percent / 100)
# print(discount(1000))

"""5.Write a function introduce(name, city='Kochi') and test it with and without the city argument."""
# def introduce(name, city='Kochi'):
#     print(f"My name is {name} and I live in {city}")
# print(introduce("Deepa"))
# print(introduce("Vidya","Kannur"))
 
"""6. Write a function that accepts any number of values using *args and returns their sum."""
# def add_number(*args):
#     total=0
#     for num in args:
#         total+=num
#     return total
# print(add_number(3,6,7,90))

"""7. Write a function that accepts any number of values using *args and returns the largest one."""
def large_number(*args):
    return max(args)
print(large_number(34,45,56,28))

"""8. Write a function that accepts user details using **kwargs and prints each key-value pair."""
def user_details(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
user_details(name="Thejas",age=16,city="Calicut")


"""9
Write a function bill(item, quantity, price) and calculate total bill.
10 Write a function marks_total(*marks) that returns total and average marks."""

