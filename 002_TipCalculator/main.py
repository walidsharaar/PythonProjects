# Welcome note

print("Welcome to the tip calculator.")

#ask the amount
amount=float(input("What was the bill amount? \n$"))

#ask tip percentage 10,12,15 %
tip_percentage=int(input("What percentage tip you like to give? "))

#ask number of people  which is going to split
no_people=int(input("How many people to split the bill?"))

# tip changed to percentage

percentage = tip_percentage/100;

tip = amount * percentage

# Total bill calculation
total = tip+ amount

amount_to_pay = round((total/no_people),2)

print(f"Each person have to pay : {amount_to_pay}"+"$")