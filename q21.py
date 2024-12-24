a = float(input("Enter the price of the item: "))

if a > 1000:
    discount = a - (a * 0.2)
    print("Discounted price:", discount)
elif 500 <= a <= 1000:
    discount = a - (a * 0.1)
    print("Discounted price:", discount)
else:
    print("No discount. Price remains:", a)
