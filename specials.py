import math
import turtle

t = turtle.Turtle()
t.pensize(5)
line_height = 70
letter_distance = 35

def draw_i():
    t.penup()
    t.forward(line_height/4)
    t.pendown()
    t.left(90)
    t.forward(line_height/2)
    t.left(90)
    t.forward(line_height/4)
    t.back(line_height/2)
    t.forward(line_height/4)
    t.left(90)
    t.forward(line_height)
    t.right(90)
    t.forward(line_height/4)
    t.back(line_height/2)
    t.forward(line_height/4)
    t.right(90)
    t.forward(line_height/2)
    t.right(90)
    t.penup()
    t.forward(line_height/4)
    t.forward(letter_distance)
    t.pendown()

def draw_q_wrong():
    t.right(90)
    t.circle(line_height / 2)
    t.left(90)
    t.penup()
    t.forward(line_height / 2)
    t.pendown()
    t.right(45)
    side_length = math.sqrt(2 * (line_height / 2) ** 2) ## diameter of a square
    t.forward(side_length)
    t.penup()
    t.left(45)
    t.left(90)
    t.forward(line_height / 2)
    t.left(90)
    t.forward(letter_distance)
    t.pendown()

def draw_special_2():
    draw_q_wrong()
    draw_q_wrong()
    draw_i()

def logic_special_1():
    draw_i()
    t.left(90)
    t.circle(line_height / 2)
    t.left(90)
    t.circle(line_height / 2)
    draw_i()

def draw_special_1():
    logic_special_1()
    for i in range(3):
        t.penup()
        t.back(line_height)
        t.left(90)
        t.pendown()
        logic_special_1()


if __name__ == "__main__":
    draw_special_2()
    t.hideturtle()
    input()