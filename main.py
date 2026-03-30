from setup import head, snakebody, wn
from colliders import eatFruit, Border, SnakeCollision
from movement import Move, MoveRight, MoveLeft, MoveUp, MoveDown

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