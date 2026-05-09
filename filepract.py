""" Section A: Basic File Opening (r mode)"""
"""1. Write a Python program to open a file in read (r) mode and display its content."""
# with open("sample.txt", "r") as f:
#     print(f.read())
# f.close()

"""2. Write a program to read the first 10 characters from a file."""
# with open("sample.txt", "r") as f:
#     data = f.read(10)
#     print(data)

"""3. Write a program to print all lines using a loop."""
# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line)   

"""4. Write a program to count total characters in a file."""
# with open("sample.txt", "r") as f:
#     data = f.read()
#     count = len(data)-data.count(" ")
#     print("Total characters:", count)

"""5. Write a program to count total lines in a file."""
# with open("sample.txt", "r") as f:
#     count = 0
#     for line in f:
#         count += 1
# print("Total lines:", count)

"""6. Write a program to display only the first line of a file."""
# with open("sample.txt", "r") as f:
#     first_line = f.readline()
#     print(first_line)

"""7. Write a program to display the last line of a file."""
# with open("sample.txt", "r") as f:
#     lines = f.readlines()
#     print(lines[-1])

"""8. Write a program to read a file and print it in uppercase."""
# with open("sample.txt", "r") as f:
#     lines = f.read()
#     print(lines.upper())

"""9. Write a program to read a file and count number of words."""
# with open("sample.txt", "r") as f:
#     data = f.read()
#     words = data.split()
#     print("Total words:", len(words))


"""10. Write a program to check what happens if file does not exist in r mode."""
# with open("test1.txt",'r') as f:
#     data=f.read()
#     print(data)

"""11. Write a program to read a file using with statement."""
# with open("sample.txt",'r') as f:
#     data=f.read()
#     print(data)

"""12. Write a program to check if file is closed after reading."""
# f = open("sample.txt", "r")
# data = f.read()
# print("Is file closed before closing?", f.closed)
# f.close()
# print("Is file closed after closing?", f.closed)

"""13. Write a program to print alternate lines from a file."""
# with open("sample.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines[0::2]:
#         print(line, end="")

"""14.Write a program to read file content and reverse it."""
# with open("sample.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines[::-1]:
#         print(line, end="")

"""full content reverse characterwise"""
# with open("sample.txt","r") as f:
#     lines=f.read()
#     print(lines[::-1])

"""Section B: Writing Files (w mode)"""
"""1. Write a program to create a file using write (w) mode."""
# with open("test2.txt",'w') as f:
#     data=f.write("Hello this is a text file")
#     print(data)

"""2. Write a program to write a single line into a file."""
# with open("test2.txt",'w') as f:
#     data=f.write("Hello this is a file")
#     print(data)

"""3. Write a program to write multiple lines into a file."""
# with open("test2.txt", "w") as f:
#     lines = ["Hello this is a file\n","This is second line\n","This is third line\n"]
#     f.writelines(lines)

"""4. Write a program to overwrite existing file content."""
# with open("test2.txt", "w+") as f:
#     lines = ["Hello this is a file\n","This is second line\n","This is third line\n"]
#     f.writelines(lines)

"""5. Write a program to write user input into a file."""
# with open("test2.txt",'w') as f:
#     userdata=input("Enter the data :")
#     data=f.write(userdata)
#     print(data) # length of string
#     print("data written successfully")

"""6. Write a program to create a file and write numbers from 1 to 10."""
# with open("test3.txt",'w') as f:
#     for i in range(1,11):
#         data=f.write(str(i)+"\n")
#     print("Numbers written successfully in the file") 

"""7. Write a program to write a list of names into a file."""
with open("test2.txt", 'w') as f:
    names = ["Priyanka", "Shony", "Dheeraj", "Thejas"]
    for name in names:
        f.write(name + "\n")
print("Names written successfully!")


"""Write a program to write formatted text into a file.
Write a program to write content and close the file manually.
Write a program using with statement to write into a file.
Write a program to demonstrate that w mode overwrites existing data.
Write a program to write a paragraph into a file.
Write a program to write data and check file size.
Write a program to write lowercase letters into a file.
Write a program to write even numbers into a file.
"""