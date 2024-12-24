preference = input("Do you prefer vegetarian or non-vegetarian? (Enter 'vegetarian' or 'non-vegetarian'): ").strip().lower()
if preference == "vegetarian":
    choice = input("Do you want 'Salad' or 'Pasta'? (Enter 'Salad' or 'Pasta'): ").strip().capitalize()
    if choice == "Salad":
        print("You chose Salad.")
    elif choice == "Pasta":
        print("You chose Pasta.")
    else:
        print("Invalid choice. Please choose either 'Salad' or 'Pasta'.")
elif preference == "non-vegetarian":
    choice = input("Do you want 'Chicken' or 'Fish'? (Enter 'Chicken' or 'Fish'): ").strip().capitalize()
    if choice == "Chicken":
        print("You chose Chicken.")
    elif choice == "Fish":
        print("You chose Fish.")
    else:
        print("Invalid choice. Please choose either 'Chicken' or 'Fish'.")
else:
    print("Invalid preference. Please choose 'vegetarian' or 'non-vegetarian'.")


