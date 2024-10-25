# Escape the Maze Game

Escape the Maze is a simple Python game where the player navigates through a randomly generated maze, collects items, avoids traps, and tries to reach the exit. The game is built using the `pygame` library, which provides functionalities for creating games and multimedia applications.

## Table of Contents
1. [Game Description](#game-description)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [How to Play](#how-to-play)
7. [Code Overview](#code-overview)
8. [Future Enhancements](#future-enhancements)

## Game Description
In Escape the Maze, the player starts at the top-left corner of a randomly generated maze and must reach the bottom-right corner to win. Along the way, the player can collect items to increase their score and must avoid traps that will reduce their score. The maze is generated using a procedural algorithm, ensuring a different layout each time the game is played.

## Features
- Randomly generated maze for each playthrough.
- Player movement using arrow keys.
- Collectible items that increase the player's score.
- Traps that decrease the player's score when triggered.
- Exit condition where the player wins upon reaching the maze's end.
- Visual representation of walls, items, traps, player, and exit using simple graphics.

## Technologies Used
- **Python 3**: The programming language used to write the game.
- **Pygame**: A Python library used for game development, which handles graphics rendering, event handling, and game loop management.

## Prerequisites
To run the game, you'll need:
- Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).
- `pygame` library. If you don't have it installed, you can install it via `pip` (Python's package installer).

## Installation
1. **Clone the repository or download the source code**:
    ```bash
    git clone https://github.com/your-username/escape-the-maze.git
    cd escape-the-maze
    ```

2. **Install Pygame**:
    If `pygame` is not already installed, you can install it using:
    ```bash
    pip install pygame
    ```

3. **Run the game**:
    Start the game by running the following command:
    ```bash
    python escape_the_maze.py
    ```

## How to Play
- Use the arrow keys (`UP`, `DOWN`, `LEFT`, `RIGHT`) to navigate the maze.
- Collect green items to increase your score by 10 points each.
- Avoid red traps, as hitting one will reduce your score by 5 points.
- Reach the white exit square located at the bottom-right corner of the maze to win.
- The game ends when the player reaches the exit, with the final score displayed in the console.

## Code Overview
The game consists of the following main components:

1. **Maze Generation**:
   - The maze is generated using a Depth-First Search (DFS) algorithm, which creates a perfect maze with one solution path.
   - Walls are represented by `1` and paths by `0`, forming a grid-like structure.

2. **Player Class**:
   - Handles player movement and interactions.
   - Player can move in four directions (up, down, left, right), collect items, and trigger traps.
   - The player's score is tracked based on interactions with items and traps.

3. **Object Placement**:
   - Items and traps are randomly placed in the maze, ensuring they do not overlap and are not located at the player's starting position.

4. **Game Loop**:
   - The game runs continuously, processing player input, updating the game state, and rendering the graphics until the player wins or quits.
   - The frame rate is controlled using `pygame.time.Clock()` to ensure smooth gameplay.

5. **Rendering**:
   - The `pygame` library is used to draw the maze, player, items, traps, and exit on the screen.
   - Each entity (walls, player, items, etc.) is represented by a colored square for simplicity.

## Future Enhancements
- **Add multiple levels**: Implement different levels with increasing maze complexity.
- **Introduce time-based scoring**: Include a timer that affects the final score based on how quickly the maze is solved.
- **Add sound effects**: Play sounds for collecting items, hitting traps, and winning the game.
- **Implement more challenging obstacles**: Add moving enemies, locked doors, and keys.
- **Create a main menu**: Include options for starting the game, viewing instructions, and exiting.



