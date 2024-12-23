
price = int(input("Enter the price of the item: "))
if price > 1000:
    print(price - (price * 0.2))
elif price >= 500 and price <= 1000:
    print(price - (price * 0.1))
else:
    print(price)

