age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
membership_type = input("Enter the membership type (Monthly/Yearly): ").capitalize()
if age>=18 and age<30:
    if gender=='M':
        if membership_type=='Monthly':
            cost=50
        else:
            cost=500
    else:
        if membership_type=='Monthly':
            cost=45
        else:
            cost=450
elif age>=30 and age<=50:
    if membership_type=='Monthly':
        cost=60
    else:
        cost=600
else:
    if membership_type=='Monthly':
        cost=40
    else:
        cost=400
print(f"Your cost is {cost}")