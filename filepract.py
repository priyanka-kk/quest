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
# with open("test2.txt", 'w') as f:
#     names = ["Priyanka", "Shony", "Dheeraj", "Thejas"]
#     for name in names:
#         f.write(name + "\n")
# print("Names written successfully!")

"""8. Write a program to write formatted text into a file."""
# name = "Sanand"
# age = 17
# course = "Python Programming"
# with open("student.txt", "w") as f:
#     f.write(f"Student Name : {name}\n")
#     f.write(f"Age          : {age}\n")
#     f.write(f"Course       : {course}\n")
# print("Formatted text written successfully.")

"""9. Write a program to write content and close the file manually."""
# name = "Sanand"
# age = 17
# course = "Python Programming"
# f=open("student.txt", "w")
# f.write(f"Student Name : {name}\n")
# f.write(f"Age          : {age}\n")
# f.write(f"Course       : {course}\n")
# print("Formatted text written successfully.")
# f.close()

"""10. Write a program using with statement to write into a file."""
# with open("test2.txt",'w') as f:
#     data=f.write("Hello this is a text file")
#     print(data)

"""10. Write a program to demonstrate that w mode overwrites existing data."""
# with open("test2.txt",'w') as f:
#     data=f.write("Hello welcome to Ooty")
#     print(data)

"""11. Write a program to write a paragraph into a file."""
# paragraph="""Onam is the most famous festival of Kerala.
# It is a harvest festival celebrated with joy.It also includes
# traditional food, flower decorations, dances, and games"""
# with open("paragraph.txt",'w') as f:
#     data=f.write(paragraph)
#     print(data)
# print("paragraph written sucessfully")

"""12. Write a program to write data and check file size."""
# paragraph="""Onam is the most famous festival of Kerala.
# It is a harvest festival celebrated with joy.It also includes
# traditional food, flower decorations, dances, and games"""
# with open("paragraph.txt",'w') as f:
#     data=f.write(paragraph)
#     print(f"file size={data}")

"""13. Write a program to write lowercase letters into a file."""
# letters="A,B,C,D,E,F,G"
# with open("test2.txt",'w') as f:
#     data=f.write(letters.lower())
#     print(data)
# print("lower case letters written successfully")

"""14. Write a program to write even numbers into a file."""
# even_nums="2,4,6,8,10,12,14"
# with open("test2.txt",'w') as f:
#     data=f.write(even_nums)
#     print(data)
# print("Even numbers written successfully")

"""Section C: Read + Write Mode (r+)"""
""" 1. Write a program to open a file in r+ mode and display content."""
# with open("test3.txt","r+") as f:
#     data=f.read()
#     print(data)

"""2. Write a program to read a file and then write additional data using r+."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     print("Existing Content:")
#     print(data)
#     f.write("\nThis is additional data.")
# print("New data added successfully.")

"""3. Write a program to overwrite the beginning of a file using r+."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     print("Existing Content:")
#     print(data)
#     f.seek(0)
#     f.write("This is additional data.")
# print("New data added successfully.")

"""4. Write a program to modify the first line of a file using r+."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     print("Existing Content:")
#     print(data)
#     f.seek(0)
#     f.write("This is the first line.")
# print("Modify the first line successfully.")

"""5. Write a program to read and append data using r+."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     print("Existing Content:")
#     print(data)
#     f.write("\nwelcome to Delhi")
# print("append the data successfully.")

"""6. Write a program to move file pointer and write data."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     print("Existing Content:")
#     print(data)
#     f.seek(0)
#     f.write("This is the first line.")
# print("Modify the first line successfully.")

"""7.Write a program to demonstrate pointer position in r+ mode."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     print("Existing Content:")
#     print(data)
#     f.seek(0)
#     f.write("This is the first line.")
#     print(f.tell())

