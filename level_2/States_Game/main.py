from turtle import Turtle, Screen
import pandas as pd

turtle = Turtle()
data = pd.read_csv("50_states.csv")
screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_states = data.state.to_list()
score = 0
correct_count = 0
state_turtle = Turtle()
state_turtle.penup()
state_turtle.hideturtle()
correct_states = []
while score < 50:
    answer_state = screen.textinput(title=f"{score} / 50", prompt="Can you name all states?").title()
    if answer_state in all_states:
        correct_states.append(answer_state)
        score += 1
        answer_state_data = data[data.state == answer_state]
        answer_state_x = int(answer_state_data.x)
        answer_state_y = int(answer_state_data.y)
        state_turtle.goto(answer_state_x, answer_state_y)
        state_turtle.write(answer_state)

    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in correct_states]
        df = pd.DataFrame(missing_states)
        df.to_csv("States_To_Learn.csv", index=False)
        break






# -------------------------- creating the 50_states csv file by copying the csv file given by the instructor-----------

# with open("/us-states-game-start/50_states.csv") as state_data_file:
#     state_data = state_data_file.readlines()
# print(state_data)
#
# data = pd.read_csv("/us-states-game-start/50_states.csv")
#
# state = data.state.to_list()
# x = data.x.to_list()
# y = data.y.to_list()
#
# data_dict = {
#     "state": state,
#     "x": x,
#     "y": y
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv("50_states.csv", index=False)
# ---------------------------------------------------------------------------------------------------------------------
