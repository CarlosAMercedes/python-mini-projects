def get_integer():
    while True:
        n = int(input("Please enter an integer between 1 and 5000:\t"))
        if 1 < n <= 5000:
            return n
        else:
            print("Invalid integer. Please try again.")

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def main():
    print("Prime Number Checker\n")
    while True:
        n = get_integer()
        factors = get_factors(n)

        if len(factors) == 2:
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is NOT a prime number.")
            print(f"It has {len(factors)} factors.")

        cont = input("Try again? (y/n): ").strip().lower()
        if cont != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
