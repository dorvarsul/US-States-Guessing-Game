import turtle
import pandas

SCORE = 0
# Screen Settings
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Check Answer
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state name?:").title()
    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
        SCORE += 1
    elif answer_state == "Exit":
        break


states_to_learn = []
for i in all_states:
    if i not in guessed_states:
        states_to_learn.append(i)
    else:
        pass

print(f"Your final score is: {SCORE} out of 50 states")
edu = pandas.DataFrame(states_to_learn)
edu.to_csv("states_to_learn.csv")