"""8. Write a program to update specific content in a file using r+."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     updated_data = data.replace("Delhi", "Agra")
#     f.seek(0)
#     f.write(updated_data)
# print("File content updated successfully.")

"""9. Write a program to replace a word in a file using r+."""
# with open("test3.txt", "r+") as f:
#     data = f.read()
#     updated_data = data.replace("welcome", "journey")
#     f.seek(0)
#     f.write(updated_data)
# print("a word in a file is replaced successfully.")

"""10. Write a program to read and rewrite file content using r+."""
# with open("test3.txt", "r+") as f:
#     content = f.read()
#     print(content)
#     f.seek(0)
#     f.write("This file content has been rewritten.")
# print("File updated successfully.")

"""🔹 Section D: Mixed Practice Questions."""
"""1. Write a program to copy content from one file to another using r and w."""
# with open("paragraph.txt", "r") as source:
#     content = source.read()
# with open("destination.txt", "w") as destination:
#     destination.write(content)
# print("Content copied successfully.")

"""2. Write a program to merge two files into a third file."""
# with open("test2.txt",'r') as f1:
#     data1=f1.read()
# with open("test3.txt",'r') as f2:
#     data2=f2.read()
# with open("merged.txt","w") as f3:
#     f3.write(data1)
#     f3.write("\n")
#     f3.write(data2)
# print("Merged two files successfully")

"""3. Write a program to read file and write only vowels into another file."""
# with open("test3.txt",'r') as f:
#     data1=f.read()
# with open("test4.txt",'w') as f1:
#     for ch in data1:
#         if ch in 'AEIOUaeiou': 
#             f1.write(ch)
# print("vowels copied sucessfully")

"""4. Write a program to read file and write only consonants into another file."""
# with open("test3.txt",'r') as f:
#     data1=f.read()
# with open("test5.txt",'w') as f1:
#     for ch in data1:
#         if ch not in 'AEIOUaeiou': 
#             f1.write(ch)
# print("consonants copied sucessfully")

"""5. Write a program to read numbers from file and write their squares into another file."""
# with open("test2.txt",'r') as f:
#     data=f.read().split()
# with open("test6.txt",'w') as f1:
#     for i in data:
#         sq=int(i)**2
#         f1.write(str(sq)+" ")
# print("squares written successfully")

"""6. Write a program to read file and remove blank lines."""
# with open("test5.txt", 'r') as f:
#     lines = f.readlines()
# for line in lines:
#     if line.strip() != "":
#         print(line, end="")

"""7. Write a program to read file and write reversed lines into another file."""
# with open("test5.txt", 'r') as f:
#     lines = f.readlines()
# with open("text8.txt", 'w') as f1:
#     for line in lines:
#         rev = line.strip()[::-1]
#         f1.write(rev + "\n")

"""8. Write a program to read file and count frequency of a word."""
# with open("paragraph.txt", 'r') as f:
#     data = f.read().split()
# word = input("Enter word to search: ")
# cnt = data.count(word)
# print(f"Frequency of {word} is {cnt}")

"""9. Write a program to read file and write unique words into another file."""
# with open("paragraph.txt", 'r') as f:
#     data = f.read().split()
# unique = []
# for word in data:
#     if data.count(word) == 1:
#         unique.append(word)
# with open("test9.txt", 'w') as f1:
#     f1.write(str(unique))

"""10.  Write a program to read file and write lines starting with a vowel into another file."""
# with open("paragraph.txt", 'r') as f:
#     data = f.readlines()
# s = []
# for line in data:
#     if line.strip() and line[0].lower() in "aeiou":
#         s.append(line)
# with open("test10.txt", 'w') as f1:
#     f1.writelines(s)
# print("Lines starting with vowels written successfully")


"""🔹 Section E: Small Practical Tasks. """
"""1. Create a file student.txt, write student names, then read and display them."""
# names = ["Dheeraj", "Thejas", "Parthip", "Sanand"]
# with open("student.txt", "w+") as f:
#     f.write("\n".join(names))   # write names line by line
#     f.seek(0)   # move pointer to beginning
#     data = f.read()
#     print(data)

"""2. Create a file marks.txt, write marks, then read and calculate total."""
# marks=[45,48,47,43,49]
# with open("marks.txt",'w+') as f:
#     f.write(str(marks))
#     f.seek(0)
#     data=f.read()
#     total=sum(marks)
#     print(total)

"""3. Create a file and update its first line using r+."""
# dances=["bharathanatyam","mohiniyattam","kathakali","ottanthullal"]
# with open("sample.txt",'w') as f:
#     data=f.write("\n".join(dances))
# with open("sample.txt",'r+') as f1:
#     f1.seek(0)
#     data1=f1.write("Chakyarkoothu")
#     print(data1)

"""4. Read a file and duplicate its content into another file."""
# with open("sample.txt",'r') as f:
#     data=f.read()
# with open("text11.txt" ,'w') as f1:
#     f1.write(data) 

"""5. Write a program to demonstrate all three modes (r, w, r+) in one program."""
#w mode -> create file and write content
# with open("demo.txt", "w") as f:    
#     f.write("Python File Handling\n")    
#     f.write("This file is created using w mode.\n")
#     print("Content written using w mode.\n")
# r mode -> read file content
# with open("demo.txt", "r") as f:    
#     data = f.read()
#     print("Reading using r mode:")
#     print(data)
#r+ mode -> read and update file
# with open("demo.txt", "r+") as f:    
#     old_data = f.read()   
#     print("Existing Content in r+ mode:")   
#     print(old_data)    
#     f.seek(0)    
#     f.write("Updated First Line\n")
#     print("\nFile updated using r+ mode.")
 # Display final content
# with open("demo.txt", "r") as f:    
#     final_data = f.read()
#     print("\nFinal File Content:")
#     print(final_data)





            



