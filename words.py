from letters import drawLetter

def drawWord(word, letter_pixels, x, y, size=20):
    for i, char in enumerate(word):
        if char == " ":
            continue
        drawLetter(letter_pixels[i], char, x + (i * 50), y, size)