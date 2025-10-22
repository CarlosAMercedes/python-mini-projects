#Program that calculates a user's weekly gross and take-home pay
#Display Title
print("Paycheck Calculator")
print()
#User inputs hours worked and pay rate
hrs_worked = int(input("Hours Worked:\t\t"))
hr_pay = round(float(input("Hourly Pay Rate:\t")),2)
print()
#Initialize variables
grs_pay = round(hrs_worked * hr_pay, 2)
tax_rate = 18
tax_amt = round(grs_pay * (tax_rate/100), 2)
home_pay = round(grs_pay - tax_amt, 2)
#Return calculations
print("Gross Pay:\t", grs_pay)
print(f"Tax Rate:\t {tax_rate}%")
print("Tax Amount:\t", tax_amt)
print("Take Home Pay:\t", grs_pay - tax_amt)
