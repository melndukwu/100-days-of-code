print("Welcome to Treasure Island! \nYour mission is to find the treasure.")
cross_road = input("You're at a cross road. Where do you want to go? \nType 'left'' or 'right':\n>>> ").lower()

if cross_road == "right":
    print("You fell into a hole. Game over.")
elif cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across:\n>>> ").lower()
    if wait_or_swim == "swim":
        print("You got attacked by an angry trout. Game Over")
    elif wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose?\n>>> ").lower()
        if door == "red" or door == "blue":
            print("It's a room full of fire. Game over.")
        elif door == "yellow":
            print("You found the treasure. You win!")
