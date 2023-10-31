import turtle
import pandas as pd

guessed_state = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer_state == "Exit":
        states_not_found = []
        for state in all_states:
            if state not in guessed_state:
                states_not_found.append(state)
        new_data = pd.DataFrame(states_not_found)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
