from turtle import Screen, Turtle
from random import randint


def make_screen():
    main_screen = Screen()
    main_screen.title("Snake Game")
    main_screen.bgcolor("black")
    main_screen.setup(600, 600)
    main_screen.tracer(False)
    return main_screen


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_food_position(food):
    xpos = randint(-270, 270)
    ypos = randint(-270, 230)
    food.goto(xpos, ypos)


def move_snake(head):
    if head.direction == "up":
        ypos = head.ycor()
        head.sety(ypos + 20)
    if head.direction == "down":
        ypos = head.ycor()
        head.sety(ypos - 20)
    if head.direction == "left":
        xpos = head.xcor()
        head.setx(xpos - 20)
    if head.direction == "right":
        xpos = head.xcor()
        head.setx(xpos + 20)


def change_dir_to_up(head):
    if head.direction != "down":
        head.direction = "up"


def change_dir_to_down(head):
    if head.direction != "up":
        head.direction = "down"


def change_dir_to_left(head):
    if head.direction != "right":
        head.direction = "left"


def change_dir_to_right(head):
    if head.direction != "left":
        head.direction = "right"


def reset(head, tails):
    head.home()
    head.direction = ""
    for tail in tails:
        tail.ht()

    tails.clear()
