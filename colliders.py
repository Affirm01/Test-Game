import turtle
import random
from numbers import numberdict, drawNumber
from setup import head, snakebody, food, score_pixel1, score_pixel2, hs_pixel1, hs_pixel2
from score import score, highscore, score_display, score_pixel, hs_pixel

# Border Collision
def Border():
    global score
    global highscore
    if head.xcor() > 290 or head.xcor() < -290:
        head.goto(0, 0)
        head.next_direction = "stop"
        score = 0
        score_display.clear()
        score_display.goto(0, 260)
        score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

        # Score Display
        if score >= 100:
            digits_list = [int(x) for x in str(score)]
            drawNumber(score_pixel, digits_list[0], -510, 260)
            drawNumber(score_pixel1, digits_list[1], -440, 260)
            drawNumber(score_pixel2, digits_list[2], -370, 260)
        elif score >= 10:
            digits_list = [int(x) for x in str(score)]
            drawNumber(score_pixel, digits_list[0], -440, 260)
            drawNumber(score_pixel1, digits_list[1], -370, 260)
            score_pixel2.clearstamps()
        else:
            drawNumber(score_pixel, score, -370, 260)
            score_pixel1.clearstamps()
            score_pixel2.clearstamps()

        score_display.goto(0, 230)
        score_display.write("High Score: {}".format(highscore), align="center", font=("Arial", 24, "normal"))

        # High Score Display
        if highscore >= 100:
            digits_list = [int(x) for x in str(highscore)]
            drawNumber(hs_pixel, digits_list[0], -510, 130)
            drawNumber(hs_pixel1, digits_list[1], -440, 130)
            drawNumber(hs_pixel2, digits_list[2], -370, 130)
        elif highscore >= 10:
            digits_list = [int(x) for x in str(highscore)]
            drawNumber(hs_pixel, digits_list[0], -440, 130)
            drawNumber(hs_pixel1, digits_list[1], -370, 130)
            hs_pixel2.clearstamps()
        else:
            drawNumber(hs_pixel, highscore, -370, 130)
            hs_pixel1.clearstamps()
            hs_pixel2.clearstamps()

        if len(snakebody) > 0:
            for i in range(len(snakebody) - 1, -1, -1):
                snakebody[i].hideturtle()
            snakebody.clear()
    if head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.next_direction = "stop"
        score = 0
        score_display.clear()
        score_display.goto(0, 260)
        score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
        
        # Score Display
        if score >= 100:
            digits_list = [int(x) for x in str(score)]
            drawNumber(score_pixel, digits_list[0], -510, 260)
            drawNumber(score_pixel1, digits_list[1], -440, 260)
            drawNumber(score_pixel2, digits_list[2], -370, 260)
        elif score >= 10:
            digits_list = [int(x) for x in str(score)]
            drawNumber(score_pixel, digits_list[0], -440, 260)
            drawNumber(score_pixel1, digits_list[1], -370, 260)
            score_pixel2.clearstamps()
        else:
            drawNumber(score_pixel, score, -370, 260)
            score_pixel1.clearstamps()
            score_pixel2.clearstamps()

        score_display.goto(0, 230)
        score_display.write("High Score: {}".format(highscore), align="center", font=("Arial", 24, "normal"))

        # High Score Display
        if highscore >= 100:
            digits_list = [int(x) for x in str(highscore)]
            drawNumber(hs_pixel, digits_list[0], -510, 130)
            drawNumber(hs_pixel1, digits_list[1], -440, 130)
            drawNumber(hs_pixel2, digits_list[2], -370, 130)
        elif highscore >= 10:
            digits_list = [int(x) for x in str(highscore)]
            drawNumber(hs_pixel, digits_list[0], -440, 130)
            drawNumber(hs_pixel1, digits_list[1], -370, 130)
            hs_pixel2.clearstamps()
        else:
            drawNumber(hs_pixel, highscore, -370, 130)
            hs_pixel1.clearstamps()
            hs_pixel2.clearstamps()

        if len(snakebody) > 0:
            for i in range(len(snakebody) - 1, -1, -1):
                snakebody[i].hideturtle()
            snakebody.clear()
        head.next_direction = "stop"

