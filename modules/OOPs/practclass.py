"""............Basic Level..............."""

"""1. Student Class
Create a class named Student.
Add a class attribute school_name = "ABC School"
Create two objects.
Display the school name using both objects."""
# class Student():
#     school_name = "ABC School"
# Dheeraj=Student()  
# Thejas=Student()
# print(Student().school_name)
# print(Student.school_name)
# print(Dheeraj.school_name)
# print(Thejas.school_name)

"""2. Mobile Class
Create a class named Mobile.
Add class attributes:
brand = "Samsung"
country = "Korea"
Create an object and print both attributes."""
# class Mobile():
#     brand = "Samsung"
#     country = "Korea"
# s24_ultra=Mobile()
# print(s24_ultra.brand)
# print(s24_ultra.country)

"""3. Employee Class
Create a class named Employee.
Add a method show_company() that prints:
"Company Name: TechSoft"
Create an object and call the method."""
# class Employee():
#     def show_company(self):
#         print("Company Name: TechSoft")
# Dhanchand = Employee()
# Dhanchand.show_company()

"""4. Car Class
Create a class named Car.
Add class attribute wheels = 4
Create two objects.
Print the number of wheels using both objects."""
# class Car():
#     wheels=4
# Ameo=Car()
# BMW=Car()   
# print(Ameo.wheels)
# print(BMW.wheels)


"""5. College Class
Create a class named College.
Add a class attribute college_name = "Green Valley College"
Add a method display() to print the college name.
Create an object and call the method."""
# class College():
#     college_name = "Green Valley College"
#     def display(self):
#         print("Green Valley College")
# Mercy_college=College()
# Mercy_college.display()

"""..........Intermediate Level..............."""

""" 6. Laptop Class Attribute Updation
Create a class named Laptop.
Add class attribute brand = "Dell"
Print the brand.
Update the class attribute to "HP"
Print the updated value."""
# class Laptop():
#     brand = "Dell"
# Dell_Lattitude5470=Laptop()
# print(Dell_Lattitude5470.brand)
# Laptop.brand="HP"
# print(Dell_Lattitude5470.brand)

"""7. Hospital Class
Create a class named Hospital.
Add class attribute hospital_name = "City Hospital"
Add method show() to display the hospital name.
Create two objects and call the method using both objects"""
# class Hospital():
#     hospital_name = "City Hospital"
#     def show(self):
#         print(self.hospital_name)
# Fathima_hospital=Hospital()
# Mims_hospital=Hospital()
# Fathima_hospital.show()
# Mims_hospital.show()

"""8. Bus Class
Create a class named Bus.
Add class attribute seats = 40
Update the number of seats to 50
Print the updated value."""
# class Bus():
#     seats = 40
# KSRTC=Bus()
# Bus.seats=50
# print(KSRTC.seats)

"""9. Bank Class
Create a class named Bank.
Add class attribute bank_name = "Federal Bank"
Add method display_bank() to print the bank name.
Create an object and call the method."""
# class Bank():
#     bank_name = "Federal Bank"
#     def display_bank(self):
#         print(self.bank_name)
# HDFC=Bank()
# HDFC.display_bank()

"""10. Movie Class
Create a class named Movie.
Add class attribute industry = "Mollywood"
Delete the class attribute.
Try printing the attribute after deletion."""
# class Movvie():
#     industry = "Mollywood"
# del Movvie.industry
# print(Movvie.industry) #AttributeError: type object 'Movvie' has no attribute 'industry'

"""..............Advanced Level............."""

"""11. Book Class
Create a class named Book.
Add class attribute library = "Central Library"
Add methods:
show_library()
update_library()
Update the library name using the method and display the updated value."""
# class Book:
#     library = "Central Library"
#     def show_library(self):
#         print(self.library)
#     def update_library(self, new_name):
#         Book.library = new_name
# book1 = Book()
# book1.show_library()
# book1.update_library("District Library")
# book1.show_library()

"""12. School Class Attribute Deletion
Create a class named School.
Add class attribute principal = "Ramesh"
Print the attribute.
Delete the attribute.
Handle the error if the attribute is accessed after deletion"""
# class School():
#     principal = "Ramesh"
# SMES = School()
# print(SMES.principal)
# del School.principal
# try:
#     print(SMES.principal)
# except AttributeError:
#     print("Attribute has been deleted")

