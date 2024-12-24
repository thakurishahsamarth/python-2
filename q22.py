age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
income = float(input("Enter your annual income: "))

if age >= 18 and age < 60:
    if gender == 'M':
        if income > 1000000:
            tax = income * 0.3
        elif income >= 500000:
            tax = income * 0.2
        else:
            tax = income * 0.1
    elif gender == 'F':
        if income > 1000000:
            tax = income * 0.25
        elif income >= 500000:
            tax = income * 0.15
        else:
            tax = income * 0.05
elif age >= 60:
    if income > 1000000:
        tax = income * 0.2
    else:
        tax = income * 0.1
else:
    tax = 0

print(f"Your calculated tax is: Rs{tax:.2f}")