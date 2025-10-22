users = {}

def menu():
    print("LOGIN SYSTEM")
    print("-------------")
    print("1. Register")
    print("2. Log in")
    print("3. Exit")
    print()

def display_menu():
    x = 0
    while x != 3:
        menu()
        try:
            x = int(input("Select Menu Option (1, 2, 3):\t"))
            print()
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        print()
        if x == 1:
            username = input("Enter Username:\t")
            password = input("Enter Password:\t")
            if username in users:
                print("\nUsername already taken.\n")
            else:
                users[username] = password
                print(f"User {username} registered successfully.\n")
        elif x == 2:
            u = input("Enter Username:\t")
            p = input("Enter Password:\t")
            if u in users and users[u] == p:
                print("\nLogin successful.\n")
            else:
                print("\nInvalid username or password.\n")
        else:
            break

def main():
    display_menu()

if __name__ == "__main__":
    main()