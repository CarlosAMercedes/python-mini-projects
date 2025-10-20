groceries = []

def menu(groceries):
    while True:
        cmd = input("Menu. Select option: Add.\nRemove.\nShow.\nClear.\nExit.\n")
        if cmd.strip().lower() == "add":
            addition = input("Added item: ")
            groceries.append(addition)
            print()
        elif cmd.strip().lower() == "remove":
            print(groceries)
            removed = int(input("Removed item: (number) "))-1
            groceries.pop(removed)
            print()
        elif cmd.strip().lower() == "Show.":
            length = len(groceries)
            print(f"List length: {length}. Items in list {groceries}")
            print()
        elif cmd.strip().lower() == "Clear.":
            groceries.clear()
            print(groceries)
            print()
        elif cmd == "Exit.":
            break
        
def main():
    menu(groceries)

if __name__ == "__main__":
    main()
    