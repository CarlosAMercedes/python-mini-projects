print("Even or Odd Checker")
print()

def even_check(n):
        if n%2 == 0:
            return "Even"
        else:
            return "Odd"

def main():
    cont = "y"

    while cont.lower().strip() == "y":
        num = int(input("Enter an integer: "))
        print()
        print(f"{num} is {even_check(num)}")

        cont = input("Would you like to check more numbers? (y/n)")
    else:
        print("Bye!")

if __name__ == "__main__":
    main()
    #cont = input("Would you like to check more numbers? (y/n)")
    #if cont.lower().strip() == "y":
     #   pass
    #else:
     #   break