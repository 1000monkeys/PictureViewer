from tkinter import Button
import pygame
from helpers.UIElement import UIElement

class ScrollBar(UIElement):
    def __init__(self, screen, gallery_screen) -> None:
        self.screen = screen
        self.gallery_screen = gallery_screen

        self.screen_size = (self.screen.get_width(), self.screen.get_height())
        
        width = self.screen.get_width()
        height = self.screen.get_height()
        
        self.size_rect = pygame.Rect(0, 0, 0, 0)

        self.button_rect = pygame.Rect(width - 25, 2, 25, 50)
        self.bar_rect = pygame.Rect(width - 25, 0, 25, height)

        self.percentage_scrolled = 0
        self.dragging = False

    def get_offset(self):
        percentage_scrolled = self.get_percentage_scrolled()
        size = self.get_size()
        #print(size)
        offset_height = ((size.height + size.y) / 100 * percentage_scrolled) - (self.screen.get_height() / 100 * percentage_scrolled)
        return offset_height

    def draw(self) -> None:
        width = self.screen.get_width()
        height = self.screen.get_height()

        self.bar_rect = pygame.Rect(width - 25, 0, 25, height)
        pygame.draw.rect(self.screen, (255, 255, 255), self.bar_rect)

        self.button_rect = pygame.Rect(width - 23, self.button_rect.y, 21, 50)
        pygame.draw.rect(self.screen, (125, 125, 125), self.button_rect)

    def get_rect(self) -> pygame.Rect:
        return self.size_rect

    def get_percentage_scrolled(self):
        return self.percentage_scrolled

    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.dragging = True
                elif self.bar_rect.collidepoint(event.pos):
                    self.button_rect.y = event.pos[1] - 25
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.button_rect.collidepoint(event.pos):
                    self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging and self.bar_rect.collidepoint(event.pos):
                    self.button_rect.y = event.pos[1] - 25
                elif not self.button_rect.collidepoint(event.pos):
                    self.dragging = False
                if self.dragging:
                    self.button_rect.y = event.pos[1] - 25

        percentage_scrolled = (self.button_rect.y - 2) / ((self.screen.get_height() - 54) / 100)
        if percentage_scrolled > 100:
            percentage_scrolled = 100
        elif percentage_scrolled < 0:
            percentage_scrolled = 0
        self.percentage_scrolled = percentage_scrolled

        if self.button_rect.y < 2:
            self.button_rect.y = 2
        elif self.button_rect.y > self.screen.get_height() - 52:
            self.button_rect.y = self.screen.get_height() - 52
        #print(self.percentage_scrolled)

    def get_size(self):
        return self.size_rect

    def calculate_size(self):
        items = self.gallery_screen.get_items()
        
        size_dict = dict()
        size_dict[0] = 0
        size_dict[1] = 0
        size_dict[2] = 0
        size_dict[3] = 0

        for item in items:
            if item.get_rect()[0] > size_dict[0]:
                size_dict[0] = item.get_rect()[0]
            if item.get_rect()[1] > size_dict[1]:
                size_dict[1] = item.get_rect()[1]

            if item.get_rect()[2] > size_dict[2]:
                size_dict[2] = item.get_rect()[2]
            if item.get_rect()[3] > size_dict[3]:
                size_dict[3] = item.get_rect()[3]
        
        #print("canvas size: " + str(size_dict))
        self.size_rect = pygame.Rect(size_dict[0], size_dict[1], size_dict[2], size_dict[3])
            