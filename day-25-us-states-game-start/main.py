import turtle
import pandas


screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
a=data["state"].to_list()
stat=[]
while len(stat)<50:
    user=screen.textinput(title=f"{len(stat)}/50 states",prompt="enter your answer").title()

    print(user)
    if user == "Exit":
        miss=[]
        for state in a:
            if state not in user:
                miss.append(state)
        c=pandas.DataFrame(miss)
        d=c.to_csv("learn.csv")
        print(miss)
        break

    if user in a:
        stat.append(user)
        tom =turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        b=data[data.state==user]
        tom.goto(b.x.item(),b.y.item())
        tom.write(user)






