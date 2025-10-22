#Program that calculates the estimated hours and minutes for a trip.
print("Travel Time Calculator")
print()
#Receive user input
dist = int(input("Enter Miles:\t\t"))
mph = int(input("Enter Miles Per Hour:\t"))
print()
#Initialize variables
time = dist/mph
hrs = int(time)
min = (time - hrs) * 60 
#Return values
print("Hours:\t\t", hrs)
print(f"Minutes:\t {round(min)}")
