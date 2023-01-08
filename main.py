import math
import turtle

t = turtle.Turtle()
t.pensize(5)
line_height = 70
letter_distance = 35


# HAPPY NEW YEAR
# H
# AAA
# PP
# YY
# N
# EE
# W
# R

# H
def draw_h():
    H_half_tallness = line_height / 2
    H_middle_line_length = 55
    t.left(90)
    t.forward(H_half_tallness)
    t.back(H_half_tallness * 2)
    t.forward(H_half_tallness)
    t.right(90)
    t.forward(H_middle_line_length)
    t.left(90)
    t.forward(H_half_tallness)
    t.back(H_half_tallness * 2)
    t.forward(H_half_tallness)
    t.right(90)

    t.penup()
    t.forward(letter_distance)
    t.pendown()


# A
def draw_a():
    A_distance_from_intersection_to_start_of_A = 30
    A_side = math.sqrt(A_distance_from_intersection_to_start_of_A ** 2 + line_height ** 2)
    A_start_position = t.position()
    t.penup()
    t.setposition((A_start_position[0], A_start_position[1] - line_height / 2))
    t.pendown()
    angle_A_creates_with_90_degrees_line = math.degrees(math.asin(A_distance_from_intersection_to_start_of_A / A_side))
    t.left(90 - angle_A_creates_with_90_degrees_line)
    t.forward(A_side)
    t.right((90 - angle_A_creates_with_90_degrees_line) * 2)
    t.forward(A_side)
    angle_on_the_second_side = t.heading()
    t.backward(A_side / 2)
    t.setheading(0)
    A_angle_inside_the_triangle = 90 - angle_A_creates_with_90_degrees_line
    A_middle_line_length_half = math.cos(math.radians(A_angle_inside_the_triangle)) * A_side / 2
    t.backward(A_middle_line_length_half * 2)
    t.forward(A_middle_line_length_half * 2)
    t.setheading(angle_on_the_second_side)
    t.forward(A_side / 2)
    t.setheading(0)
    t.penup()
    t.forward(letter_distance)
    t.setheading(90)
    t.forward(line_height / 2)
    t.setheading(0)
    t.pendown()


# P
def draw_p():
    t.right(90)
    t.forward(line_height / 2)
    t.backward(line_height)
    circle_full_line = 30
    t.forward(circle_full_line)
    t.left(90)
    t.circle(circle_full_line / 2, 180)
    t.setheading(-90)
    t.forward(line_height / 2)
    t.setheading(0)

    t.penup()
    t.forward(letter_distance + circle_full_line / 2)
    t.pendown()


# Y
def draw_y():
    t.right(90)
    t.forward(line_height / 2)
    t.backward(line_height / 2 + line_height / 4)
    t.right(180)
    angle_of_sides_with_90_degrees_line = 30
    t.left(angle_of_sides_with_90_degrees_line)
    remaining_line_height = line_height / 2 - line_height / 4
    Y_side = math.cos(math.radians(angle_of_sides_with_90_degrees_line)) ** -1 * remaining_line_height
    t.forward(Y_side)
    t.backward(Y_side)
    t.right(angle_of_sides_with_90_degrees_line * 2)
    t.forward(Y_side)
    t.setheading(0)
    position_on_the_top_of_the_right_Y_side = t.position()
    t.penup()
    t.setposition((position_on_the_top_of_the_right_Y_side[0], 0))
    t.forward(letter_distance)
    t.pendown()


# N
def draw_n():
    t.right(90)
    t.forward(line_height / 2)
    t.backward(line_height)
    angle_of_N = 30
    t.left(angle_of_N)
    N_middle_line = math.cos(math.radians(angle_of_N)) ** -1 * line_height
    t.forward(N_middle_line)
    t.right(angle_of_N)
    t.backward(line_height)
    t.forward(line_height / 2)
    t.setheading(0)

    t.penup()
    t.forward(letter_distance)
    t.pendown()


# E
def draw_e():
    E_up_and_down = 50
    E_middle = E_up_and_down * 3 / 4
    t.right(90)
    t.forward(line_height / 2)
    t.left(90)
    t.forward(E_up_and_down)
    t.backward(E_up_and_down)
    t.right(90)
    t.backward(line_height / 2)

    t.left(90)
    t.forward(E_middle)
    t.backward(E_middle)
    t.right(90)
    t.backward(line_height / 2)

    t.left(90)
    t.forward(E_up_and_down)
    t.backward(E_up_and_down)
    t.right(90)
    t.forward(line_height / 2)

    t.setheading(0)
    t.penup()
    t.forward(E_middle)
    t.forward(letter_distance)
    t.pendown()


# W
def draw_w():
    first_angle = 15
    second_angle = 15
    t.left(90)
    t.penup()
    t.forward(line_height / 2)
    t.pendown()
    t.setheading(0)
    t.right(90 - first_angle)
    W_side = math.cos(math.radians(first_angle)) ** -1 * line_height
    t.forward(W_side)
    t.setheading(90)
    t.right(second_angle)
    t.forward(W_side)
    t.setheading(-90)
    t.left(second_angle)
    t.forward(W_side)
    t.setheading(90)
    t.right(first_angle)
    t.forward(W_side)

    t.setheading(0)
    position_on_the_top_of_the_right_W_side = t.position()
    t.penup()
    t.setposition((position_on_the_top_of_the_right_W_side[0], 0))
    t.forward(letter_distance)
    t.pendown()

# R
def draw_r():
    t.right(90)
    t.forward(line_height / 2)
    t.backward(line_height / 2)
    t.setheading(0)
    t.circle(line_height / 2 / 2, 180)
    t.setheading(-90)
    t.forward(line_height / 2)
    R_remaining_side_length = math.sqrt((line_height / 2) ** 2 + (line_height / 2 / 2) ** 2)
    angle_for_last_side = math.degrees(math.asin((line_height / 2 / 2)/R_remaining_side_length))
    t.left(angle_for_last_side)
    t.forward(R_remaining_side_length)
    t.backward(R_remaining_side_length)
    t.setheading(0)

    t.penup()
    t.forward(line_height / 2 / 2 + letter_distance)
    t.pendown()

# space
def draw_space():
    t.penup()
    t.forward(letter_distance)
    t.pendown()


# HAPPY NEW YEAR
# H
# AAA
# PP
# YY
# N
# EE
# W
# R
def draw_word(str):
    t.penup()
    t.setposition(-450, 0)
    t.pendown()
    str = str.upper()
    for letter in str:
        if letter == 'H':
            draw_h()
        elif letter == 'A':
            draw_a()
        elif letter == 'P':
            draw_p()
        elif letter == 'Y':
            draw_y()
        elif letter == 'N':
            draw_n()
        elif letter == 'E':
            draw_e()
        elif letter == 'W':
            draw_w()
        elif letter == 'R':
            draw_r()
        elif letter == ' ':
            draw_space()

draw_word("HAPPY NEW YEAR")

input()
