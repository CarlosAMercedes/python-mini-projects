import random

print("Dice Roller")
print()

def roll():
    return (random.randint(1,6)), (random.randint(1,6))

def ask_cont():
    print()
    return input ("Roll again? (y/n): ").lower().strip()

def main():
    cont = "y"
    while cont == "y":
        a, b = roll()
        print(f"Die 1:\t{a}")
        print(f"Die 2:\t{b}")
        total = a + b
        print(f"Total:\t{total}")
        if total == 2:
            print("Snake eyes!")
        elif total == 12:
            print("Boxcars!")
        cont = ask_cont()
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()

