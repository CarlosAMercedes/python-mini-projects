#Program that calculates the tip and total for a meal at a restaurant
print("Tip Calculator")
print()
cost = float(input("Cost of meal:\t"))
percent = float(input("Tip percent:\t"))
print()
tip = cost * (percent / 100)
print("Tip amount:\t", tip)
total = cost + tip
print("Total amount:\t", total)