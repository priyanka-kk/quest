"""1. Create a dictionary representing a 'Laptop' with keys: brand, model, and price."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# print(laptop)

"""2. Access the value of the 'model' key using square brackets."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# print(laptop['model'])

"""3. Access the value of a key that doesn't exist using .get() and explain why it's safer than []."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# print(laptop.get('size')) # by using get() Returns None (or a default value if provided)
# No error
# Safe to use when you're not sure if the key exists
# by using [] Raises an error:
# KeyError: 'size'

"""4. Create an empty dictionary using both {} and the dict() constructor."""
# d={}
# print(d)
# d=dict()
# print(d)

"""5. Add a new key-value pair 'processor': 'i7' to an existing dictionary."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# laptop.update(processor='i7')
# print(laptop)

"""6. Update the 'price' of the laptop to a new value."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# laptop.update(price=65000)
# print(laptop)

"""7. Use the len() function to find how many key-value pairs are in a dictionary."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# print(len(laptop))

"""8. Create a dictionary where the keys are numbers 1 to 5 and the values are their squares."""
# num_sqs={1:1,2:4,3:9,4:16,5:25}
# print(num_sqs)

"""9. Check if a specific key exists in a dictionary using the 'in' operator."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# print('model' in laptop)

"""10. Delete a key-value pair using the 'del' keyword and handle the case if the key is missing."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# del(laptop['model'])
# del(laptop['size'])
# print(laptop)

"""11. Use the pop() method to remove a key and store its value in a variable."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# d=laptop.pop('model')
# print(laptop)
# print(d)

"""12. Use popitem() to remove the last inserted item and explain its behavior in Python 3.7+."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# d=laptop.popitem()
# print(laptop)
# print(d) #Behavior in Python 3.7+
# Dictionaries maintain insertion order
# .popitem() removes the last inserted item (LIFO - Last In, First Out)

"""13. Use the keys() method to print all the keys in a dictionary."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# d=laptop.keys()
# print(d)

"""14. Use the values() method to print all the values in a dictionary."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# d=laptop.values()
# print(d)

