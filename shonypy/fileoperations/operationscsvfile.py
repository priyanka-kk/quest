"""Section 1: Basic File Operations"""
"""1. Open the CSV file using open() in read mode and print its contents."""
# with open("csvfile.csv",'r') as f:
#     data=f.read()
#     print(data)

"""2. Count the total number of lines in the file."""
# with open("csvfile.csv", 'r') as f:
#     data = f.readlines()
#     count = len(data)
# print("Total number of lines:", count)

"""3. Read only the first 5 rows from the file."""
# with open("csvfile.csv", 'r') as f:
#     data = f.readlines()
#     print(data[0:5])

"""4. Read the file line by line using readline()."""
# with open("csvfile.csv", 'r') as f:
#     line = f.readline()
#     while line!="":
#         print(line.strip())
#         line = f.readline()

"""5. Read all lines using readlines() and display them."""
# with open("csvfile.csv", 'r') as f:
#     data = f.readlines()
# for line in data:
#     print(line.strip())

"""6. Print only the header row of the CSV file."""
# with open("csvfile.csv",'r') as f:
#     data=f.readlines()
#     print(data[0])

"""7. Check whether the file exists before opening it."""
# import os
# if os.path.exists("csvfile.csv"):
#     with open("csvfile.csv", 'r') as f:
#         data = f.read()
#         print(data)
# else:
#     print("File does not exist")

"""8. Close the file manually after reading."""
# files=open("csvfile.csv",'r')
# data=files.read()
# print(data)
# files.close()

"""9. Use with statement to open and read the file."""
# with open("csvfile.csv",'r') as f:
#     data=f.read()
#     print(data)

"""10.Print file size in bytes."""
# import os
# size = os.path.getsize("csvfile.csv")
# print(f"File size: {size} bytes")

"""🔹 Section 2: Working with CSV Data"""
"""1. Read the CSV file using the csv module and
Print all rows as lists."""
# import csv
# with open("csvfile.csv", 'r') as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)

"""2. Print all rows as dictionaries using DictReader."""
# import csv
# with open("csvfile.csv", 'r') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         print(row)

"""3. Extract and print all names from the file."""
# import csv
# with open("csvfile.csv", 'r') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         print(row["Name"])

"""4. Extract and print all cities."""
# import csv
# with open("csvfile.csv", 'r') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         print(row["City"])

"""5. Count how many records are there in total."""
# import csv
# count = 0
# with open("csvfile.csv", 'r') as f:
#     data = csv.reader(f)
#     for row in data:
#         count += 1
# print("Total records:", count)

"""6. Print records where Age > 30."""
# import csv
# with open("csvfile.csv", 'r') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         if int(row["Age"])>30:
#             print(row)

"""7. Print records where City = "Kochi"."""
# import csv
# with open("csvfile.csv", 'r') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         if row["City"]=="Kochi":
#             print(row)

"""8. Count how many people belong to each city."""
# import csv
# city_count = {}
# with open("csvfile.csv", 'r') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         city = row["City"]
#         if city in city_count:
#             city_count[city] += 1
#         else:
#             city_count[city] = 1
# print(city_count)

"""9. Find the maximum age in the dataset."""
# import csv
# ages = []
# with open("csvfile.csv", 'r') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         ages.append(int(row["Age"]))
# print("Maximum age:", max(ages))

"""🔹 Section 3: Writing to CSV. """
"""1. Create a new CSV file and write 5 records manually."""
import csv
with open("csvfile1.csv", "w", newline="") as f:
    datas = csv.writer(f)
    datas.writerow(["ID", "Name", "Age", "City"])
    datas.writerow([101, "Arun", 26, "Bangalore"])
    datas.writerow([102, "Meera", 30, "Hyderabad"])
    datas.writerow([103, "Rahul", 29, "Kolkata"])
    datas.writerow([104, "Anjali", 28, "Kochi"])
    datas.writerow([105, "Nithin", 31, "Delhi"])
    datas.writerow([101, "Arun", 26, "Bangalore"])
    datas.writerow([102, "Meera", 30, "Hyderabad"])
    datas.writerow([103, "Rahul", 29, "Kolkata"])
print("CSV file created successfully")

"""2. Copy contents from original file to a new file."""
import csv
with open("csvfile1.csv", "r", newline="") as f:
    datas = csv.reader(f)
    with open("csvfile2.csv", "w", newline="") as f1:
        writer = csv.writer(f1)
        for row in datas:
            writer.writerow(row)
print("Contents copied successfully")

"""3. Append a new record to the existing CSV file."""
import csv
with open("csvfile1.csv", "a", newline="") as f:
    datas = csv.writer(f)
    datas.writerow(["106", "Arunima", "24", "Kozhikode"])
print("record appended successfully")

"""4.Write only names and ages to a new file."""
import csv
with open("csvfile1.csv",'r',newline="") as f:
    data=csv.reader(f)
    with open("csvfile3.csv",'w',newline="") as f1:
        dataw=csv.writer(f1)
        for row in data:
            dataw.writerow([row[1],row[2]])

"""5. Save filtered data (Age > 25) into a new CSV."""
# import csv
# with open("csvfile1.csv", 'r', newline="") as f:
#     data = csv.reader(f)
#     with open("csvfile4.csv", 'w', newline="") as f1:
#         dataw = csv.writer(f1)
#         for row in data:
#             if int(row[2]) > 25:
#                 dataw.writerow(row) 
#this code got an error  ValueError: invalid literal for int() with base 10: 'Age' 

import csv
with open("csvfile1.csv", 'r', newline="") as f:
    data = csv.reader(f)
    next(data)   # Skip header row
    with open("csvfile4.csv", 'w', newline="") as f1:
        dataw = csv.writer(f1)
        for row in data:
            if int(row[2]) > 25:
                dataw.writerow(row)    
       
"""6. Write a CSV file with custom delimiter (e.g., ;)."""
import csv
with open("csvfile6.csv", "w", newline="") as f:
    datas = csv.writer(f,delimiter=";")
    datas.writerow(["ID", "Name", "Age", "City"])
    datas.writerow([101, "Arun", 26, "Bangalore"])
    datas.writerow([102, "Meera", 30, "Hyderabad"])
    datas.writerow([103, "Rahul", 29, "Kolkata"])
    datas.writerow([104, "Anjali", 28, "Kochi"])
    datas.writerow([105, "Nithin", 31, "Delhi"])
print("CSV file created with delimiter ; successfully")

"""7. Write a file with uppercase names."""
import csv
with open("csvfile1.csv",'r',newline="") as f:
    data=csv.reader(f)
    with open("csvfile5.csv",'w',newline="") as f1:
        dataw=csv.writer(f1)
        for row in data:
            row[1]=row[1].upper()
            dataw.writerow(row)

"""8. Remove duplicate rows (if any) and write to new file."""
import csv
unique_rows=[]
with open("csvfile1.csv",'r',newline="") as f:
    data=csv.reader(f)
    with open("csvfile7.csv",'w',newline="") as f1:
        dataw=csv.writer(f1)
        for row in data:
             if row not in unique_rows:
                unique_rows.append(row)
                dataw.writerow(row)
print("duplicate rows removed") 
 
"""Write sorted data based on Age.
Write data in reverse order.
"""              
