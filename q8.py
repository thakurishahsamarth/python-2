print("Welcome to the Jungle Survival Challenge")
action = input("What do you want to do: 'search for food' or 'build a shelter'? ")
if action == "search for food":
    choice = input("Do you want to 'hunt' or 'gather'? ").lower()
    if choice == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice. Game Over.")
elif action == "build a shelter":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    print("Invalid action. Game Over.")
