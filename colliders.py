import turtle
import random
from numbers import drawNumber
from setup import head, snakebody, food, score_pixel, score_pixel1, score_pixel2, hs_pixel, hs_pixel1, hs_pixel2, letter_pixels, restart_pixels, quit_pixels, gameover_pixels, score_pixels, highscore_pixels
from score import score, highscore
from words import drawWord
import main

def displayScore():
    global score
    if score >= 100:
        digits_list = [int(x) for x in str(score)]
        drawNumber(score_pixel, digits_list[0], -442, 180)
        drawNumber(score_pixel1, digits_list[1], -412, 180)
        drawNumber(score_pixel2, digits_list[2], -382, 180)
    elif score >= 10:
        digits_list = [int(x) for x in str(score)]
        drawNumber(score_pixel, digits_list[0], -427, 180)
        drawNumber(score_pixel1, digits_list[1], -397, 180)
        score_pixel2.clearstamps()
    else:
        drawNumber(score_pixel, score, -412, 180)
        score_pixel1.clearstamps()
        score_pixel2.clearstamps()

def displayHighscore():
    global highscore
    if highscore >= 100:
        digits_list = [int(x) for x in str(highscore)]
        drawNumber(hs_pixel, digits_list[0], -442, 80)
        drawNumber(hs_pixel1, digits_list[1], -412, 80)
        drawNumber(hs_pixel2, digits_list[2], -382, 80)
    elif highscore >= 10:
        digits_list = [int(x) for x in str(highscore)]
        drawNumber(hs_pixel, digits_list[0], -427, 80)
        drawNumber(hs_pixel1, digits_list[1], -397, 80)
        hs_pixel2.clearstamps()
    else:
        drawNumber(hs_pixel, highscore, -412, 80)
        hs_pixel1.clearstamps()
        hs_pixel2.clearstamps()


# Border Collision
def Border():
    global score
    global highscore
    if head.xcor() > 290 or head.xcor() < -290:
        head.goto(0, 0)
        head.next_direction = "stop"
        score = 0

        # Score & Highscore Display
        displayScore()
        drawWord("SCORE", score_pixels, -450, 220, 5)
        displayHighscore()
        drawWord("HIGHSCORE", highscore_pixels, -480, 120, 5)

        main.gameOver = True
        drawWord("GAME OVER", gameover_pixels, -206, 44, 12)
        drawWord("PRESS R TO RESTART", restart_pixels, -147, -33, 5)
        drawWord("PRESS Q TO QUIT", quit_pixels, -147, -71, 5)
        

        if len(snakebody) > 0:
            for i in range(len(snakebody) - 1, -1, -1):
                snakebody[i].hideturtle()
            snakebody.clear()

    if head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.next_direction = "stop"
        score = 0

        displayScore()
        drawWord("SCORE", score_pixels, -450, 220, 5)
        displayHighscore()
        drawWord("HIGHSCORE", highscore_pixels, -480, 120, 5)

        main.gameOver = True
        drawWord("GAME OVER", gameover_pixels, -206, 44, 12)
        drawWord("PRESS R TO RESTART", restart_pixels, -205, -33, 5)
        drawWord("PRESS Q TO QUIT", quit_pixels, -205, -71, 5)

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
        
        # Score & Highscore Display
        displayScore()
        drawWord("SCORE", score_pixels, -450, 220, 5)
        displayHighscore()
        drawWord("HIGHSCORE", highscore_pixels, -480, 120, 5)

# Tail Collision
def SnakeCollision():
    global body
    global score
    for i in snakebody:
        if head.distance(i) < 20:
            head.goto(0, 0)
            head.next_direction = "stop"
            score = 0

            # Score & Highscore Display
            displayScore()
            drawWord("SCORE", score_pixels, -450, 220, 5)
            displayHighscore()
            drawWord("HIGHSCORE", highscore_pixels, -480, 90, 5)

            main.gameOver = True
            drawWord("GAME OVER", gameover_pixels, -206, 44, 12)
            drawWord("PRESS R TO RESTART", restart_pixels, -205, -33, 5)
            drawWord("PRESS Q TO QUIT", quit_pixels, -205, -71, 5)

            if len(snakebody) > 0:
                for i in range(len(snakebody) - 1, -1, -1):
                    snakebody[i].hideturtle()
                snakebody.clear()