print("The Wizard Inventory program")
print()

inventory = ["wooden staff","wizard hat","cloth shoes"]

def menu_prompt():
    print("show - Show all items\ngrab - Grab an item\n" \
    "edit - Edit an item\ndrop - Drop an item\nexit - Exit program")
    print()

def menu_funct():
    cont = "y"
    while cont == "y":
        print()
        cmd = input("Command:\t")
        if cmd.strip().lower() == "show":
            for idx, inv in enumerate(inventory, start =1):
                print(f"{idx}. {inv}")
        elif cmd.strip().lower() == "grab":
            x = input("Name:\t")
            inventory.append(x)
            print(f"{x} was added.")
        elif cmd.strip().lower() == "edit":
            y = int(input("Number:\t")) - 1
            inventory[y] = input("Updated name:\t")
            print(f"Item number {y} was updated.")
        elif cmd.strip().lower() == "drop":
            y = int(input("Number:\t")) - 1
            removed = inventory.pop(y)
            print(f"{removed} was dropped.")
            inventory.pop(y)
        else:
            cmd.strip().lower() == "exit"
            print("Bye!")
            break

def main():
        menu_prompt()
        menu_funct()

if __name__ == "__main__":
    main()
    
        
