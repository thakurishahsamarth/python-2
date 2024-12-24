price = int(input("Enter the price of an item: "))
if price > 1000:
    discount =( price * 10)/100
    final_price = price - discount
    print(f"Your final price is {final_price}")
elif price > 500:
    discount = (price * 5)/100
    final_price = price - discount
    print(f"Your final price is {final_price}")
else:
    print("No discount available")

