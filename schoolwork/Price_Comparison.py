#Program that compares the unit prices for two sizes of detergent.
print("Price Comparison")
print()
#Receive user input
price_64 = round(float(input("Price of 64 oz size:\t")), 2)
price_32 = round(float(input("Price of 32 oz size: \t")), 2)
print()
#Initialize variables
oz_64 = round(price_64 / 64, 2)
oz_32 = round(price_32 / 32, 2)
#Return values
print("Price per oz (64):\t", oz_64)
print("Price per oz (32):\t", oz_32)
