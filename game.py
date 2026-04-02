import turtle
from main import gameLoop
from setup import wn, head, snakebody, restart_pixels, quit_pixels, gameover_pixels
from colliders import displayScore, displayHighscore
from movement import MoveRight, MoveLeft, MoveUp, MoveDown
import score as sc
import main

# Keyboard Recording
wn.listen()

# Keyboard Bindings
wn.onkeypress(MoveRight, "d")
wn.onkeypress(MoveRight, "Right")

wn.onkeypress(MoveLeft, "a")
wn.onkeypress(MoveLeft, "Left")

wn.onkeypress(MoveUp, "w")
wn.onkeypress(MoveUp, "Up")

wn.onkeypress(MoveDown, "s")
wn.onkeypress(MoveDown, "Down")

def restart():
    if not main.gameOver:
        return
    sc.score = 0

    # Score & Highscore Display
    displayScore()
    displayHighscore()

    head.goto(0, 0)
    head.next_direction = "stop"

    for i in range(len(snakebody) - 1, -1, -1):
        snakebody[i].hideturtle()

    for pixel in restart_pixels:
        pixel.clearstamps()
    for pixel in quit_pixels:
        pixel.clearstamps()
    for pixel in gameover_pixels:
        pixel.clearstamps()

    snakebody.clear()

    main.gameOver = False
    gameLoop()

def quitGame(): 
    if not main.gameOver:
        return
    turtle.bye()

wn.onkeypress(restart, "r")
wn.onkeypress(quitGame, "q")

# Start the Game
gameLoop()
turtle.done()