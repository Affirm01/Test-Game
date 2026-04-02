from setup import head, snakebody, wn, score_pixels, highscore_pixels
from colliders import eatFruit, Border, SnakeCollision, displayHighscore, displayScore
from movement import Move
from words import drawWord

gameOver = False

# Main Game Loop
def gameLoop():
    if gameOver:
        return
    
    displayScore()
    drawWord("SCORE", score_pixels, -510, 220, 5)
    displayHighscore()
    drawWord("HIGHSCORE", highscore_pixels, -510, 90, 5)

    eatFruit()
    for i in range(len(snakebody) - 1, 0, -1):
        if len(snakebody) > 0:
            snakebody[i].goto(snakebody[i-1].xcor(), snakebody[i-1].ycor())
    if len(snakebody) > 0:
        snakebody[0].goto(head.xcor(), head.ycor())
    head.direction = head.next_direction
    Move()
    Border()
    SnakeCollision()
    wn.update()
    wn.ontimer(gameLoop, 45)