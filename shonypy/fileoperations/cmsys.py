d = {}

def validation(f, data):
    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty")
        return

    if name in data:
        print("Name already exists")
        return

    phno1 = input("Enter phone number (+91xxxxxxxxxx): ")

    if phno1 in data:
        print("Phone number already exists")
        return

    if not (phno1.startswith("+91") and len(phno1) == 13):
        print("Invalid phone number")
        return
    
    phone2 = ""

    phno2 = input("Add more phone? 1-Yes / 0-No: ")

    if phno2 == "1":
        phone2 = input("Enter phone number: ")

        if phone2 in data:
            print("Phone number already exists")
            return

        if not (phone2.startswith("+91") and len(phone2) == 13):
            print("Invalid phone number")
            return


    email1 = input("Enter email: ")

    if email1 in data:
        print("Email already exists")
        return

    if not email1.endswith("@gmail.com"):
        print("Invalid email")
        return
    
    email3 = ""

    email2 = input("Add more email? 1-Yes / 0-No: ")

    if email2 == "1":
        email3 = input("Enter email: ")

        if email3 in data:
            print("Email already exists")
            return

        if not email3.endswith("@gmail.com"):
            print("Invalid email")
            return


    d["Name"] = name

    d["Phones"] = [phno1]
    if phone2:
        d["Phones"].append(phone2)

    d["Emails"] = [email1]
    if email3:
        d["Emails"].append(email3)

    f.writelines(str(d) + "\n")

    print("Record added successfully")
    print(d)

def menudetails():
    print("<---------------- Menu ------------------->")
    print("1. List all records")
    print("2. Add Record")
    print("3. Edit Record")
    print("4. Delete Record")
    print("5. Exit")

menudetails()

ec = input("Enter your choice : ")

if ec=="1":
    print(".........List all Records.........")
    with open("record.txt", "a+") as f:
        f.seek(0)
        data = f.read()
        print(data)

if ec == "2":
    print("........Add Record..........")
    with open("record.txt", "a+") as f:
        f.seek(0)
        data = f.read()
        validation(f, data)

def menu2_details():
    print("1. Edit Name")
    print("2. Add Phone")
    print("3. Add Email")
    print("4. Edit Phone")
    print("5. Edit Email")
    print("0. Back")

if ec == "3":
    print("..........Edit Record...........")

    with open("record.txt", "r") as f:
        
        found = False

        ne = input("Enter the name to edit: ")
        import ast
        for line in f:
            record = ast.literal_eval(line.strip())

            if record['Name'].lower() == ne.lower():
                found = True
                break

        if found:
            print("Record found")
            menu2_details()
        else:
            print("Record not found")

if ec=="4":
    print("..........Delete Record..........")

if ec=="5":
    print("Exiting......Thank You")