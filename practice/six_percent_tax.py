print("Sales Tax Calculator")
print()

def tax(n):
    return n * .06

def ask_cont():
    return input("Again? (y/n): ").lower().strip()

def ask_cost():
    return float(input(f"Cost of item: "))

def main():
    print("ENTER ITEMS (ENTER 0 TO END)")
    cont = "y"
    while cont == "y":
        total_cost = 0.0
        while True:
            cost = ask_cost()
            if cost > 0:
                total_cost += cost
            else:
                print(f"Total:  ${total_cost:.2f}")
                print(f"Sales tax: ${tax(total_cost):.2f}")
                tax_cost = tax(total_cost) + total_cost
                print(f"Total after tax: ${tax_cost:.2f}")
                break
        cont = ask_cont()
    print("Thanks, bye!")

if __name__ == "__main__":
    main()
