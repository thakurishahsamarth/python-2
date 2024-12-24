a = float(input("Enter your BMI: "))

if a < 18.5:
    print("Underweight")
elif 18.5 <= a < 24.9:
    print("Normal weight")
elif 25 <= a < 29.9:
    print("Overweight")
else:
    print("Obesity")