import turtle
import pandas

# Setup:
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
guessed_states = []

# Turtle to write states names:
name = turtle.Turtle()
name.hideturtle()
name.penup()
name.speed(0)

def write_state(state):
    state_data = df[df.state == state]
    state_name = state_data.state.item()
    x_cor = state_data.x.item()
    y_cor = state_data.y.item()
    name.goto(x_cor, y_cor)
    name.write(state_name, align="center", font=("Arial", 8, "normal"))

while len(guessed_states) < 50:
    # Get input from user and convert to Title case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name?").title()

    # Check if the guess is among the 50 states
    check_answer = df[df.state == answer_state]

    # Write correct guesses onto the map
    if answer_state == "Exit":
        # save missed states in states_to_learn_csv.
        list_of_all_states = df.state.to_list()
        list_of_states_to_learn = [state for state in list_of_all_states if state not in guessed_states]
        df2 = pandas.DataFrame(list_of_states_to_learn)
        df2.to_csv("states_to_learn.csv", header=False, index=False)
        # show missed states in red
        name.color("red")
        for state in list_of_states_to_learn:
            write_state(state)
        break
    if not check_answer.empty:
        write_state(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

turtle.mainloop()