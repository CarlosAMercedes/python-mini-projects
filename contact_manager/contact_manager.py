contacts = [["Guido van Rossum", "guido@gmail.com", "+1 609 333 4444"],["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]

def menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()

def list_contact(contacts):
    if not contacts:
        print("No contacts.")
        print()
        return
    else:
        for i, con in enumerate(contacts, start=1):
            print(f"{i}. {con[0]}")
    print()

def view_contact(contacts):
    if not contacts:
        print("No contacts.")
        print()
        return
    num = input("Number:\t\t")
    idx=int(num) - 1
    name, email, phone = contacts[idx]
    print(f"Name:\t\t{name}")
    print(f"Email:\t\t{email}")
    print(f"Phone:\t\t{phone}")
    print()

def add_contact(contacts):
    name = input("Name:\t\t")
    email = input("Email:\t\t")
    phone = input("Phone:\t\t")
    contacts.append([name, email, phone])
    print(f"{name} was added.")
    print()

def del_contact(contacts):
    if not contacts:
        print("No contacts.")
        print()
        return
    num = int(input("Number:\t\t"))
    idx = int(num) -1
    remove = contacts.pop(idx)
    print(f"{remove[0]} was deleted.")
    print()

def command(contacts):
    while True:
        cmd = input("Command:\t")
        if cmd.strip().lower() == "list":
            list_contact(contacts)
        elif cmd.strip().lower() == "view":
            view_contact(contacts)
        elif cmd.strip().lower() == "add":
            add_contact(contacts)
        elif cmd.strip().lower() == "del":
            del_contact(contacts)
        else:
            print("Bye!")
            break

def main():
    print("Contact Manager\n")
    menu()
    command(contacts)

if __name__ == "__main__":
    main()
