print("*************CONTACT MANAGEMENT SYSTEM***************")
d = {}

#validation
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

    d={}
    d["Name"] = name

    d["Phones"] = [phno1]
    if phone2:
        d["Phones"].append(phone2)

    d["Emails"] = [email1]
    if email3:
        d["Emails"].append(email3)

    f.write(str(d) + "\n")

    print("Record added successfully")
    print(d)

def menudetails():
    
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

    import ast

    with open("record.txt", "r") as f:

        records = []

        for line in f:
            line = line.strip()

            if line != "":
                records.append(ast.literal_eval(line))

    ne = input("Enter the name to edit: ")

    found = False

    for record in records:

        if record['Name'].lower() == ne.lower():

            found = True

            print("Record found")

            menu2_details()

            ec1 = input("Enter your choice: ")

            # Edit Name
            if ec1 == "1":

                new_name = input("Enter new name: ").strip()

                if new_name == "":
                    print("Name cannot be empty")

                else:
                    record["Name"] = new_name
                    print("Name updated successfully")

            # Add Phone
            elif ec1 == "2":

                if len(record["Phones"]) >= 2:
                    print("Maximum 2 phone numbers allowed")

                else:
                    new_phone = input("Enter new phone number: ")

                    if not (new_phone.startswith("+91") and len(new_phone) == 13):
                        print("Invalid phone number")

                    else:
                        record["Phones"].append(new_phone)
                        print("Phone added successfully")

            # Add Email
            elif ec1 == "3":

                if len(record["Emails"]) >= 2:
                    print("Maximum 2 emails allowed")

                else:
                    new_email = input("Enter new email: ")

                    if not new_email.endswith("@gmail.com"):
                        print("Invalid email")

                    else:
                        record["Emails"].append(new_email)
                        print("Email added successfully")

            # Edit Phone
            elif ec1 == "4":

                print(record["Phones"])

                pchoice = int(input("Enter phone index to edit (1/2): "))

                if 1 <= pchoice <= len(record["Phones"]):

                    new_phone = input("Enter new phone number: ")

                    if not (new_phone.startswith("+91") and len(new_phone) == 13):
                        print("Invalid phone number")

                    else:
                        record["Phones"][pchoice - 1] = new_phone
                        print("Phone updated successfully")

                else:
                    print("Invalid choice")

            # Edit Email
            elif ec1 == "5":

                print(record["Emails"])

                echoice = int(input("Enter email index to edit (1/2): "))

                if 1 <= echoice <= len(record["Emails"]):

                    new_email = input("Enter new email: ")

                    if not new_email.endswith("@gmail.com"):
                        print("Invalid email")

                    else:
                        record["Emails"][echoice - 1] = new_email
                        print("Email updated successfully")

                else:
                    print("Invalid choice")

            elif ec1 == "0":
                print("Back")

            else:
                print("Invalid menu choice")

            break

    if not found:
        print("Record not found")

    with open("record.txt", "w") as f:

        for record in records:
            f.write(str(record) + "\n")

def menu3_details():
    print("1. Delete Entire Record")
    print("2. Delete Phone")
    print("3. Delete Email")
    print("0. Exit")


if ec == "4":
    print("..........Delete Record..........")
   

    import ast

    with open("record.txt", "r") as f:
        records = []

        for line in f:
            line=line.strip()
            if line!="":
                records.append(ast.literal_eval(line.strip()))

    nd = input("Enter the name to delete: ")

    found = False

    for record in records:

        if record['Name'].lower() == nd.lower():

            found = True

            print("Record found")
            menu3_details()

            ec1 = input("Enter your choice: ")

            if ec1 == "0":
                print("Exit")

            elif ec1 == "1":

                records.remove(record)

                print("Entire record deleted successfully")

            elif ec1 == "2":

                print(record["Phones"])

                pchoice = int(input("Enter phone index to delete (1/2): "))

                if 1 <= pchoice <= len(record["Phones"]):

                    deleted = record["Phones"].pop(pchoice - 1)

                    print(deleted, "deleted successfully")

                else:
                    print("Invalid choice")

            elif ec1 == "3":

                print(record["Emails"])

                echoice = int(input("Enter email index to delete (1/2): "))

                if 1 <= echoice <= len(record["Emails"]):

                    deleted = record["Emails"].pop(echoice - 1)

                    print(deleted, "deleted successfully")

                else:
                    print("Invalid choice")

            else:
                print("Invalid menu choice")

            break

    if not found:
        print("Record not found")

    with open("record.txt", "w") as f:

        for record in records:
            f.write(str(record) + "\n")


if ec=="5":
    print("Exiting......Thank You")