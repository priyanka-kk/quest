# #zer0division error
# a=10
# b=0
# print(a/b)

# #valueerror
# num=int("Hell0")
# print(num)

# #typeerror
# string="quest"
# print(string+20)

# #index error
# numbers=[1,2,3,4,5]
# print(numbers[10])
 
# #keyerror
# student={"name": "John", "age":20 }
# print(student["grade"])

# #FileNotFoundError
# open("abc.txt")

# #nameError
# print(x)

# #attribute Error
# text="hello"
# #print(text.uppercase())

# print(text.sort())

# import error
# import Qis

"""zerodivision exception handling"""
# a=int(int(input("Enter First number:")))
# b=int(int(input("Enter First number:")))

# try:
#     print(a/b)
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print("can't divisible by zer0....",e)
# else:
#     print("There is no error in try block")
# finally:
#     print("The code must run")
#     print("Testing.............")


# try:
    
#     a=int(input("Entef First number:"))
#     b=int(int(input("Enter second number:")))
#     print(a+b)

# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print("can't divisible by zer0....",e)
# except Exception as e:
#     print("genaral block",e)
# else:
#     print("There is no error in try block")
# finally:
#     print("The code must run")
#     print("Testing.............")

try:
    import math
except Exception as e:
    print(e)
else:
    print('success')
finally:
    print('done')









