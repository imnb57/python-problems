costprice = float(input("Enter the cost price of the bike: "))

if costprice > 100000:
    tax = costprice * 0.15
elif costprice > 50000 and costprice <= 100000:
    tax = costprice * 0.10
else:
    tax = costprice * 0.05

print("The road tax to be paid is:", tax, "Rs")
