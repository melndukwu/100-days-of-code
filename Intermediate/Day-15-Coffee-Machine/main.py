import menu as m

profit = 0

def is_resource_sufficient(order_ingredients):
    """returns true when order can be made, false if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= m.resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    """returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """returns true when the payment is accepted, or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2 )
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        m.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        for i, v in m.resources.items():
            print(f"{i.capitalize()}: {v}")
        print(f"Money: ${profit}")
    else:
        drink = m.menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
