from setup import head, snakebody, wn
from colliders import eatFruit, Border, SnakeCollision
from movement import Move

# Main Game Loop
def gameLoop():
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