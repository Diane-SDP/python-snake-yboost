# 🐍 Snake Game

Welcome to the Snake Game!

## 🎮 How to Play

1. **Objective**: Control the snake to eat apples and grow longer. Avoid colliding with the snake's own body.
2. **Controls**: The game uses a joystick to change the snake's direction.
3. **Game Over**: The game ends when the snake collides with itself. After that, you can upgrade the game by purchasing items in the marketplace.

## 🛒 MarketPlace

In the marketplace, you can buy 3 items:
1. Increase the value of an apple (initial value: 1)  
2. Increase the chance of getting a golden apple (initial chance: 0%)  
3. Buy a second life to use during the game  

You can also restart a game to collect more apples, or reset the entire game.

## 🛠️ Project Structure

- **`game.py`**: Contains the main game loop and logic for starting, restarting, and ending the game.
- **`snake.py`**: Defines the Snake class, which manages the snake's position, movement, and collision detection.
- **`apple.py`**: Manages the apple's position and checks if the snake has eaten an apple.
- **`ledboard.py`**: Handles the LED board display for the game.
- **`buzzer.py`**: Manages sound effects for the game.
- **`direction.py`**: Handles the direction changes for the snake.
- **`market.py`**: Manages the market place.

## 🚀 Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Diane-SDP/python-snake-yboost
   cd python-snake-yboost
   ```

2. **Run the Game**:
   Execute the `main.py` file to start the game. Ensure all dependencies are installed and configured.

3. **Requirements**:
   Make sure to have all necessary hardware and libraries set up, especially for the LED board.

## 📦 Requirements

### Hardware

- ESP-32 C3
- Led Matrix (8x8)
- Buzzer
- Joystick

### Software

- Python 3.*
- Neopixel : run ```pip install micropython-neopixel``` to install
- Thonny (or any other code editor that can implements the code on your ESP)

## Electrical diagram

[See the PDF file here](./img/Job1.PDF)
