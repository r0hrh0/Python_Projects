# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art

print(art.logo)

play_on = True


def choose_level():
    level = input("Choose Level (Easy/Hard): ").lower()
    print(level, "\n")
    if level == "easy":
        lives = 10
    else:
        lives = 5
    return lives


def target_number():
    import random
    targ_numb = random.randint(1, 101)
    return targ_numb


def get_guess():
    number = int(input("Guess the number between 1 and 100: "))
    return number


def check_num(target_num, guessed_num):
    if guessed_num == target_num:
        print("Answer is correct!")

    elif guessed_num < target_num:
        print("Too Low.")

    elif guessed_num > target_num:
        print("Too High.")


lives_left = choose_level()
targ_num = target_number()
print(f"Answer to be guessed is: {targ_num}\n")
print(f"Lives left is:{lives_left}")

while play_on:
    guess = get_guess()
    check_num(targ_num, guess)
    if guess != targ_num:
        lives_left -= 1
        print(f"Lives left:{lives_left}")

    if lives_left <= 0 or guess == targ_num:
        play_on = False
        if lives_left <= 0:
            print("No more lives left. You lose.\n")
