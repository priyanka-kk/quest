""" 



43. Create an Employee class inherited by Developer.

44. Create a hospital management system using inheritance.

45. Create a payment gateway system using inheritance.

MULTILEVEL INHERITANCE

46. Create:
   - Animal → Mammal → Dog

47. Create:
   - Company → Department → Employee

48. Create:
   - User → Seller → PremiumSeller

49. Create:
   - Account → SavingsAccount → SalaryAccount

50. Create:
   - Device → Laptop → GamingLaptop"""

""" 41. Create:
   - Parent → Person
   - Child → Student"""

# class Person:
#     def cname(self,name):
#         print(f"The person has a name {name}")

#     def cage (self,age):
#         print(f"The person is {age} years old ")


# class Student(Person):
#     id =101
#     def sid (self):
#         self.mid = self.id
#         self.id+=1  
#         print(self.id) 
#         return self.mid

#     def subject (self):
#         self.sid()
#         print(f"{self.mid} has joined for Python")

# stdnt1 = Student()
# stdnt2 = Student()

# stdnt1.cname('Sooraj')
# stdnt1.cage(14)
# stdnt1.subject()

# stdnt2.cname('manoj')
# stdnt2.cage(15)
# stdnt2.subject()

""" 42. Create:
   - Parent → Vehicle
   - Child → Bike"""

# class Vehicle:
#     def bname(self,brand):
#         print(f"The Vehicle has a brand name {brand}")

#     def bmodel (self,kollam):
#         print(f"The Vehicle is {kollam} model")


# class Bike(Vehicle):
    
#     def reg (self, num):
#         self.num = num


#     def subject (self):
#         print(f"{self.num} is EV")

# stdnt1 = Bike()
# stdnt2 = Bike()

# stdnt1.bname('TVS')
# stdnt1.bmodel(2026)
# stdnt1.reg('KL 11 7933')
# stdnt1.subject()

""" 48. Create:
   - User → Seller → PremiumSeller"""

class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    
class Seller(User):
    def login():
        super(e)
