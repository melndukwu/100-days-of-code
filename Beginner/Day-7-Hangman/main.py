import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print("HANGMAN")
print(f"Word to gless: {placeholder}")

lives = 6
game_over = False
correct_letters = []

while not game_over:
    print(f"{lives} lives left.")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}. That's not in the word. You lost a life.")
        if lives == 0:
            game_over = True

    if "_" not in display:
        print("You win.")
    elif lives == 0:
        print(f"The word was {chosen_word}.")
        print("You lose.")

    print(hangman_art.stages[lives])