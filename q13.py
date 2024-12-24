print("Welcome to the Wizarding World")

choice1 = input("Do you want to study 'spells' or 'potions'? ").lower()

if choice1 == "spells":
    choice2 = input("Do you want to 'practice magic' or 'compete in duels'? ").lower()
    
    if choice2 == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif choice2 == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice. Game Over.")

elif choice1 == "potions":
    choice3 = input("Do you want to 'brew an elixir' or 'create poison'? ").lower()
    
    if choice3 == "brew an elixir":
        print("You healed a village. You Win!")
    elif choice3 == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice. Game Over.")

else:
    print("Invalid choice. Game Over.")
