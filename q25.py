age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
show_type = input("Enter the show type (Matinee/Evening): ").capitalize()

if age < 12:
    if show_type == "Matinee":
         ticket_price = 500
    else:
        ticket_price = 700
elif age >= 12 and age < 60:
    if gender == 'M':
        if show_type == "Matinee":
            ticket_price = 800
        else: 
            ticket_price = 1000
    elif gender == 'F':
        if show_type == "Matinee":
            ticket_price = 700 
        else:
            ticket_price = 900
elif age >= 60:
    ticket_price = 600
else:
    ticket_price = 0

print(f"The ticket price is: Rs{ticket_price}")

