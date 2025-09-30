from logo import logo
should_continue = True
people = {}

print(logo)
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    people[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    print("\n" * 100)

    if answer == "no":
        should_continue = False

winner =  max(people, key=people.get)
highest_bid = people[winner]

print(f"The winner is {winner} with a bid of ${highest_bid}.")