"""13. TV Class
Create a class named TV.
Add class attribute company = "Sony"
Create three objects.
Update the class attribute to "LG"
Show that the updated value is reflected in all objects."""
# class TV():
#     company = "Sony"
# TCL=TV()
# VU=TV()
# Samsung=TV()
# TV.company="LG"
# print(TCL.company)
# print(VU.company)
# print(Samsung.company)

"""14. University Class
Create a class named University.
Add class attribute country = "India"
Add method show_country()
Create multiple objects and call the method."""
# class University():
#     country = "India"
#     def show_country(self):
#         print(self.country)
# Kannur=University()
# calicut=University()
# Cusat=University()
# Kannur.show_country()
# calicut.show_country()
# Cusat.show_country()

"""15. Restaurant Class
Create a class named Restaurant.
Add class attribute type = "Veg"
Update the attribute to "Multi Cuisine"
Delete the attribute.
Print suitable messages after each operation."""
# class Restaurant():
#     type = "Veg"
# print("Original Type:", Restaurant.type)
# Restaurant.type = "Multi Cuisine"
# print("Updated Type:", Restaurant.type)
# del Restaurant.type
# print("Attribute deleted")

"""...........Challenge Questions..............."""

"""16. Company Management
Create a class named Company.
Add class attribute company_name = "Infosys"
Add methods to:
Display company name
Update company name
Delete company name. """
# class Company:
#     company_name = "Infosys"

#     def display_companyname(self):
#         print("Company Name:", Company.company_name)

#     def update_companyname(self, new_name):
#         Company.company_name = new_name

#     def delete_companyname(self):
#         del Company.company_name


# oracle = Company()

# Display
# oracle.display_companyname()

# Update
# oracle.update_companyname("TCS")
# oracle.display_companyname()

# Delete
# oracle.delete_companyname()


"""17. Cricket Team
Create a class named CricketTeam.
Add class attribute team_name = "India"
Create multiple objects.
Change the team name to "Kerala"
Display the updated value using all objects."""
# class CricketTeam:
#     team_name = "India"
# Pakistan=CricketTeam()
# Srilanka=CricketTeam()
# Australia=CricketTeam()
# CricketTeam.team_name = "Kerala"
# print(Pakistan.team_name)
# print(Srilanka.team_name)
# print(Australia.team_name)


"""18. ATM Machine
Create a class named ATM.
Add class attribute bank = "SBI"
Add method show_bank()
Delete the class attribute and check the output."""
# class ATM:
#     bank = "SBI"
#     def show_bank(self):
#         print(self.bank)
# atm=ATM()
# atm.show_bank()
# del ATM.bank
# atm.show_bank() #AttributeError: 'ATM' object has no attribute 'bank'
#..........or
# class ATM:
#     bank = "SBI"

#     def show_bank(self):
#         if hasattr(self, "bank"):
#             print(self.bank)
#         else:
#             print("Bank attribute not found")

# atm = ATM()
# atm.show_bank()
# del ATM.bank
# atm.show_bank()

"""19. Airline Class
Create a class named Airline.
Add class attribute airline_name = "Air India"
Add methods to display and update the airline name.
Create two objects and test the methods.""" 
# class Airline:
#     airline_name = "Air India"
#     def display_airline_name(self):
#         print("Air line Name:",Airline.airline_name)
#     def update_airline_name(self,new_name):
#         Airline.airline_name=new_name

# quaterairways=Airline()
# emirates=Airline()
# quaterairways.display_airline_name()
# quaterairways.update_airline_name("IndiGo")
# emirates.display_airline_name()
# emirates.update_airline_name("IndiGo")


"""20. Shopping Mall
Create a class named Mall.
Add class attribute mall_name = "Lulu Mall"
Create objects.
Update and delete the class attribute.
Display outputs before and after each operatio. """

class Mall:
    mall_name = "Lulu Mall"

# Create objects
hilite = Mall()
gokulam = Mall()

# Before update
print("Before update:", Mall.mall_name)

# Update class attribute
Mall.mall_name = "Blue Diamond Mall"
print("After update:", Mall.mall_name)

# Delete class attribute
del Mall.mall_name

# After delete
if hasattr(Mall, "mall_name"):
    print(Mall.mall_name)
else:
    print("mall_name attribute deleted")

