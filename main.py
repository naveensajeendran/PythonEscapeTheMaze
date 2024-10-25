import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480  # Screen width and height
TILE_SIZE = 32            # Size of each tile in the maze
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE  # Number of rows and columns in the maze

# Colors for the game
WHITE = (255, 255, 255)  # Wall color
BLACK = (0, 0, 0)        # Background color
RED = (255, 0, 0)        # Trap color
GREEN = (0, 255, 0)      # Item color
BLUE = (0, 0, 255)       # Player color

# Game settings
FPS = 60  # Frames per second

# Initialize the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Maze")  # Window title
clock = pygame.time.Clock()  # Clock to control frame rate

# Create basic images for the player, items, traps, and exit
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill(BLUE)  # Player is represented by a blue square
item_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
item_image.fill(GREEN)   # Items are represented by green squares
trap_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
trap_image.fill(RED)     # Traps are represented by red squares
exit_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
exit_image.fill(WHITE)   # Exit is represented by a white square

# Maze generation using Depth-First Search algorithm
def generate_maze(rows, cols):
    # Initialize the maze grid with walls (1s)
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    stack = [(1, 1)]  # Stack for backtracking, starting from position (1, 1)
    maze[1][1] = 0    # Mark the starting point as a path (0)

    # Perform depth-first search to carve out a maze
    while stack:
        current = stack[-1]  # Get the current position
        r, c = current
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]  # Possible directions to move (up, down, left, right)
        random.shuffle(directions)  # Randomize direction order

        found = False
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            # Check if the new position is within maze boundaries and is a wall
            if 1 <= new_r < rows-1 and 1 <= new_c < cols-1 and maze[new_r][new_c] == 1:
                maze[new_r][new_c] = 0  # Mark the new cell as a path
                maze[r + dr//2][c + dc//2] = 0  # Also mark the wall in between as a path
                stack.append((new_r, new_c))  # Push the new position to the stack
                found = True
                break
        if not found:
            stack.pop()  # If no unvisited neighbors, backtrack

    return maze

# Function to randomly place items and traps in the maze
def place_objects(maze, num_items, num_traps):
    items = []
    traps = []
    rows = len(maze)
    cols = len(maze[0])

    # Place items randomly in the maze
    for _ in range(num_items):
        while True:
            r = random.randint(1, rows-2)
            c = random.randint(1, cols-2)
            # Ensure the cell is a path, not already occupied, and not the starting position
            if maze[r][c] == 0 and (r, c) not in items and (r, c) != (1, 1):
                items.append((r, c))
                break

    # Place traps randomly in the maze
    for _ in range(num_traps):
        while True:
            r = random.randint(1, rows-2)
            c = random.randint(1, cols-2)
            # Ensure the cell is a path, not already occupied, and not the starting position
            if maze[r][c] == 0 and (r, c) not in traps and (r, c) != (1, 1):
                traps.append((r, c))
                break

    return items, traps

# Player class to handle player movement and interactions
class Player:
    def __init__(self, x, y):
        self.x = x  # Player's x position (column)
        self.y = y  # Player's y position (row)
        self.score = 0  # Player's score

    # Move the player in the maze
    def move(self, dx, dy, maze):
        new_x, new_y = self.x + dx, self.y + dy
        # Check if the new position is within maze boundaries and is a path
        if 0 <= new_x < COLS and 0 <= new_y < ROWS and maze[new_y][new_x] == 0:
            self.x = new_x
            self.y = new_y

    # Check if the player is on an item and collect it
    def collect_item(self, items):
        if (self.y, self.x) in items:
            items.remove((self.y, self.x))  # Remove the collected item
            self.score += 10  # Increase score

    # Check if the player hit a trap
    def hit_trap(self, traps):
        if (self.y, self.x) in traps:
            traps.remove((self.y, self.x))  # Remove the triggered trap
            self.score -= 5  # Decrease score

# Initialize game settings
maze = generate_maze(ROWS, COLS)  # Generate the maze
items, traps = place_objects(maze, 5, 3)  # Place 5 items and 3 traps
player = Player(1, 1)  # Initialize player at the start
exit_position = (ROWS-2, COLS-2)  # Exit is at the bottom-right corner

# Game loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen with black

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit the game

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0, maze)  # Move left
    if keys[pygame.K_RIGHT]:
        player.move(1, 0, maze)   # Move right
    if keys[pygame.K_UP]:
        player.move(0, -1, maze)  # Move up
    if keys[pygame.K_DOWN]:
        player.move(0, 1, maze)   # Move down

    # Check for item collection
    player.collect_item(items)

    # Check for trap collision
    player.hit_trap(traps)

    # Check for winning condition
    if (player.y, player.x) == exit_position:
        print(f"You escaped the maze! Final Score: {player.score}")
        running = False

    # Draw the maze
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw items
    for item in items:
        screen.blit(item_image, (item[1] * TILE_SIZE, item[0] * TILE_SIZE))

    # Draw traps
    for trap in traps:
        screen.blit(trap_image, (trap[1] * TILE_SIZE, trap[0] * TILE_SIZE))

    # Draw exit
    screen.blit(exit_image, (exit_position[1] * TILE_SIZE, exit_position[0] * TILE_SIZE))

    # Draw player
    screen.blit(player_image, (player.x * TILE_SIZE, player.y * TILE_SIZE))

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(FPS)

# Quit pygame
pygame.quit()
