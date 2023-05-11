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
# still need to draw: #B, C, D, F, G, I, J, K, L, M, O, Q, S, T, U, V, X, Z

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


# B
def draw_b():
    t.right(90)
    t.forward(line_height / 2)
    t.left(90)
    t.forward(line_height / 4)
    t.circle(line_height / 4, 180)
    pos = t.pos()
    t.right(180)
    t.circle(line_height / 4, 180)
    t.forward(line_height / 4)
    t.right(90)
    t.right(180)
    t.forward(line_height / 2)
    t.penup()
    t.setposition((pos[0], pos[1]))
    t.setheading(0)
    t.forward(letter_distance)
    t.pendown()

# C
def draw_c():
    initial_pos = t.pos()
    y = t.pos()[1]
    t.right(90)
    t.circle(line_height / 2, 90)
    x = t.pos()[0]
    t.penup()
    t.setposition(initial_pos)
    t.pendown()
    t.setheading(0)
    t.left(90)
    t.circle(line_height / -2, 90)
    t.penup()
    t.setposition((x, y))
    t.forward(letter_distance)
    t.pendown()

# D
def draw_d():
    t.right(90)
    t.forward(line_height/2)
    t.back(line_height)
    t.right(90)
    t.circle(line_height/2, -180)
    t.left(90)
    t.forward(line_height/2)
    t.right(90)
    t.penup()
    t.forward(line_height/2) # radius
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

# F
def draw_f():
    t.right(90) # turn 90 degrees
    t.forward(line_height/2) # make the lower vertical
    t.back(line_height) # make the upper vertical
    t.left(90) # turn the head to forward
    t.forward(line_height/2) # make the upper horizontal
    t.back(line_height/2) # come back
    t.right(90) # head down
    t.forward(line_height/2) # get to the middle
    t.left(90) # turn the head to forward
    t.forward(line_height/2) # make the middle horizontal
    t.penup()
    t.forward(letter_distance)
    t.pendown()

# G
def draw_g():
    t.penup()
    t.forward(line_height/2)
    t.left(90)
    t.forward(line_height/2)
    t.pendown()
    t.right(90)
    t.forward(line_height/6)
    t.back(line_height/6)
    t.right(180)
    t.circle(line_height/2, 270)
    t.left(90)
    t.forward(line_height/2)
    t.back(line_height/2)
    t.right(180)
    t.penup()
    t.forward(letter_distance)
    t.pendown()

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


# I
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

# J
def draw_j():
    t.penup()
    t.forward(line_height/3)
    t.pendown()
    t.left(90)
    t.forward(line_height/2)
    t.right(90)
    t.forward(line_height/4)
    t.right(90)
    t.forward(line_height/8)
    t.back(line_height/8)
    t.left(90)
    t.back(line_height/4)
    t.back(line_height/4)
    t.right(90)
    t.forward(line_height/8)
    t.back(line_height/8)
    t.left(90)
    t.forward(line_height/4)
    t.right(90)
    t.forward(line_height/2)
    t.forward(line_height/4)
    t.circle(-line_height/4, 180)
    t.right(180)
    t.circle(line_height/4, 180)
    t.forward(line_height/4)
    t.right(90)
    t.penup()
    t.forward(letter_distance)
    t.pendown()

# K
def draw_k():
    middle_y = t.pos()[1]
    t.right(90)
    t.forward(line_height/2)
    t.back(line_height)
    t.forward(line_height/2)
    t.right(180)
    k_degree = 45
    side_length = line_height/ 2 / math.cos(math.radians(k_degree))
    t.right(k_degree)
    t.forward(side_length)
    t.back(side_length)
    t.right(180 - k_degree * 2)
    t.forward(side_length)
    t.back(side_length/3)
    t.penup()
    t.goto(t.pos()[0], middle_y)
    t.setheading(0)
    t.forward(letter_distance)
    t.pendown()

# L
def draw_l():
    middle_y = t.pos()[1]
    t.left(90)
    t.forward(line_height/2)
    t.back(line_height)
    t.right(90)
    t.forward(line_height/2)
    t.left(90)
    t.forward(line_height/8)
    t.back(line_height/8)
    t.right(90)
    t.back(line_height/8)
    t.penup()
    t.goto(t.pos()[0], middle_y)
    t.setheading(0)
    t.forward(letter_distance)
    t.pendown()

# M
def draw_m():
    t.right(90)
    t.forward(line_height/2)
    t.right(180)
    t.forward(line_height)
    t.right(90)
    m_degree = 25
    t.right(90 - m_degree)
    side_length = line_height / math.cos(math.radians(m_degree))
    t.forward(side_length)
    t.left(90 - m_degree)
    t.left(90 - m_degree)
    t.forward(side_length)
    t.setheading(-90)
    t.forward(line_height)
    t.back(line_height/2)
    t.left(90)
    t.penup()
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

# O
def draw_o():
    t.right(90)
    t.circle(line_height/2)
    t.left(90)
    t.penup()
    t.forward(line_height)
    t.forward(letter_distance)
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

# Q
def draw_q():
    t.right(90)
    t.circle(line_height / 2)
    t.left(90)
    t.penup()
    t.forward(line_height / 2)
    t.right(90)
    t.forward(line_height / 8 * 1.5) # I'm trying to start the \ line lower than the middle of the circle
    left_side = line_height / 2 - (line_height / 8 * 1.5) # all these calculations is to find the new angle based on the new start
    bottom_side = line_height / 2
    angle_radian = math.atan(bottom_side / left_side)
    angle_degrees = math.degrees(angle_radian)
    t.left(angle_degrees)
    t.pendown()
    side_length = bottom_side / math.sin(angle_radian)
    t.forward(side_length)
    t.penup()
    t.left(90 - angle_degrees)
    t.left(90)
    t.forward(line_height / 2)
    t.right(90)
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

# S

# T

# U

# V

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

# X


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


# Z





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
        if letter == 'A':
            draw_a()
        elif letter == 'B':
            draw_b()
        elif letter == 'C':
            draw_c()
        elif letter == 'D':
            draw_d()
        elif letter == 'E':
            draw_e()
        elif letter == 'F':
            draw_f()
        elif letter == "G":
            draw_g()
        elif letter == 'H':
            draw_h()
        elif letter == 'I':
            draw_i()
        elif letter == 'J':
            draw_j()
        elif letter == 'K':
            draw_k()
        elif letter == "L":
            draw_l()
        elif letter == "M":
            draw_m()
        elif letter == 'N':
            draw_n()
        elif letter == "O":
            draw_o()
        elif letter == 'P':
            draw_p()
        elif letter == 'Q':
            draw_q()
        elif letter == 'R':
            draw_r()
        elif letter == 'W':
            draw_w()
        elif letter == 'Y':
            draw_y()
        elif letter == ' ':
            draw_space()

# draw_word("HAPPY NEW YEAR")
draw_word("IQQI")







input()
