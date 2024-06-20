#create a tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

bill = float(input("What is your total bill? $"))

tip = int(input("How much would you like to tip? 10, 12, or 15 "))

people_split = int(input("How many people would you like to split with?"))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_split = total_bill / people_split
final_amt = (round(bill_split, 2))

print(f"Each person should pay ${final_amt}")
