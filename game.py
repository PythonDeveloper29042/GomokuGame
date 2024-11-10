#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@fileName: game.py
@project: GomokuGame
@description: Provides a base Game class with functionality for keyboard and mouse events, pause, fullscreen mode, and score display.
Includes a Test class as an example for basic game setup.
@author: Pythondeveloper29042
@authorEmail: pythondeveloper.29042@outlook.com
@commitDate: 2024/11/10
@github: https://github.com/PythonDeveloper29042/GomokuGame.git
"""

import pygame
from pygame.locals import *
from sys import exit
from typing import Callable, Optional, Tuple

# Define four-neighbor and eight-neighbor directions for movement
FOUR_NEIGH = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}
EIGHT_NEIGH = list(FOUR_NEIGH.values()) + [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define keyboard direction mapping
DIRECTION = {
    pygame.K_UP: "up",
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
    pygame.K_DOWN: "down",
}


def hex2rgb(color: int) -> Tuple[int, int, int]:
    """
    Convert a hexadecimal color to an RGB tuple.

    Args:
        color (int): The color in hexadecimal format.

    Returns:
        Tuple[int, int, int]: The corresponding RGB color.
    """
    b = color % 256
    color = color >> 8
    g = color % 256
    color = color >> 8
    r = color % 256
    return (r, g, b)


class Game:
    def __init__(self, title: str, size: Tuple[int, int], fps: int = 30):
        """
        Initialize the Game class with title, window size, and frame rate.

        Args:
            title (str): The title of the game window.
            size (Tuple[int, int]): The dimensions of the window (width, height).
            fps (int, optional): Frames per second for game updates. Defaults to 30.
        """
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size, 0, 32)
        pygame.display.set_caption(title)
        self.keys = {}
        self.keys_up = {}
        self.clicks = {}
        self.timer = pygame.time.Clock()
        self.fps = fps
        self.score = 0
        self.end = False
        self.fullscreen = False
        self.last_time = pygame.time.get_ticks()
        self.is_pause = False
        self.is_draw = True
        self.score_font = pygame.font.SysFont("Calibri", 130, True)

    def bind_key(self, key: int | list[int], action: Callable[[int], None]):
        """
        Bind a function to a key press event.

        Args:
            key (int | list[int]): A single key or list of keys to bind.
            action (Callable[[int], None]): Function to call when the key is pressed.
        """
        if isinstance(key, list):
            for k in key:
                self.keys[k] = action
        elif isinstance(key, int):
            self.keys[key] = action

    def bind_key_up(self, key: int | list[int], action: Callable[[int], None]):
        """
        Bind a function to a key release event.

        Args:
            key (int | list[int]): A single key or list of keys to bind.
            action (Callable[[int], None]): Function to call when the key is released.
        """
        if isinstance(key, list):
            for k in key:
                self.keys_up[k] = action
        elif isinstance(key, int):
            self.keys_up[key] = action

    def bind_click(self, button: int, action: Callable[[int, int], None]):
        """
        Bind a function to a mouse button click event.

        Args:
            button (int): The mouse button to bind (1 for left-click, etc.).
            action (Callable[[int, int], None]): Function to call with (x, y) on click.
        """
        self.clicks[button] = action

    def pause(self, key: int):
        """
        Toggle the game's pause state.

        Args:
            key (int): The key triggering the pause action.
        """
        self.is_pause = not self.is_pause

    def set_fps(self, fps: int):
        """
        Set the game's frames per second.

        Args:
            fps (int): Desired frames per second.
        """
        self.fps = fps

    def handle_input(self, event: pygame.event.Event):
        """
        Handle user input for key and mouse events.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in self.keys.keys():
                self.keys[event.key](event.key)
            if event.key == pygame.K_F11:  # F11 for fullscreen
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.screen = pygame.display.set_mode(
                        self.size, pygame.FULLSCREEN, 32
                    )
                else:
                    self.screen = pygame.display.set_mode(self.size, 0, 32)
        if event.type == pygame.KEYUP:
            if event.key in self.keys_up.keys():
                self.keys_up[event.key](event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in self.clicks.keys():
                self.clicks[event.button](*event.pos)

    def run(self):
        """Main game loop, handling events, updates, and drawing."""
        while True:
            for event in pygame.event.get():
                self.handle_input(event)
            self.timer.tick(self.fps)

            self.update(pygame.time.get_ticks())
            self.draw(pygame.time.get_ticks())

    def draw_score(
        self, color: Tuple[int, int, int], rect: Optional[pygame.Rect] = None
    ):
        """
        Draw the game score on the screen.

        Args:
            color (Tuple[int, int, int]): Color for the score text.
            rect (Optional[pygame.Rect], optional): Positioning rectangle. Defaults to None.
        """
        score = self.score_font.render(str(self.score), True, color)
        if rect is None:
            r = self.screen.get_rect()
            rect = score.get_rect(center=r.center)
        self.screen.blit(score, rect)

    def is_end(self) -> bool:
        """Check if the game has ended.

        Returns:
            bool: True if the game has ended, otherwise False.
        """
        return self.end

    def update(self, current_time: int):
        """
        Update game state. Override this in subclasses for game-specific logic.

        Args:
            current_time (int): Current time in milliseconds.
        """
        pass

    def draw(self, current_time: int):
        """
        Draw game elements. Override this in subclasses for game-specific visuals.

        Args:
            current_time (int): Current time in milliseconds.
        """
        pass


class Test(Game):
    def __init__(self, title: str, size: Tuple[int, int], fps: int = 30):
        """
        Initialize Test game with specific title, window size, and frame rate.

        Args:
            title (str): The title of the game window.
            size (Tuple[int, int]): The dimensions of the window (width, height).
            fps (int, optional): Frames per second for game updates. Defaults to 30.
        """
        super(Test, self).__init__(title, size, fps)
        self.bind_key(pygame.K_RETURN, self.press_enter)

    def press_enter(self):
        """Handle the Enter key press event."""
        print("press enter")

    def draw(self, current_time: int):
        """Draw game elements for the Test game."""
        pass


def press_space(key: int):
    """Handle the Space key press event."""
    print("press space.")


def click(x: int, y: int):
    """Handle a mouse click event by printing the clicked coordinates."""
    print(x, y)


def main():
    """
    Main function to initialize and run a Test game instance.
    Includes example key and click bindings.
    """
    print(hex2rgb(0x012456))
    game = Test("game", (640, 480))
    game.bind_key(pygame.K_SPACE, press_space)
    game.bind_click(1, click)
    game.run()


if __name__ == "__main__":
    main()

# To create an executable, run the following command in the terminal:
# pyinstaller -F -w game.py
