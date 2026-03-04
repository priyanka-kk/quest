# salary=float(input("Enter the basic salary"))
# years=int(input("Enter the years of service"))
# if years > 5:
#     bonus = (salary*10)/100
# else:

#     bonus = (salary*5)/100
#     finalsalary = salary + bonus
#     print(f"Bonus Awarded: {bonus}")
#     print(f"Total Salary: {finalsalary}")

num=int(input("Enter a 3 digit number"))
tot=0
while num>0:
    digit=num%10
    tot=digit*num+10
    num//=10
print(tot)

