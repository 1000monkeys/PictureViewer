import sys
import pygame
from helpers.UIElement import UIElement


class Screen(UIElement):
    def __init__(self) -> None:
        pass

    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    def get_rect(self) -> pygame.Rect:
        pass
