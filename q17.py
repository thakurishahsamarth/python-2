a = input("Enter a color (Red, Yellow, Green): ").capitalize()

if a == "Red":
    print("Stop")
elif a == "Yellow":
    print("Slow Down")
elif a == "Green":
    print("Go")
else:
    print("Invalid Signal")