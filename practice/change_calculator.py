print("Change Calculator")
print()
#If cent is 0-99, run loop. Else rerun prompt
while True:
    cent = int(input("Enter number of cents (0-99):\t"))
    if cent < 0 or cent > 99:
        print()
        print("Invalid amount, please enter an amount between 0 and 99.")
        print()
        continue
#If cent is 0-99, then calculations using cent will be executed
    else:
        qt = cent//25
        centq = cent - (qt * 25)
        dt = centq//10
        centd = centq - (dt * 10)
        nt = centd//5
        centn = centd - (nt * 5)
        pt = centn//1
#Print values
        print(f"Quarters: {qt}")
        print(f"Dimes: {dt}")
        print(f"Nickles: {nt}")
        print(f"Pennies: {pt}")
        print()
#Ask user to continue. If no, print bye and close
    cont = input("Continue? (y/n):")
    if cont.lower().strip() == "y":
        pass
    else:
        break

print("Bye!")
