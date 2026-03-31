

# line_str = input("Please enter a string:")

# line_str2 = line_str[::-1]

# if line_str == line_str2:

#     print (" The string is Plaindrome")
# else:
#     print ("Not palindrome")
""" -----------------------------------------------------"""
# line_str1 = input("Please enter first string:")

# line_str2 = input("Please enter second string:")

# s1=line_str1.lower()

# s2 = line_str2.lower()

# if sorted(s1) == sorted(s2):
#     print("anagrams")
# else:
#     print(" Not a anagrams")
    

# for i in s1:
#     if i not in s2:
#         print(" Not a anagrams")
#         break
# print("  anagrams")

""" ------------------------------------"""

line_str = input("Please enter a string:")
s=line_str.lower()

# p = ""
# a = 0
# b = 0

# for i in s:
#     a= s.count(i)
#     print(f"{i} - {a}")

#     if i in s:

""" another method"""        
# for i in range(len(s)):
#     count = 0
#     for j in range (len(s)):
#         if s[i]== s[j]:
#             count+=1
#     print(s[i],":",count)

""" in built counter method"""
# from collections import Counter

# print(Counter(s))

""" ------------------------------------"""

""" first reapating characor"""

# line_str = input("Please enter a string:")

# s= line_str.lower()

# for i in s:
#     a = s.count(i)
#     if a>1:
#         print (f" The first reapeating char is {i}")
#         break

""" first non reapating characor"""

# line_str = input("Please enter a string:")

# s= line_str.lower()

# for i in s:
#     a = s.count(i)
#     if a==1:
#         print (f" The first non reapeating char is {i}")
#         break

# for i in range (len(s)):
#     for j in range(i+1,len(s)):
#         if s[i]!=s[j]:
#             print

""" 3. Remove duplicate characters from a string."""

# line_str = input("Please enter a string:")
# s=line_str.lower()

# p = ""

# for i in s:
#     if i not in p:
        
#         p = p + i

# print(f"{p}")
    
