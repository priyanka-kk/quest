"""1. Create a string and print it."""
# s="welcome to my home"
# print(s)

"""2. Print each character of a string using indexing."""
s="welcome to my home"
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
s="          Quest Innovative Solutions                "
print(s.strip())

