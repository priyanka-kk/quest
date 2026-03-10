"""strings"""
#sequence of characters
#includes letters,numbers,symbols and even whitespaces
#python does not not have a 
#string has a length 
#string is an iterabkle
#For finding ASCII value ord function 
#convert ASCII value to character we use chr()
#characteristics of strings immutable,iterable,ordered,supports slicing,unicode support,dynamic length,holds any characters g
#indexing 
#slicing s[start:stop:step] 
# name="Dheeraj"
# print(name)
# print(type(name))
# numbers="123456789"
# print(numbers)
# print(type(numbers))
# special="@#$%^&()"
# print(special)
# print(type(special))
# emoji="❤️"
# print(emoji)
# print(type(emoji))
# mal="തേജസ്"
# print(mal)
# print(type(mal))
# s='A'
# print(s)
# company="Quest calicut"
# print(len(company))
# num=123
# print(len(str(num)))
# name="Thejas"
# for char in name:
#     print(char,end=" ")

# print(ord("A"))
# print(ord("a"))
# print(chr(65))
# white_spaces="          "
# print(type(white_spaces))
# print(len(white_spaces))
# for i in white_spaces:
#     print(white_spaces)
# s="kello programmers"
# print(s[4])
# print(s[-9])
# print(s[-1]) # to find last character of a string
# print(len(s))

s="Python data types"
# print(s[1:4])
# print(s[1:])
# print(s[:6])
# print(s[0:])
# print(s[::])
# print(s[::1])
# print(s[::2])
# print(s[-1:-5])
# print(s[-5:-1])
# print(s[-5:17])
# print(s[-5:20])
# print(s[-1:-5:-1])
# print(s[::-1])
# print(chr(90))
# place="calicut"
# place+="dist"
# print(place)


# place="calicut"
# place+=5
# print(place)


# place="calicut"
# place+="dist"
# print(place*place)

# place="calicut"
# place+="dist"
# print(place*5)

# place="calicut"
# place+="dist"
# print(place-"cut")

# company="quest calicut"
# print(dir(company))

# print(company.upper())
# print(company.lower())
# print(company.title())
# print(company.capitalize())
# print(company.upper())
# name="DhEEraj"
# print(name.swapcase())

"""searching and finding"""
stack="Python Django"
# print(stack.find('D'))
# print(stack.find('thon'))
# print(stack.find('tnoj'))
# print(stack.find('o'))
# print(stack.rfind('o'))
# print(stack.index('h'))
# print(stack.index('ang'))
# print(stack.index('z'))
# print(stack.index('o'))
# print(stack.rindex('o'))
# text="welcome to my home welcome to ooty"
# print(text.count('welcome')) 
"""validation and checking"""
s='Quest Innovtive Solutions'
# s1=s.upper()
# print(s.isalnum)
# print(s.isalpha()) 
# pincode='686415'
# print(pincode.isdigit())
# space="       "
# print(space.isspace())
# salary="15000"
# print(salary.isdecimal())
# print(s1.isupper())
# print(s.islower())
# print(s.istitle())
# print(s.startswith('Q')
"""Formatting and alignment"""
# s="python"
# print(s.center(25,'*'))
# print(s.ljust(25,"*"))
# print(s.rjust(25,'*'))
# print(s.isascii('e'))
# print(s.zfill(10))
# name="Dheeraj"
# age=14
# print("My name is {1} and i'm {0} years old".format(name,age))
# print("My name is {} and i'm {} years old".format(age,name))
# print("My name is {1} and i'm {0} years old".format(age,name))
# print("My name is {:>10} and i'm {} years old".format(name,age))
# print("My name is {:<10} and i'm {} years old".format(name,age))
# print("My name is {:^10} and i'm {:05} years old".format(name,age))
# print(r"my name is PRIYA \n and \t shony")
# print("abc\" one\" three\`")
# s="welcome to Delhi"
# print(s.split())
s="welcome to Delhi abc akss"
# print(s.split("-"))
# print("hello".split('l'))
# print(s.split("-",3))
# print(s.rsplit(" ",3))
# splitted=s.split()
# print(splitted)
# joined_string="-".join(splitted)
# print(joined_string)
# s1="job=python"
s1="python"
# print(s1.partition("="))
# print(s1.partition("python"))
# print(s1.partition("python"))
# print(s1.partition("x"))
s="my name is Thejas"
# print(s.partition(" "))
# print(s.rpartition(" "))
# print(s.encode(encoding="utf-8",errors="strict"))
# encoded=s.encode()
# decoded=encoded.decode()
# print(decoded)
# print("hello\tpython".expandtabs(50 ))

# print("sayanax".translate({97:'x', 115:'y'}))
# print(chr(111))
# print(chr(108))
# print("Hello world".translate({111:'0',108:'!'}))
# table=s.maketrans('abcxyz','xyzabc')
# print(s.translate(table))
# print(table)


















