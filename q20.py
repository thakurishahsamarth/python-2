a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a % 2 == 0 and b % 2 == 0:
    print("Sum:", a + b)
elif (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
    print("Difference:", abs(a - b))
else:
    print("Product:", a * b)