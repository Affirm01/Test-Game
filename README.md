# Snake Game

A classic Snake game built with Python's `turtle` module as a hands-on way to learn game logic, collision detection, and modular code design.

## How to Play

Run `game.py` to start.

| Key | Action |
|-----|--------|
| `W` / `↑` | Move up |
| `S` / `↓` | Move down |
| `A` / `←` | Move left |
| `D` / `→` | Move right |
| `R` | Restart (after game over) |
| `Q` | Quit (after game over) |

## Features

- Checkered play field with a border
- Score and persistent high score display
- Custom pixel-font rendering for all on-screen text and numbers
- Game over screen with restart and quit prompts

## Project Structure

| File | Purpose |
|------|---------|
| `game.py` | Entry point — keyboard bindings and game start |
| `main.py` | Main game loop |
| `setup.py` | Screen, snake, food, and UI turtle setup |
| `movement.py` | Snake direction and movement logic |
| `colliders.py` | Border, fruit, and self-collision detection |
| `score.py` | Score and high score state |
| `words.py` | Renders words using the pixel-letter system |
| `letters.py` | Pixel-art letter definitions |
| `numbers.py` | Pixel-art number definitions |

## Requirements

- Python 3.x (standard library only — no installs needed)
