"""1. Write a function `company_welcome()` that prints:"Welcome to Python Full Stack Lab" """ 
# def company_welcome():
#     print("Welcome to Python Full Stack Lab")
# company_welcome()

"""2. Write a function `display_course_name()` and call it 3 times."""
# def display_course_name():
#     print("Python Full Stack")
# display_course_name()
# display_course_name()
# display_course_name()  

"""3. Create a function `show_lab_rules()` that prints at least 5 lab instructions."""
# def show_lab_rules():
#     print("Maintain silence")
#     print("Handle keyboard,mouse,monitor gently")
#     print("Use the internet only for educational purpose")
#     print("Save your work properly")
#     print("shut down the compuer properly before leaving")
# show_lab_rules()

"""4. Write a function `student_info(name)` that prints:
   "Hello <name>, welcome to the Python lab" """
# def student_info(name):
#     print(f"Hello {name},welcome to the Python lab")
# student_info("Priyanka")

"""5. Write a function `add_two_numbers(a, b)` that returns the sum."""
# def add_two_numbers(a, b):
#     return a+b
# print(add_two_numbers(6,7)) 

"""6. Write a function `multiply_three_numbers(a, b, c)` that returns the result."""
# def multiply_three_numbers(a, b, c):
#     return a*b*c
# print(multiply_three_numbers(4, 5, 3))

"""7. Write a function `is_even(num)` that returns True if the number is even, otherwise False."""
# def is_even(num):
#     return True if num%2==0 else False
# print(is_even(8))

"""8. Write a function `find_square(n)` that returns the square of a number."""
# def  find_square(n):
#     return n**2
# print(find_square(7))

"""9. Write a function `find_cube(n)` that returns the cube of a number.""" 
# def find_cube(n):
#     return n**3
# print(find_cube(5))

"""10. Write a function `full_name(first_name, last_name)` that returns the full name."""
# def full_name(first_name, last_name):
#     return first_name+" "+last_name
# print(full_name("Shony", "Gangadharan"))

"""11. Write a function `calculate_discount(price, discount_percent)` that returns the final price."""
# def calculate_discount(price, discount_percent):
#     return price-(price*discount_percent)
# print(calculate_discount(1000,0.2))

"""12. Write a function `fahrenheit_to_celsius(temp)` that returns the Celsius value."""
# def fahrenheit_to_celsius(temp):
#     return (temp-32)*(5/9)
# print(fahrenheit_to_celsius(95))

"""13. Write a function `calculate_area_of_rectangle(length, width)`."""
# def calculate_area_of_rectangle(length, width):
#     return length*width
# print(calculate_area_of_rectangle(8, 12)) 

"""14. Write a function `calculate_simple_interest(p, r, t)`."""
# def calculate_simple_interest(p, r, t):
#     return (p*r*t)/100
# print(calculate_simple_interest(1000, 20, 2))

"""15. Write a function `generate_email(username, domain)` that returns a professional email ID."""
# def generate_email(username, domain):
#     return username.lower()+"@"+domain 
# print(generate_email("Dheeraj_shony","gmail.com"))

"""16. Write one function using `print()` and another using `return()` for adding two numbers.Compare the outputs."""
# def add_2nos(a,b):
#     return a+b
# print(add_2nos(5,8))

# def add_2nos(a,b):
#     print(a+b)
# add_2nos(5,8)
    

"""17. Create a function `product_price(price, tax)` using return.
    Store the returned value in a variable and print it."""
# def product_price(price, tax):
#     return price+tax
# res=product_price(100,2) 
# print(res)

"""18. Write a function `greet_user(name)` using print.
    Try storing it in a variable and observe the output."""
# def greet_user(name):
#     print(f"Hi {name} welcome to my home")
# res=greet_user("Priyanka")
# print(res)

"""19. Write a function `calculate_salary(basic, hra, bonus)` that returns gross salary."""
# def calculate_salary(basic, hra, bonus):
#     return basic+hra+bonus
# salary=calculate_salary(40000,5000,2000)
# print(salary)

"""20. Create a function `student_result(mark1, mark2, mark3)` that returns total and average."""
# def student_result(mark1, mark2, mark3):
#     total_mark= mark1+mark2+mark3
#     avg_mark=total_mark/3
#     return total_mark,avg_mark
# res=student_result(89,78,95)
# print(res)

"""21. Write a function `login_status(username)` using print.
    Then convert it to return-based logic."""
# def login_status(username):
#     print(f" user {username} login successful")
# print(login_status("priyanka"))
# def login_status(username):
#     return f" user {username} login successful"
# msg = login_status("priyanka")
# print(msg)

"""22. Create a function `order_summary(item, qty, price)` that prints order details."""
# def order_summary(item, qty, price):
#     total = qty * price
#     print(f"Item: {item}")
#     print(f"Quantity: {qty}")
#     print(f"Price per item: {price}")
#     print(f"Total: {total}")
# order_summary("soap", 5, 50)

"""23. Rewrite the previous question using return so the output can be reused elsewhere."""
# def order_summary(item, qty, price):
#     total = qty * price
#     return f"Item: {item}, Qty: {qty}, Price: {price}, Total: {total}"
# print(order_summary("soap", 5, 50))

"""24. Write a function `employee_details(name, age, department)` using positional arguments."""
# def employee_details(name, age, department):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Department: {department}")
# employee_details("Sanand", 30, "Electronics")

