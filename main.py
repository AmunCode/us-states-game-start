import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S.A.")
# screen.bgpic("blank_states_img.gif")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("50_states.csv")
all_states = state_data.state.to_list()

guessed_states = []


while len(guessed_states) < 50:
    usr_answer_state = screen.textinput(title="Guess the state.", prompt="Please enter another state name?").capitalize()

    if usr_answer_state in all_states:
        guessed_states.append(usr_answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        s_data = state_data[state_data.state == usr_answer_state]
        t.goto(int(s_data.x), int(s_data.y))
        t.write(usr_answer_state)


screen.exitonclick()