# Fruit Collision and Spawn
def eatFruit():
    global score
    global highscore
    if head.distance(food) < 20:
        food.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
        body = turtle.Turtle()
        body.shape("square")
        body.color("black")
        body.shapesize(1, 1, None)
        body.penup()
        body.speed(0)
        body.goto(head.xcor(), head.ycor())
        snakebody.append(body)
        score += 1
        if score > highscore:
            highscore = score
        score_display.clear()
        score_display.goto(0, 260)
        score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
        
        # Score Display
        if score >= 100:
            digits_list = [int(x) for x in str(score)]
            drawNumber(score_pixel, digits_list[0], -510, 260)
            drawNumber(score_pixel1, digits_list[1], -440, 260)
            drawNumber(score_pixel2, digits_list[2], -370, 260)
        elif score >= 10:
            digits_list = [int(x) for x in str(score)]
            drawNumber(score_pixel, digits_list[0], -440, 260)
            drawNumber(score_pixel1, digits_list[1], -370, 260)
            score_pixel2.clearstamps()
        else:
            drawNumber(score_pixel, score, -370, 260)
            score_pixel1.clearstamps()
            score_pixel2.clearstamps()

        score_display.goto(0, 230)
        score_display.write("High Score: {}".format(highscore), align="center", font=("Arial", 24, "normal"))

        # High Score Display
        if highscore >= 100:
            digits_list = [int(x) for x in str(highscore)]
            drawNumber(hs_pixel, digits_list[0], -510, 130)
            drawNumber(hs_pixel1, digits_list[1], -440, 130)
            drawNumber(hs_pixel2, digits_list[2], -370, 130)
        elif highscore >= 10:
            digits_list = [int(x) for x in str(highscore)]
            drawNumber(hs_pixel, digits_list[0], -440, 130)
            drawNumber(hs_pixel1, digits_list[1], -370, 130)
            hs_pixel2.clearstamps()
        else:
            drawNumber(hs_pixel, highscore, -370, 130)
            hs_pixel1.clearstamps()
            hs_pixel2.clearstamps()

# Tail Collision
def SnakeCollision():
    global body
    global score
    for i in snakebody:
        if head.distance(i) < 20:
            head.goto(0, 0)
            head.next_direction = "stop"
            score = 0
            score_display.clear()
            score_display.goto(0, 260)
            score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

            # Score Display
            if score >= 100:
                digits_list = [int(x) for x in str(score)]
                drawNumber(score_pixel, digits_list[0], -510, 260)
                drawNumber(score_pixel1, digits_list[1], -440, 260)
                drawNumber(score_pixel2, digits_list[2], -370, 260)
            elif score >= 10:
                digits_list = [int(x) for x in str(score)]
                drawNumber(score_pixel, digits_list[0], -440, 260)
                drawNumber(score_pixel1, digits_list[1], -370, 260)
                score_pixel2.clearstamps()
            else:
                drawNumber(score_pixel, score, -370, 260)
                score_pixel1.clearstamps()
                score_pixel2.clearstamps()

            score_display.goto(0, 230)
            score_display.write("High Score: {}".format(highscore), align="center", font=("Arial", 24, "normal"))

            # High Score Display
            if highscore >= 100:
                digits_list = [int(x) for x in str(highscore)]
                drawNumber(hs_pixel, digits_list[0], -510, 130)
                drawNumber(hs_pixel1, digits_list[1], -440, 130)
                drawNumber(hs_pixel2, digits_list[2], -370, 130)
            elif highscore >= 10:
                digits_list = [int(x) for x in str(highscore)]
                drawNumber(hs_pixel, digits_list[0], -440, 130)
                drawNumber(hs_pixel1, digits_list[1], -370, 130)
                hs_pixel2.clearstamps()
            else:
                drawNumber(hs_pixel, highscore, -370, 130)
                hs_pixel1.clearstamps()
                hs_pixel2.clearstamps()

            if len(snakebody) > 0:
                for i in range(len(snakebody) - 1, -1, -1):
                    snakebody[i].hideturtle()
                snakebody.clear()