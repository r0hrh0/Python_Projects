import random
import os

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo, "\n")
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

blanks = []
for n in range(word_length):
    blanks += "_"

print(" ".join(blanks))

end_of_game = False
lives = 6

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    os.system('cls')

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            blanks[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(hangman_art.stages[lives])
            print(f"You lose. The word was {chosen_word}.\n")
            end_of_game = True
            break

    if "_" not in blanks:
        end_of_game = True
        print(f"You Win. The word was {chosen_word}!\n")
        break

    print(" ".join(blanks))
    print(f"Lives remaining : {lives}")
    print(hangman_art.stages[lives])
