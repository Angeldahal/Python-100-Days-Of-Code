import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = 'blank_states_img.gif'
screen.register_shape(image)
turtle.shape(image)

guessed_states = []
data = pandas.read_csv('50_states.csv')
while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct ", prompt = "What's another state name?")
    answer_state = answer_state.title()
    all_states = data["state"].to_list()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
remaining_states = []
for state in all_states:
    if state not in guessed_states:
        remaining_states.append(state)
df = pandas.DataFrame(remaining_states)
df.to_csv('states_to_learn.csv')
