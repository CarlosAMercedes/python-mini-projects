print("="*50)
print("Shipping Calculator")
print("="*50)

while True:
    cost = float(input("Cost of items ordered:\t"))
    if cost < 0.00:
        print("You must enter a positive number. Please try again.")
        continue
    elif cost < 30.00 and cost > 0.00:
        sc = 5.95
    elif cost >= 30.00 and cost <= 49.99:
        sc = 7.95
    elif cost >= 50.00 and cost <= 74.99:
        sc = 7.95
    else:
        sc = "FREE"

    if sc == "FREE":
        print(f"Shipping cost: \t {sc:.2f}")
        print(f"Total cost: \t ${cost}")
    else:
        tc = cost + sc 
        print(f"Shipping cost: \t {sc:.2f}")
        print(f"Total cost: \t {tc:.2f}")
        print()
    cont = input("Continue? (y/n): ")
    print("=" * 50)
    if cont.lower().strip() == "y":
        pass
    else:
        break
print("Bye!")
