"""1. Create a string and print it."""
# s="welcome to my home"
# print(s)

"""2. Print each character of a string using indexing."""
# s="welcome to my home"
# for i in range(len(s)):
#     print(s[i])

"""3. Print the first and last character of a string."""
# s="welcome to my home"
# print(f"The first character is {s[0]}")
# print(f"The last character is {s[-1]}")

"""4. Demonstrate positive and negative indexing on a string."""
# s="python programming"
# print(s[0::]) #positive indexing from left to right
# print(s[::-1]) #negative indexing from rifht to right 

"""5. Extract the first five characters from a string using slicing."""
# s="python programming"
# print(s[0:5])

"""6. Reverse a string using slicing."""
# s="python programming"
# print(s[::-1])

"""7. Count the length of a string without using len()."""
# count=0
# s="python programming"
# for i in s:
#     count+=1 
# print(f"The length of the string is {count}")

"""8. Convert a string to uppercase and lowercase."""
# s="python programming"
# up=s.upper()
# print(f"upper case {up}")
# print(f"lower case {up.lower()}")

"""9. Capitalize the first letter of a string."""
# s="python programming"
# print(s.capitalize())

"""10. Swap the case of each character in a string"""
# s="PYTHON programming"
# print(s.swapcase())

"""11. Check whether a string starts with a specific substring."""
# s="Quest Innovative Solutions"
# print(s.startswith('Q'))

"""12. Check whether a string ends with a specific substring."""
# s="Quest Innovative Solutions"
# print(s.endswith('s'))

"""13. Count the number of occurrences of a character in a string."""
# s="Quest Innovative Solutions"
# print(s.count('n'))

"""14. Replace a word in a string with another word."""
# s="Quest Innovative Solutions"
# print(s.replace('Quest','Talent'))

"""15. Remove leading and trailing spaces from a string."""
# s="          Quest Innovative Solutions                "
# print(s.strip())

"""INTERMEDIATE LEVEL"""
"""1. Check whether a string contains only alphabets."""
# s="welcometoKozhikode"
# print(s.isalpha())

"""2. Check whether a string contains only digits."""
# n="12345678910"
# print(n.isdigit())

"""3. Check whether a string is alphanumeric."""
# s="abcdefghijklmn123356778"
# print(s.isalnum())

"""4. Split a sentence into words using split()."""
# s="seena sings a song"
# print(s.split())

"""5. Join a list of words into a single string."""
# text=["welcome","to","my","home"]
# joined=" ".join(text)
# print(joined)

"""6. Find the first occurrence of a substring in a string."""
# s="abc abcd abcdef abcdefg"
# print(s.find("d"))

"""7. Find the last occurrence of a substring in a string."""
# s="mathematics"
# print(s.rfind("a"))

"""8. Remove a prefix from a string."""
# s="Dr.Jayasree Rajagopal"
# print(s.removeprefix("Dr."))

"""9. Remove a suffix from a string."""
# s="Dr.Jayasree Rajagopal MBBS DNB"
# print(s.removesuffix("DNB"))

"""10. Center align a string within a given width."""
# s="Happy Onam"
# print(s.center(25))

"""11. Left justify and right justify a string."""
# s="Happy Onam"
# print(s.ljust(25))
# print(s.rjust(25))

"""12. Pad a number string with zeros using zfill()."""
# s="Happy Onam"
# print(s.zfill(15))

"""13. Use format() method in string formatting."""
# name1="Thejas"
# name2="Aadidev"
# print("My name is {} and my friend's name is {}".format(name1,name2))

"""14. Create a formatted string using f-strings."""
# a=8 
# b=14
# print(f"the sum of numbers {a} and {b} are {a+b}")

"""15. Use partition() to split a string into three parts."""
# s="I=love my country"
# print(s.partition("="))

"""Logical problem solving"""
"""1. Check whether a string is a palindrome."""
# s=input("enter a string")
# temp=s
# reverse=s[::-1]
# if reverse==temp:
#     print("The string is palyndrome")
# else:
#     print("The string is not palyndrome")

"""2. Count the number of vowels and consonants in a string."""

# s=input("Enter a string:")
# vcount=0
# slen=len(s)
# for i in range(slen):
#     if s[i] in 'aeiouAEIOU':
#         vcount+=1
# ccount=slen-vcount
# print(f"The number of vowels in the string is {vcount}")
# print(f"The number of consonants in the string is {ccount}")

"""3. Remove duplicate characters from a string."""
# s=input("Enter a string:")
# res=""
# for char in s:
#     if char not in res:
#         res+=char
# print(f"String after removing : {res}")

"""4. Find the most frequent character in a string."""
# s=input("Enter a string:")
# p=""
# a=0
# b=0
# for i in s:
#     a=s.count(i)
#     if a>b:
#         b=a
#         p=i
# print(f"The most frequent character is {p} repeated {b} times")

"""5. Check if two strings are anagrams."""
# t1=input("Enter first string:")
# t2=input("Enter second string:")
# a=t1.lower()
# b=t2.lower()
# if sorted(a)==sorted(b):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

"""6. Reverse each word in a sentence without reversing the sentence order"""
# s=input("Enter a string:")
# s1=s.split()
# p=""
# for i in s1:
#     p=p+" "+i[::-1]
# print(f"The reversed string is {p.strip()}")

"""7. Find the longest word in a sentence"""
# s=input("Enter the string :")
# sp=s.split()
# a=0
# b=0
# p=""
# for i in sp:
#     a=len(i)
#     if a>b:
#         b=a
#         p=i
# print(f"The largest word in a sentence is {p}")

"""9. Remove all spaces from a string."""
# s=input("Enter a string :")
# a=s.replace(" ","")
# print(a)

"""10. Convert the first letter of every word to uppercase without using title()"""
# s=input("Enter a string :")
# a=s.split()
# p=""
# for i in a:
#     p=p+" "+i.capitalize()
# print(p.strip())

"""11. Extract digits from a string and store them separately."""
# s=input("Enter a string :")
# p=""
# for i in s:
#     if i.isdigit():
#         p=p+str(i)
# print(p)

"""12. Count the number of words in a sentence"""
# s=input("Enter a string :")
# count=0
# a=s.split()
# for i in a:
#     count+=1
# print(count)

"""13. Replace multiple spaces with a single space."""
# s=input("Enter a string :")
# a=s.replace("  "," ")
# print(a)

"""14. Check whether a string contains special characters"""
# s=input("Enter a string :")
# if s.isalnum():
#     print("No special characters")
# else:
#     print("Special characters present")

"""15. Find the ASCII value of each character."""
# s=input("Enter a string :")
# for i in s:
#     a=ord(i)
#     print(f"{i} : {a}")
    

