from setup import head, snakebody

# Move Right
def MoveRight():
    if head.direction != "left" or len(snakebody) == 0:
        head.next_direction = "right"

# Move Left
def MoveLeft():
    if head.direction != "right" or len(snakebody) == 0:
        head.next_direction = "left"

# Move Up
def MoveUp():
    if head.direction != "down" or len(snakebody) == 0:
        head.next_direction = "up"

# Move Down
def MoveDown():
    if head.direction != "up" or len(snakebody) == 0:
        head.next_direction = "down"

# Dictates the movement of the snake head
def Move():
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)