"""25. Call the above function with incorrect order and observe the issue."""
# def employee_details(name, age, department):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Department: {department}")
# employee_details(30, "Sanand", "Electronics")

"""26. Rewrite the previous question using keyword arguments."""
# def employee_details(name, age, department):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Department: {department}")
# employee_details(department="Electronics", name="Sanand", age=30)

"""27. Create a function `create_profile(name, city="Kochi")`.
    Call it with and without city."""
# def create_profile(name, city="Kochi"):
#     print(f"Name: {name}, City: {city}") 
# create_profile("Smitha", "Calicut")
# create_profile("Smitha")

"""28. Write a function `book_ticket(name, seat_type="General", meal="No")`."""
# def book_ticket(name, seat_type="General", meal="No"):
#     return name,seat_type,meal
# print(book_ticket("Dheeraj")) 

"""29. Create a function `send_notification(user, message="Welcome!")`."""
# def send_notification(user, message="Welcome!"):
#     print(f"Notification for {user}: {message}")
# send_notification("Priyanka")

"""30. Write a function `register_student(name, course="Python", duration="3 Months")`."""
# def register_student(name, course="Python", duration="3 Months"):
#     print(f"Registration for {name}-course:{course},duration:{duration}")
# register_student("Dhyan Chand")

"""31. Write a function `calculate_bill(amount, gst=18)`."""
# def calculate_bill(amount, gst=18):
#     gst_amount = (amount * gst) / 100
#     total = amount + gst_amount
#     print(f"Amount: {amount}, GST: {gst_amount}, Total: {total}")
# calculate_bill(1000)

"""32. Create a function `delivery_charge(location, charge=50)`."""
# def delivery_charge(location, charge=50):
#     print(f"Delivery charge to {location}: {charge}")
# delivery_charge("Calicut")

"""33. Write a function `attendance_status(name, status="Present")`."""
# def attendance_status(name, status="Present"):
#     print(f"{name} is {status}")
# attendance_status("Thejas")

"""34. Write a function `sum_all(*numbers)` that returns the sum of all given numbers."""
# def sum_all(*numbers):
#     total=0
#     for num in numbers:
#         total+=num
#     return total
# print(sum_all(45,67,34,23,90))

"""35. Write a function `find_maximum(*numbers)`."""
# def find_maximum(*numbers):
#     return max(numbers) 
# print(find_maximum(45,67,89,98,23,34))

"""36. Write a function `display_subjects(*subjects)` that prints all subject names."""
# def display_subjects(*subjects):
#     for subject in subjects:
#         print(subject)
# display_subjects("English", "Maths", "Science", "Social", "Malayalam")

"""37. Write a function `average_marks(*marks)` that returns the average."""
# def average_marks(*marks):
#     if not marks:
#         return 0
#     avg_marks=sum(marks)/len(marks)
#     return avg_marks
# print(average_marks(45,48,49,43,47))

"""38. Write a function `shopping_total(*prices)` that returns total amount."""
# def shopping_total(*prices):
#     total_amount=sum(prices)
#     return total_amount
# print(shopping_total(100,200,234,256,765))

"""39. Write a function `student_profile(**details)` that prints all key-value pairs."""
# def student_profile(**details):
#     for key, value in details.items():
#         print(key, ":", value)
# student_profile(name="Kiranchand",age=20,course="Python", place="Calicut")

"""40. Write a function `employee_record(**data)` to print employee details."""
# def employee_record(**data):
#     for key,value in data.items():
#         print(key, ":" ,value) 
# employee_record(name="Veena",age=49,job="Teacher",salary=60000)

"""41. Write a function `product_details(**info)` for an ecommerce product."""
# def product_details(**data):
#     for key, value in data.items():
#         print(key, ":", value)
# product_details(product="Laptop",brand="HP",price=55000,stock=12,rating=4.5)

"""42. Write a function `user_settings(**settings)` to simulate app preferences."""
# def user_settings(**settings):
#     print("User App Preferences:")
#     for key, value in settings.items():
#         print(key, ":", value)
# user_settings(theme="Dark",language="English",notifications=True,font_size="Medium")

"""43. Write a function `create_resume(**details)` to print formatted resume data."""
# def create_resume(**details):
#     print("------ RESUME ------")
#     for key, value in details.items():
#         print(key.title(), ":", value)
# create_resume(name="Dhyanchand",age=24,qualification="BCA",skills="Python, SQL",experience="Fresher",location="Calicut")

"""44. Write a function `report_card(name, *marks, **details)`."""
# def report_card(name, *marks, **details):
#     print("----- REPORT CARD -----")
#     print("Name :", name)
#     print("Marks :", marks)
#     print("Total :", sum(marks))
#     print("Average :", sum(marks) / len(marks))
#     print("\nAdditional Details:")
#     for key, value in details.items():
#         print(key, ":", value)
# report_card("Dheeraj",45, 48, 50, 47,grade="A",course="BCA",place="Calicut")

"""45. Write a function `invoice(customer_name, *items, **meta)`."""
# def invoice(customer_name, *items, **meta):
#     print("----- INVOICE -----")
#     print("Customer Name :", customer_name)
#     print("\nItems Purchased:")
#     for item in items:
#         print("*", item)
#     print("\nAdditional Information:")
#     for key, value in meta.items():
#         print(key, ":", value)
# invoice("Bhavyalakshmi","Laptop","Mouse","Keyboard",bill_no=1023,payment="Online",delivery="Express")