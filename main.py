#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@fileName: main.py
@project: GomokuGame
@version: 1.0.2
@description: Implementation of a Gomoku (Five in a Row) game using Pygame.
The game allows two players (black and white) to take turns placing pieces on a 17*17 board.
The first player to achieve a consecutive line of five pieces wins the game.
@author: PythonDeveloper29042
@authorEmail: pythondeveloper.29042@outlook.com
@date: 2024/11/8
@github: https://github.com/PythonDeveloper29042/GomokuGame.git
"""

import pygame
import game

ROWS = 17
SIDE = 30

SCREEN_WIDTH = ROWS * SIDE  # Width of the screen
SCREEN_HEIGHT = ROWS * SIDE  # Height of the screen

EMPTY = -1
BLACK = (0, 0, 0)  # Color representing black pieces
WHITE = (255, 255, 255)  # Color representing white pieces
DIRE = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Directions for checking consecutive pieces


class Gomoku(game.Game):
    def __init__(self, title: str, size: tuple[int, int], fps: int = 15):
        """
        Initialize the Gomoku game with the specified title, size, and FPS.

        Args:
            title (str): The title of the game window.
            size (tuple[int, int]): The dimensions of the game window (width, height).
            fps (int, optional): Frames per second for game updates. Defaults to 15.
        """
        super(Gomoku, self).__init__(title, size, fps)
        self.board = [
            [EMPTY for _ in range(ROWS)] for _ in range(ROWS)
        ]  # Initialize board as a 2D list
        self.select = (-1, -1)
        self.black = True
        self.draw_board()
        self.bind_click(1, self.click)

    def click(self, x: int, y: int):
        """
        Handle click events for placing a piece on the board.

        Args:
            x (int): The x-coordinate of the click position.
            y (int): The y-coordinate of the click position.
        """
        if self.end:
            return
        i, j = y // SIDE, x // SIDE
        if self.board[i][j] != EMPTY:
            return
        self.board[i][j] = BLACK if self.black else WHITE
        self.draw_chess(self.board[i][j], i, j)
        self.black = not self.black

        chess = self.check_win()
        if chess:  # Check for victory condition
            self.end = True
            i, j = chess[0]
            winner = "Black" if self.board[i][j] == BLACK else "White"
            pygame.display.set_caption(f"Gomoku ---- {winner} won!")
            for c in chess:
                i, j = c
                self.draw_chess((100, 255, 255), i, j)  # Highlight the winning pieces
                self.timer.tick(5)

    def check_win(self) -> list[tuple[int, int]] | None:
        """
        Check if there is a winner by searching for five consecutive pieces.

        Returns:
            list[tuple[int, int]] | None: A list of coordinates forming the winning line, or None if no winner.
        """
        for i in range(ROWS):
            for j in range(ROWS):
                win = self.check_chess(i, j)
                if win:
                    return win
        return None

    def check_chess(self, i: int, j: int) -> list[tuple[int, int]] | None:
        """
        Check for consecutive pieces in all directions from the given position.

        Args:
            i (int): Row index of the piece.
            j (int): Column index of the piece.

        Returns:
            list[tuple[int, int]] | None: A list of coordinates forming a consecutive line if found, otherwise None.
        """
        if self.board[i][j] == EMPTY:
            return None
        color = self.board[i][j]
        for dire in DIRE:
            x, y = i, j
            chess = []
            while 0 <= x < ROWS and 0 <= y < ROWS and self.board[x][y] == color:
                chess.append((x, y))
                x, y = x + dire[0], y + dire[1]
            if len(chess) >= 5:
                return chess
        return None

    def draw_chess(self, color: tuple[int, int, int], i: int, j: int):
        """
        Draw a chess piece at the specified position on the board.

        Args:
            color (tuple[int, int, int]): RGB color of the piece.
            i (int): Row index for the piece.
            j (int): Column index for the piece.
        """
        center = (j * SIDE + SIDE // 2, i * SIDE + SIDE // 2)
        pygame.draw.circle(self.screen, color, center, SIDE // 2 - 2)
        pygame.display.update(pygame.Rect(j * SIDE, i * SIDE, SIDE, SIDE))

    def draw_board(self):
        """
        Draw the initial game board with grid lines and center point.
        """
        self.screen.fill((139, 87, 66))  # Fill background with brownish color
        for i in range(ROWS):
            start = (i * SIDE + SIDE // 2, SIDE // 2)
            end = (i * SIDE + SIDE // 2, ROWS * SIDE - SIDE // 2)
            pygame.draw.line(self.screen, 0x000000, start, end)  # Draw vertical lines
            start = (SIDE // 2, i * SIDE + SIDE // 2)
            end = (ROWS * SIDE - SIDE // 2, i * SIDE + SIDE // 2)
            pygame.draw.line(self.screen, 0x000000, start, end)  # Draw horizontal lines
        center = ((ROWS // 2) * SIDE + SIDE // 2, (ROWS // 2) * SIDE + SIDE // 2)
        pygame.draw.circle(self.screen, (0, 0, 0), center, 4)  # Draw center point
        pygame.display.update()


if __name__ == "__main__":
    print(
        "\nWelcome to the ultimate Gomoku match!!!\nLeft click any point of the board to start.\n"
    )  # Welcome message

    gomoku = Gomoku("Gomoku", (SCREEN_WIDTH, SCREEN_HEIGHT))
    gomoku.run()  # Run the game

# Create executable:
# pip install pyinstaller
# pyinstaller -F -w main.py
