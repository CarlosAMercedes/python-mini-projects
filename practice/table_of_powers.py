print("Table of Powers")
print()
while True:
    start = int(input("Start number: "))
    stop = int(input("Stop number: "))
    if start > stop:
        print("Stop integer must be less than the start integer. Try again.")
        continue
    else:
        print()
        print("Number\t\t Squared\t Cubed")
        print("="*6,"\t\t","="*7, "\t", "="*5)
    for i in range(start, stop+1):
        sq = i ** 2
        cu = i ** 3
        print(i, "\t\t", sq, "\t\t", cu)
    cont = input("Continue? (y/n)")
    if cont.lower().strip() == "y":
        pass
    else:
        break
print("Goodbye")
