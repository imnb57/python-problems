
price = int(input("Enter the price of the item: "))
if price > 1000:
    price = price - price * 0.1
elif price > 500:
    price = price - price * 0.05
print("Final price: ", price)