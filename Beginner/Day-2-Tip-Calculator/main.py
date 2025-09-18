print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip = bill * (tip_percentage/100)
total = (round((bill + tip) / people, 2))

print(f"Each person should pay: ${total}")