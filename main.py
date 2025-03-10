from turtle import Turtle, Screen
import random

is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
tur = []
y = 0
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 30
    tur.append(new_turtle)



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle with win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in tur:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
