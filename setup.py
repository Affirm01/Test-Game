import turtle
import random

# Screen Setup
wn = turtle.Screen()
wn.title("Snake Game by Affirm")
wn.setup(width=1000, height=650)
wn.bgcolor("#3B5C62")
wn.tracer(0)

# Checkered Background
background = turtle.Turtle()
background.shape("square")
background.speed(0)
background.penup()
for i in range(-280, 300, 20):
    for j in range(-280, 300, 20):
        if (i + j) // 20 % 2 == 0:
            background.color("#33c3c8")
            background.goto(i, j)
            background.stamp()
        else:
            background.goto(i, j)
            background.color("#21A0AE")
            background.stamp()
background.hideturtle()

# Border Setup
border = turtle.Turtle()
border.speed(0)
border.color("#8BB8BD")
border.penup()
border.goto(-295, -295)
border.pensize(9)
border.pendown()
for i in range(4):
    border.forward(590)
    border.left(90)
border.hideturtle()

# Letter Display Setup
letter_pixels = []
for i in range(20):
    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.shapesize(0.6, 0.6, None)
    pixel.color("#FDFDFD")
    pixel.penup()
    pixel.hideturtle()
    letter_pixels.append(pixel)

# Game Over, Restart, and Quit Display Setup
gameover_pixels = []
for i in range (9):
    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.shapesize(0.6, 0.6, None)
    pixel.color("#FDFDFD")
    pixel.penup()
    pixel.hideturtle()
    gameover_pixels.append(pixel)

restart_pixels = []
for i in range(18):
    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.shapesize(0.25, 0.25, None)
    pixel.color("#FDFDFD")
    pixel.penup()
    pixel.hideturtle()
    restart_pixels.append(pixel)

quit_pixels = []
for i in range(15):
    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.shapesize(0.25, 0.25, None)
    pixel.color("#FDFDFD")
    pixel.penup()
    pixel.hideturtle()
    quit_pixels.append(pixel)

score_pixels = []
for i in range(6):
    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.shapesize(0.3, 0.3, None)
    pixel.color("#FDFDFD")
    pixel.penup()
    pixel.hideturtle()
    score_pixels.append(pixel)

highscore_pixels = []
for i in range(9):
    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.shapesize(0.3, 0.3, None)
    pixel.color("#FDFDFD")
    pixel.penup()
    pixel.hideturtle()
    highscore_pixels.append(pixel)

# Score Display Setup
score_pixel = turtle.Turtle()
score_pixel.speed(0)
score_pixel.shape("square")
score_pixel.shapesize(0.4, 0.4, None)
score_pixel.color("#FDFDFD")
score_pixel.penup()
score_pixel.hideturtle()

score_pixel1 = turtle.Turtle()
score_pixel1.speed(0)
score_pixel1.shape("square")
score_pixel1.shapesize(0.4, 0.4, None)
score_pixel1.color("#FDFDFD")
score_pixel1.penup()
score_pixel1.hideturtle()

score_pixel2 = turtle.Turtle()
score_pixel2.speed(0)
score_pixel2.shape("square")
score_pixel2.shapesize(0.4, 0.4, None)
score_pixel2.color("#FDFDFD")
score_pixel2.penup()
score_pixel2.hideturtle()

# Highscore Display Setup
hs_pixel = turtle.Turtle()
hs_pixel.speed(0)
hs_pixel.shape("square")
hs_pixel.shapesize(0.4, 0.4, None)
hs_pixel.color("#FDFDFD")
hs_pixel.penup()
hs_pixel.hideturtle()

hs_pixel1 = turtle.Turtle()
hs_pixel1.speed(0)
hs_pixel1.shape("square")
hs_pixel1.shapesize(0.4, 0.4, None)
hs_pixel1.color("#FDFDFD")
hs_pixel1.penup()
hs_pixel1.hideturtle()

hs_pixel2 = turtle.Turtle()
hs_pixel2.speed(0)
hs_pixel2.shape("square")
hs_pixel2.shapesize(0.4, 0.4, None)
hs_pixel2.color("#FDFDFD")
hs_pixel2.penup()
hs_pixel2.hideturtle()

# Snake Head
head = turtle.Turtle()
head.direction = "stop"
head.next_direction = "stop"
head.shape("square")
head.color("black")
head.shapesize(1, 1, None)
head.penup()
head.goto(0, 0)
head.speed(0)

# Snake Food
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.shapesize(1, 1, None)
food.penup()
food.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)

# Snake Body
snakebody = []