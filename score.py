import turtle
from numbers import numberdict, drawNumber
from setup import score_pixel, hs_pixel

def highScore():
    global highscore
    with open('highscore.txt', 'w') as file:
        file.write("High Score: {highscore}")

# Score
score = 0
highscore = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
drawNumber(score_pixel, score, -370, 260)
score_display.goto(0, 230)
score_display.write("High Score: {}".format(highscore), align="center", font=("Arial", 24, "normal"))
drawNumber(hs_pixel, highscore, -370, 130)