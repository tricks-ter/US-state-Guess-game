import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("U.S states Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
n=0
guessed=[]

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
while n<=50:
    answer=screen.textinput(title="Guess state",prompt="Name of state").title()
######
    if answer=="Exit":
        missing=[]
        for state in all_states:
            if state not in guessed:
                missing.append(state)
                temp=state
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                state_data = data[data.state == temp]
                t.goto(int(state_data.x), int(state_data.y))
                t.write(temp)
        new_data=pd.DataFrame(missing)
        new_data.to_csv("Missed ones.csv")




        break
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))

        t.write(answer)

        guessed.append(answer)
    n=n+1
turtle.mainloop()
