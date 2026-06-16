## Tip Calculator
print("Welcome to the tip calculator!\n")

bill = int(input("What's the total bill? $"))
tip = int(input("How much tip would you like give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
total_bill = round(total_bill, 2)

split = total_bill / people
final_amount  = round(split, 2)

print(f"Total blil: ${total_bill:.2f}\n")
print(f"Each person should pay ${final_amount:.2f}")