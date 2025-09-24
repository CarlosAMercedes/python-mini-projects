#main.py for 4-Function Calculator

def add(a,b):
    #Return the sum of two integers a b
    return a + b

def sub(a,b):
    #Return the product of two integers a b
    return a - b

def mul(a,b):
    #Return the sum of two integers a b
    return a * b

def div(a,b):
    #Return the quotient of two integers a b
    #If b = 0, return error
    if b ==0:
        return "Invalid🚫 Cannot divide by zero."
    return a / b

def get_num(prompt):
    #Ask user for an int
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")

def main():
#Asks user for operation, then executes.
    print("🖩Calculator🖩 (+, -, *, /). Type 'q' to quit.\n")

    while True:
        #Ask for operation
        op = input("Choose operation (+ - * /) or q: ")

        if op.lower() == "q":
            print("Goodbye!☺️")
            break

        if op not in {"+", "-", "*", "/"}:
            print("Invalid input🚫 Try again. \n")
            continue

        #Asks user for two int
        a = get_num("First integer: ")
        b = get_num("Second integer: ")

        #Execute operation
        if op == "+":
            result = add(a,b)
        elif op == "-":
            result = sub(a, b)
        elif op == "*":
            result = mul(a, b)
        else: 
            result = div(a, b)

        print(f"👍Result: {result}\n")

#Run the program
main()


            