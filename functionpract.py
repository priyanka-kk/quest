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
# def large_number(*args):
#     return max(args)
# print(large_number(34,45,56,28))

"""8. Write a function that accepts user details using **kwargs and prints each key-value pair."""
# def user_details(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
# user_details(name="Thejas",age=16,city="Calicut")

"""9. Write a function bill(item, quantity, price) and calculate total bill."""
# def bill(item, quantity, price):
#     total_bill=quantity*price
#     return f"Item: {item}, Total Bill: {total_bill}"
# print(bill("soap",2,50))
"""10 Write a function marks_total(*marks) that returns total and average marks."""
# def marks_total(*marks):
#     if len(marks) == 0:
#         return 0, 0
#     total_marks=sum(marks)
#     avg_marks=total_marks/len(marks)
#     return f"Total marks={total_marks},Average marks={avg_marks}"
# print(marks_total(45,50,55,60,65))

"""1. Write a function to check whether a string is a palindrome."""
# def str_palindrome(text):
#     if text[::-1]==text:
#         return "palindrome"
#     else:
#         return "not palindrome" 
# print(str_palindrome("malayalam"))

"""2. Write a function to count uppercase and lowercase letters in a string."""
# def count_lowerupper(text):
#     upper_count=0
#     lower_count=0
#     for i in text:
#         if i.isupper():
#             upper_count+=1
#         elif i.islower():
#             lower_count+=1
#     return f"upper count={upper_count},lower count={lower_count}"
# print(count_lowerupper("Welcome To Ooty"))

"""3. Write a function to remove all spaces from a string."""
# def remove_space(text):
#     res=text.replace(" ","")
#     return res
# print(remove_space("Welcome To Ooty"))
    
"""4. Write a function to find the frequency of a given character in a string."""
# def freq_char(text,ch):
#     return text.count(ch)
# print(freq_char('character','c'))
                      
"""5.Write a function to convert the first letter of each word to uppercase."""
# def fl_toupper(text):
#     res=text.title()
#     return res
# print(fl_toupper("welcome to ooty"))

"""6. Write a function to replace all vowels in a string with '*'."""
# def rep_vowels(text):
#     for i in text:
#         if i in 'AEIOUaeiou':
#             text = text.replace(i, '*')
#     return text
# print(rep_vowels("dheeraj"))

"""7. Write a function to check whether two strings are anagrams."""
# def check_anagram(text1,text2):
#     if sorted(text1)==sorted(text2):
#         return "anagrams"
#     else:
#         return "not anagrams"
# print(check_anagram("care","race"))

"""8. Write a function to return the longest word in a sentence."""
# def long_word(text):
#     words = text.split()
#     return max(words, key=len)
# print(long_word("welcome to Thiruvananthapuram"))

"""9. Write a function to count how many times a word appears in a sentence."""
# def word_count(text1, text2):
#     words = text1.split()
#     return words.count(text2)
# print(word_count("My dog is cute and my dog is black", "dog"))

"""10 Write a function to split a sentence and return only words with length greater than 4"""
# def len_great4(text):
#     s=[]
#     words=text.split()
#     for i in words:
#         if len(i)>4:
#             s.append(i)
#     return s
# print(len_great4("welcome hello cat dog"))

"""1. Write a function to return only even numbers from a list."""
# def even_numbers(numbers):
#     list1=[i for i in numbers if i%2==0]
#     return list1       
# print(even_numbers([2,5,8,7,9,4,10,16,15,13,19]))

"""2.Write a function to return only prime numbers from a list."""
# def prime_numbers(numbers):
#     primes = []
#     for n in numbers:
#         if n > 1:
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     break
#             else:
#                 primes.append(n)
#     return primes
# print(prime_numbers([2,5,8,7,9,4,10,16,15,13,19]))

"""3. Write a function to remove duplicates from a list without changing the order."""
# def rem_duplicates(numbers):
#     result = []
#     for i in numbers:
#         if i not in result:
#             result.append(i)
#     return result
# print(rem_duplicates([2,5,8,7,9,4,10,16,15,13,19,2,5,7]))

"""4. Write a function to return the sum of all odd numbers in a list."""
# def sum_oddnos(numbers):
#     total=0
#     for i in numbers:
#         if i%2!=0:
#             total+=i
#     return total
# print(sum_oddnos([2,5,8,7,9,4,10,16,15,13,19]))

"""5. Write a function to find the index positions of a given element in a list."""
# def find_index(numbers, num):
#     result = []
#     for i in range(len(numbers)):
#         if numbers[i] == num:
#             result.append(i)
#     return result
# print(find_index([2,5,8,7,9,4,10,16,15,13,19], 10))

"""6. Write a function to merge two lists and return a sorted result."""
# def merge_list(list1,list2):
#     return sorted(list1+list2)
# print(merge_list([2,5,8,7,9,4,10],[16,15,13,19]))

"""7.Write a function to count positive and negative numbers in a list."""
# def cnt_posneg(numbers):
#     cp=0
#     cn=0
#     for i in numbers:
#         if i>0:
#             cp+=1
#         elif i<0:
#             cn+=1
#     return cp,cn
# print(cnt_posneg([2,5,-8,7,9,-4,10,-16,15,-13,19]))

"""8. Write a function to return the maximum difference between two elements in a list"""
        

