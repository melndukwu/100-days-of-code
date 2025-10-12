import random
import characters_list as c

score = 0

# picking two different characters
a = random.choice(c.danmei_characters)
b = random.choice(c.danmei_characters)
while b == a or b["height"] == a["height"]:
    b = random.choice(c.danmei_characters)

should_continue = True

print("Guess which Danmei character is taller!")
while should_continue:

    print(f"Compare A: {a['name']}, {a['bio']}")
    print(f"Against B: {b['name']}, {b['bio']}")

    #ask user for a guess
    answer = input("Who is taller? Type 'A' or 'B': ").lower()

    def check_answer():
        if a["height"] > b["height"]:
            return answer == "a"
        else:
            return answer == "b"

    #check if user is correct
    if check_answer():
        score += 1
        print("\n" * 20)
        print(f"You're right! Current score: {score}")

        #next round
        a = b
        b = random.choice(c.danmei_characters)
        while b == a or b["height"] == a["height"]:
            b = random.choice(c.danmei_characters)
    else:
        print(f"Wrong! Final score: {score}")
        should_continue = False