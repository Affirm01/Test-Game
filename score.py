def highScore():
    global highscore
    with open('highscore.txt', 'w') as file:
        file.write("High Score: {highscore}")

# Score
score = 0
highscore = 0