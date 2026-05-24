# class Student:
#     pass

# richu=Student()
# print(type(richu))
# print(id(richu))

# yaseen=Student()
# print(id(yaseen))

# class Student:
#     def exam(self):
#         print(("exam conducted on 8/5/2026"))
# richu=Student()
# yaseen=Student()
# richu.exam()
# yaseen.exam()

# class Student:
#     school_name="Quest Innovative solutions"

# richu=Student()
# yaseen=Student()    
# print(Student().school_name)
# print(Student.school_name)
# print(richu.school_name)
# print(yaseen.school_name)
# Student.school_name= "QIS"
# print(richu.school_name)
# print(yaseen.school_name)
# Student.school_name="XAVIO"
# del richu.school_name
# print(richu.school_name)
# del Student.school_name
# print(yaseen.school_name)

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
# s1 = Student("John",22)
# print(s1.name,s1.age)

# class Student:
#     school_name="QIS"
#     course="Python Full Stack"
#     def __init__(self,sid,name,age,email):
#         print("Constructor created.....")
#         self.student_id=sid
#         self.s_name=name
#         self.age=age
#         self.email=email
#     def get_details(self):
#         print(f"student id:{self.student_id}\nstudent name:{self.s_name}\nage :{self.age}\nemail:{self.email}")
# shahal=Student(255,"Shahal",22,"shahal.co.in")
# shahal.get_details()
# niyas=Student(265,"Niyas",23,"niyas.co.in")
# niyas.get_details()

"""Employee details"""
# class Employee:
#     company_name="QIS"
#     branch_name="calicut"
#     def __init__(self,id,name,email,salary):
#         self.empid=id
#         self.empname=name
#         self.emp_email=email
#         self.emp_salary=salary
#         print("constructor created.........")
#     def get_details(self):
#         print(f"emp id :{self.empid}")
#         print(f"emp name :{self.empname}")
#         print(f"emp email :{self.emp_email}")
#         print(f"emp salary :{self.emp_salary}")

#     # if salary<100000 increment 5%
    
#     def update_salary(self):
#         if self.emp_salary < 100000:
#             increment = self.emp_salary * 0.05
#             self.emp_salary = self.emp_salary + increment
#             print("increment if salary<100000")
#         print(f"updated salary = {self.emp_salary}")

#     #if the person resigned in the company
#     def resign_company(self):
#         self.company_name="TCS"
#         self.branch_name="Trivandrum"
#         self.empid=2345
#         self.empname="Dhyanchand"
#         self.emp_email="Dhyanchand@tcs.com"
#         self.emp_salary=80000
#         print("if the person resigned in the company")
#         print(f"emp id :{self.empid}")
#         print(f"emp name :{self.empname}")
#         print(f"emp email :{self.emp_email}")
#         print(f"emp salary :{self.emp_salary}")

# Dhyanchand=Employee(234,"Dhyanchand","Dhyanchand@gmail.com",35000)
# Dhyanchand.get_details()
# Dhyanchand.update_salary()
# Dhyanchand.resign_company()

"""Bank details of a person"""
# class Bank:
#     bank_name = "ICICI Bank"

#     def __init__(self, name, balance, ifsc, acno):
#         self.account_no = acno
#         self.account_name = name
#         self.ifsc_code = ifsc
#         self.acc_balance = balance

#     def get_details(self):
#         print(f"account_no: {self.account_no}")
#         print(f"account_name: {self.account_name}")
#         print(f"ifsc_code: {self.ifsc_code}")
#         print(f"account_balance: {self.acc_balance}")

#     def balance(self):
#         print(f"Current balance: {self.acc_balance}")

#     def withdraw(self, amt):
#         if amt > self.acc_balance:
#             print("Insufficient balance")
#         else:
#             self.acc_balance -= amt
#             print(f"Balance after withdrawal: {self.acc_balance}")

#     def deposit(self, amt):
#         self.acc_balance += amt
#         print(f"New balance: {self.acc_balance}")


# shony_ac = Bank("shony", 1010, "icici0001", 5000)

# shony_ac.get_details()

# shony_ac.withdraw(200)

# shony_ac.deposit(500)

# shony_ac.balance()
          
"""................single inheritance....................."""
# class Animal:
#     def eat(self):
#         print("eating........")
#     def sleep(self):
#         print("sleeping....")
# class Dog(Animal):
#     def run(self):
#         print("running..........")
# arjun=Dog()
# arjun.eat()
# arjun.sleep()
# arjun.run()

"""starting"""
# class Person:
#     def __init__(self,name,age):
#         print("calling parent constructor.....")
#         self.name=name
#         self.age=age

#     def get_details(self):
#         print(f"name:{self.name}\nage:{self.age}")
    
#     def test(self):
#         print("testing parent methods")


# class Student(Person):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         print("calling child constructor")

#     def test(self):
#         super().test()
#         print("testing child method")


# richu = Student("Richu",22)
# jasil = Student("Jasil",23)

# richu.get_details()
# richu.test()
# jasil.get_details()
# jasil.test()
"""ending"""


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Developer(Person):
#     def __init__(self, name, age,salary,language):
#         super().__init__(name, age)
#         self.salary=salary
#         self.language=language

#     def get_details(self):
#         print(f"name :{self.name}\nage :{self.age}\nsalary :{self.salary}\nlanguage :{self.language}")
# najad=Developer("Najad",25,25000,"Python")
# najad.get_details()


""".........................Multilevel Inheritance................"""
# class Vehicle:
#     def start(self):
#         print("vehicle can start")

# class Car(Vehicle):
#     def horn(self):
#         print("horn")


"""Multiple Inheritance"""
# class SportsPerson:
#     team='Barcelona'
#     def action(self):
#         print(" plays Football ")
# class Musician:
#     brand="thaikudam"
#     def action(self):
#         print("plays guitar")
# class student(SportsPerson,Musician):
#     def study(self):
#         print 

# class Vehicle:
#     def fuel_type(self):
#         print("Vehicle uses some fulel types ")

# #level1
# class Car(Vehicle):
#     def wheels(self):
#         print("car has 4 wheels")

# class Motorcycle(Vehicle):
#     def wheels(self):
#         print("Motorcycle has 2 wheels ")

# #level2(Hybrid)
# class electriccar(Car):
#     def battery(self):
 

"""build a food delivery app using multiple inheritance"""
class user:
    def __init__(self,name,location):
        self.name=name
        self.location=location 
        def user_login(self):  
            print(f"name :{self.name}\nlocation :{self.location}")
    def __init__(self,shop_name):
        self.shop_name=shop_name 
        def order(self):
            print(f"name :{self.name}\nlocation :{self.location}")
        def __init__(self, name,location,item_name):
            self.name=name
            self.location=location
            self.item_name=item_name
        def delivery(self):
            pass                                                                                

                                                                    

"""....inner class..."""
# class Electronics:
#     def collections(self):
#         print("collection of eectronic items")
#         class Laptop:
#             def brand(self):
#                 print("HP")

# e=Electronics()
# laptop=Electronics.Laptop()
# laptop.brand()

# from practclass import Book


# studen = Book()
# Book.show_library()
         


"""...............Polymorphism................."""

# class student:
#     def __init__(self):
#         pass
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
# # thejas=student()
# # print(thejas)
# dheeraj=student("Dheeraj",14)
# print(dheeraj.name)
# print(dheeraj.age)


# class vehicle:
#     def start(self):
#         print("vehicle is starting")

# class Bike(vehicle):
#     def start(self):
#         super().start()
#         print("self start")

# b=Bike()
# print(b.start())
 
    

