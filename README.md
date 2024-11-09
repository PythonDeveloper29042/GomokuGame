# Gomoku Game

Welcome to Gomoku, a two-player game where the objective is to place five consecutive pieces of the same color (either black or white) on a 17x17 board. This project uses Pygame to create an interactive and engaging experience.

## Features
- 17x17 grid-based game board.
- Two-player turn-based gameplay (black and white pieces).
- Automatic victory detection for five consecutive pieces in any direction.
- Visual highlight for the winning sequence.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Pygame library**

To install Pygame, use:  

(Windows)
```
pip install pygame
```
(macOS/Linux)
```
pip3 install pygame
```

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/PythonDeveloper29042/GomokuGame.git
   ```
2. Navigate to the project directory:
   ```
   cd GomokuGame
   ```
3. Run the game:
   ```
   python main.py
   ```

### Creating an Executable (Optional)
You can create a standalone executable using `pyinstaller`:

```
pip install pyinstaller
pyinstaller -F -w main.py
```

This will generate an executable in the `dist` directory.

Replace `pip` with `pip3` if you are using macOS and Linux.

## Game Instructions

1. **Objective**: Place five consecutive pieces (horizontal, vertical, or diagonal) to win.
2. **Controls**: Use the left mouse button to place pieces on the board.
3. **Winning Condition**: The game displays a winning message and highlights the winning sequence when a player achieves five consecutive pieces.

## Code Structure

- **`main.py`**: Contains the main game logic, board drawing, piece placement, and win-checking mechanisms.
- **`game.py`**: Base game class that manages Pygame setup and essential functionalities.

## Class Overview

### `Gomoku`
Inherits from `game.Game` and includes:
- `click(x: int, y: int)`: Handles piece placement and turn changes.
- `check_win() -> list[tuple[int, int]] | None`: Checks the board for a winning sequence.
- `check_chess(i: int, j: int) -> list[tuple[int, int]] | None`: Checks consecutive pieces in specified directions.
- `draw_chess(color: tuple[int, int, int], i: int, j: int)`: Draws pieces at specified board positions.
- `draw_board()`: Initializes the board with grid lines and center point.

## Customization

You can modify the `ROWS` and `SIDE` constants in `main.py` to change the board size and grid spacing.

## Credits

- **Author**: PythonDeveloper29042
- **Contact**: [pythondeveloper.29042@outlook.com](mailto:pythondeveloper.29042@outlook.com)

