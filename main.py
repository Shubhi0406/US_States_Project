import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

game_is_on = True
guessed = []
while len(guessed) < 50 and game_is_on:
    answer_state = screen.textinput(title=f"Score: {len(guessed)}/50",
                                    prompt="Enter State (or, type 'quit' to exit):").title()
    data = pandas.read_csv("50_states.csv")
    state = data["state"]

    if answer_state == "Quit":
        states_missed = [each_state for each_state in state if each_state not in guessed]
        states_missed_dict = {
            "States Missed": states_missed
        }
        states_missed_file = pandas.DataFrame(states_missed_dict)
        states_missed_file.to_csv("States_to_Learn.csv")
        game_is_on = False

    elif answer_state not in guessed:
        for each_state in state:
            if each_state == answer_state:
                state_row = data[state == each_state]
                state_xcor = int(state_row.x)
                state_ycor = int(state_row.y)
                writer.goto(state_xcor, state_ycor)
                writer.write(arg=each_state, align="center", font=("Calibri", 10, "bold"))
                guessed.append(answer_state)

if len(guessed) == 50:
    replay = screen.textinput(title=f"Score: {len(guessed)}/50", prompt="Well done! You guessed all the states! "
                                                                        "'Replay' or 'Quit'?").title()
    if replay == "Replay":
        guessed = []
    else:
        game_is_on = False
