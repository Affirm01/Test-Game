import turtle
from main import gameLoop
from setup import wn
from movement import MoveRight, MoveLeft, MoveUp, MoveDown

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

# Start the Game
gameLoop()
turtle.done()