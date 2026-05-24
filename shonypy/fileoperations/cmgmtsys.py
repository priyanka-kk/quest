d = {}
def menudetails():
    print("<---------------- Menu ------------------->")
    print("1. List all records")
    print("2. Add Record")
    print("3. Edit Record")
    print("4. Delete Record")
    print("5. Exit")

menudetails()

ec = int(input("Enter your choice : "))
with open("record.txt",'a+') as f:
    data=f.read()
    f.seek(0)


    if ec == 2:
        name = input("Enter name: ").strip()
        if name == "":
            print("Name cannot be empty")
        elif name in data:
         print("Name already exists")
        else:
            d.update({"Name": name})

    phno1 = input("Enter phone number (+91xxxxxxxxxx):")

    if phno1.startswith("+91") and len(phno1) == 13 and phno1 not in d.values():
        d.update({"Phone": phno1})
    else:
        print("Invalid phone number")

    phno2 = input("Add more phone numbers? 1-Yes / 0-No: ")

    phone2 = input("Enter second phone number: ")

    if phone2.startswith("+91") and len(phone2) == 13 and phone2 not in d.values():
        d.update({"Phone2": phone2})
    else:
        print("Invalid second phone number")

    email1 = input("Enter email id: ")

    if email1.endswith("@gmail.com") and email1 not in d.values():
        d.update({"Email": email1})
    else:
        print("Invalid email")

    email2 = input("Add more email? 1-Yes / 0-No: ")

    if email2 == "1":
        email2 = input("Enter second email: ")
        if email2.endswith("@gmail.com") and email2 not in d.values():
            d.update({"Email2": email2})
        else:
            print("invalid second email")
    f.write(str(d) + "\n")

    print("Record added successfully")
    print(d)




 


