import art
import game_data
import random

data = game_data.data


def check(item1, item2, answer):
    if answer == "A":
        if data[item1]["follower_count"] >= data[item2]["follower_count"]:
            return True
        else:
            return False
    if answer == "B":
        if data[item1]["follower_count"] <= data[item2]["follower_count"]:
            return True
        else:
            return False


def start_game():
    score = 0
    play_on = True
    item1 = random.randint(0, 51)
    item2 = random.randint(0, 51)
    while item2 == item1:
        item2 = random.randint(0, 51)

    while play_on:
        print(art.logo)
        print(f'Compare A:{data[item1]["name"]}, a {data[item1]["description"]} from {data[item1]["country"]}.')
        print(art.vs)
        print(f'Against B:{data[item2]["name"]}, a {data[item2]["description"]} from {data[item2]["country"]}.')
        answer = input("Who has more followers? Type A or B: ")
        if check(item1, item2, answer):
            score += 1
            item1 = random.randint(0, 51)
            item2 = random.randint(0, 51)
            if item2 == item1:
                item2 = random.randint(0, 51)
        else:
            print("Sorry your answer is wrong.")
            print(f'Your final score is: {score}.')
            play_on = False


start_game()
