print("Letter Grade Calculator\n")

#cont = "y"

while True:

    cont = input("Continue? (Y/N):\t")

    if cont.lower().strip() != "y":
        break
    else:
        pass

    grade = int(input("Enter numerical grade: "))
    print()

    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        continue

    if grade >= 88:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 67:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else: 
        letter_grade = "F"
    print()
    print(f"Your letter grade is: \t{letter_grade}")
    print()
    
    print()

print("Bye!")

    
