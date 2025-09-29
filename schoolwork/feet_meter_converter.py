def welcome():
    print("Feet and Meters Converter")
    print()

welcome()

def f2m(n): #Convert feet to meters
    feet = n * 0.3048
    return feet

def m2f(n): #Convert meters to feet
    meters = n / 0.3048
    return meters

def ask_cont():
    return input("Would you like to perform another conversion? (y/n):").lower().strip()

def main():
    cont = "y"
    while cont.lower().strip() == "y":
        print("Conversions Menu:")
        ab = input("a. Feet to Meters\nb. Meters to Feet\nSelect a conversion (a/b): ").lower().strip()
        if ab == "a":
            num = float(input("Enter feet: "))
            print(f"{f2m(num):.2f} meters")
        elif ab == "b":
            num = float(input("Enter meters: "))
            print(f"{m2f(num):.2f} feet")
        else:
            print("Invalid input.")

        cont = ask_cont()

    print("Thanks, bye!")

if __name__ == "__main__":
    main()

        


