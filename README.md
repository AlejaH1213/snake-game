# Snake Game

This classic Snake Game is implemented in Python using the Turtle graphics library. Navigate the snake around the screen, collecting food to grow larger. Each piece of food the snake eats increases its length and your score. The game ends if the snake collides with itself or the wall.

## Features

- **Simple Controls:** Use the arrow keys (Up, Down, Left, Right) to change the direction of the snake.
- **Scoring System:** Your score increases by one point each time the snake eats a piece of food.
- **Dynamic Speed:** The game's speed increases slightly each time the snake eats food, making it progressively more challenging.
- **Customizable Appearance:** The game's code allows for easy customization of the snake and background colors.

## Game Elements

### Screen
The game window where all the action takes place. It is set up at the beginning of the game with a specified width, height, and background color.

### Snake
The main character of the game, controlled by the player. The snake starts with a small size and grows each time it eats food.

### Food
Randomly placed items on the screen that the snake eats to grow larger. Each piece of food eaten increases the player's score.

### Score
Displayed at the top of the game window, the score represents how many pieces of food the snake has eaten. The game becomes faster as the score increases.

### Border
A red border drawn around the edge of the game window. If the snake touches the border, the game ends.

### Movement and Control
The snake's movement is controlled using the arrow keys. The game ensures that the snake cannot immediately reverse direction.

### Game Over
The game ends when the snake collides with itself or the border. At game over, the final score is displayed.

## How to Play

1. Start the game by running the Python script.
2. Use the arrow keys to navigate the snake towards the food.
3. Avoid colliding with the snake's tail or the border.
4. Try to eat as much food as possible to increase your score.

## Customization

The game's appearance can be easily customized by changing the color settings for the snake and the background within the script.

## Requirements

- Python 3.x
- Turtle Graphics Library (should be included with Python)

## Running the Game

To run the game, navigate to the directory containing the game's script and execute the following command:

```bash
python snake_game.py