"""15. Use the items() method to iterate through a dictionary and print "Key: Value" for each
pair."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# for key, value in laptop.items():
#     print(f"{key} : {value}")

"""16. Merge two dictionaries: {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using the update() method."""
# d1={'a':1,'b':2}
# d2={'c':3,'d':4}
# d1.update(d2)
# print(d1)

"""17. Clear all items from a dictionary using the clear() method."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# laptop.clear()
# print(laptop)

"""18. Use the setdefault() method to add a key 'country' with value 'India' only if it doesn't exist."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# laptop.setdefault('country','India')
# print(laptop)

"""19. Create a shallow copy of a dictionary and show that modifying the copy doesn't change
 the original."""
# laptop={'brand':'HP','model':'Victus','price':60000}
# c=laptop.copy()
# c['price'] = 50000
# print("Original:", laptop)
# print("Copy:", c)

"""20. Create a dictionary from two lists: one for keys and one for values using the zip()
function."""
# states=['Kerala','karnataka','Goa']
# capitals=['Thiruvananthapuram','Bangaluru','Panaji']
# res=dict(zip(states,capitals))
# print(res)

"""21. Create a nested dictionary called 'Employees' containing data for three different people."""
# employees={
#     'employee1':{'name':'Sandhya','job':'teacher','salary':40000},
#     'employee2':{'name':'Febina','job':'Engineer','salary':60000},
#     'employee3':{'name':'Shahana','job':'Doctor','salary':65000},
# }
# print(employees)

"""22. Access a value inside a nested dictionary (e.g., Employees['emp1']['salary'])."""
# employees={
#     'employee1':{'name':'Sandhya','job':'teacher','salary':40000},
#     'employee2':{'name':'Febina','job':'Engineer','salary':60000},
#     'employee3':{'name':'Shahana','job':'Doctor','salary':65000},
# }
# print(employees['employee1']['salary'])
# print(employees['employee3']['name'])

"""23. Update a value inside a nested dictionary."""
# employees={
#     'employee1':{'name':'Sandhya','job':'teacher','salary':40000},
#     'employee2':{'name':'Febina','job':'Engineer','salary':60000},
#     'employee3':{'name':'Shahana','job':'Doctor','salary':65000},
# }
# employees['employee3']['phoneno']=8547690846
# print(employees)

"""24. Add a new nested dictionary (a new employee) to the existing 'Employees' structure."""
# employees={
#     'employee1':{'name':'Sandhya','job':'teacher','salary':40000},
#     'employee2':{'name':'Febina','job':'Engineer','salary':60000},
#     'employee3':{'name':'Shahana','job':'Doctor','salary':65000},
# }
# employees['employee4']={'name':'Manju','job':'Designer','salary':45000}
# print(employees)

"""25. Write a loop to print only the names of all employees from the nested 'Employees'
dictionary."""
# employees={
#     'employee1':{'name':'Sandhya','job':'teacher','salary':40000},
#     'employee2':{'name':'Febina','job':'Engineer','salary':60000},
#     'employee3':{'name':'Shahana','job':'Doctor','salary':65000},
# }
# for key,value in employees.items():
#     print(value['name'])

"""26.  Create a dictionary where a key points to a list of values (e.g., 'hobbies': ['coding',
'reading'])."""
# person={'name':'Sandhya','job':'teacher','salary':40000,'hobbies': ['coding','reading']}
# print(person)

"""27. Append a new hobby to the list inside that dictionary."""
# person={'name':'Sandhya','job':'teacher','salary':40000,'hobbies': ['coding','reading']}
# person['hobbies'].append('dancing')
# print(person)

"""28. Given a dictionary of students and their marks (a list), calculate the average marks for one
student."""
# students = {
#     'stud1': {'name':'Dheeraj','id':101,'marks':[50,60,65,55]},
#     'stud2': {'name':'Thejas','id':102,'marks':[55,65,60,75]},
#     'stud3': {'name':'Parthip','id':103,'marks':[60,70,65,55]}
# }
# m = input("Enter student key (stud1/stud2/stud3): ")
# if m in students:
#     marks = students[m]['marks']
#     avg = sum(marks) / len(marks)
#     print("Average marks:", avg)
# else:
#     print("Student not found")

"""29. Flatten a simple nested dictionary (convert {'a': {'b': 1}} to {('a', 'b'): 1})."""
# d = {'a': {'b': 1}}
# flat_dict = {}
# for key, value in d.items():
#     for inner_key, inner_value in value.items():
#         flat_dict[(key, inner_key)] = inner_value
# print(flat_dict)

"""30. Represent a JSON response from a weather API as a nested dictionary and extract the
'temperature'."""
# weather_data = {
#     "location": "Calicut",
#     "current": {
#         "temperature": 32,
#         "humidity": 70,
#         "weather": "Cloudy"
#     }
# }
# temp = weather_data["current"]["temperature"]
# print("Temperature:", temp)

"""31. [Comprehension] Create a dictionary of even numbers between 1-10 as keys and their
cubes as values."""
# even_cube={x:x**3 for x in range(1,11) if x%2==0}
# print(even_cube)

"""32.[Comprehension] Given a dictionary, create a new one with only items where the value is
> 100."""
# d={1:100,2:120,3:130,4:90,5:80,6:140}
# gr_100={k:v for k,v in d.items() if v>100 }
# print(gr_100)

"""33. [Comprehension] Swap keys and values in a dictionary (Reverse Mapping)."""
# d={1:100,2:120,3:130,4:90,5:80,6:140}
# swap_d={v:k for k,v in d.items()}
# print(swap_d)

"""34. Sort a dictionary by its keys in alphabetical order. """
# d={'d':10,'a':20,'f':30,'c':40,'e':50,'b':60}
# sort_d={k:d[k] for k in sorted(d)}
# print(sort_d)
            # or
# d={'d':10,'a':20,'f':30,'c':40,'e':50,'b':60}
# sort_d=dict(sorted(d.items()))
# print(sort_d)

"""35. Sort a dictionary by its values in ascending order."""
# d = {'d':60,'a':10,'f':50,'c':40,'e':20,'b':30}
# sort_d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
# print(sort_d)

"""36. Find the key with the maximum value in a dictionary of product prices."""
# prices = {'TV':30000,'Fridge':26000,'Washing machine':33000}
# max_price = 0
# max_key = ""
# for k, v in prices.items():
#     if v > max_price:
#         max_price = v
#         max_key = k
# print(max_key)

"""37. Count the frequency of each character in a string "Python Trainer" using a dictionary."""
s="Python Trainer" 
# freq = {}
# for ch in s:
#     if ch!=" ":
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1
# for k, v in freq.items():
#     print(f"{k} : {v}")

"""38. Combine two dictionaries by adding values for common keys."""
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 5, 'c': 15, 'd': 25}
# result = {}
# for key in d1: 
#     result[key] = d1[key]
# for key in d2:
#     result[key] = result.get(key, 0) + d2[key]
# print(result)

"""39. Convert a dictionary into a list of tuples."""
# d1 = {'a': 10, 'b': 20, 'c': 30}
# print(list(d1.items()))

"""40. Check if all values in a dictionary are the same."""
# d = {'a': 10, 'b': 10, 'c': 10}
# if len(set(d.values())) == 1:
#     print("All values are the same")
# else:
#     print("Values are different")

"""42. [Data Cleaning] Remove all keys from a dictionary that have None or empty string
values.
43. [Security] Explain why a list cannot be used as a dictionary key, but a tuple can.
44. [Logic] Write a program to find the sum of all values in a numeric dictionary.
45. [Simulation] Use a dictionary to simulate a simple "Switch-Case" statement logic.
46. [Efficiency] Compare the time it takes to find a value in a list of 10,000 items vs. a
dictionary.
47. [Functionality] Use **kwargs in a function to accept arbitrary keyword arguments as a
dictionary.
48. [Mapping] Create a dictionary to map Roman numerals to Integers (e.g., 'I': 1, 'V': 5).
49. [Logic] Given a list of words, group them by their starting letter using a dictionary.
50. [Interview Question] Explain the difference between '==' and 'is' when comparing two
identical dictionaries."""

"""42. [Data Cleaning] Remove all keys from a dictionary that have None or empty string
values."""
# d= {1:10,2:20,3:30,4:"",5:None,6:50,7:""}
# s={}
# for k,v in d.items():
#     if v!="" and v is not None:
#       s[k]=v
# print(s)

"""44. Write a program to find the sum of all values in a numeric dictionary."""
d= {1:10,2:20,3:30,4:40,5:50,6:60,7:70}
for k,v in d.items():
    s=sum(d.values())
print(s)
