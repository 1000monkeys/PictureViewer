import gc
from xml.etree import ElementInclude
import pygame

from PIL import Image
from helpers.UIElement import UIElement
from helpers.loader import Loader

class ImageClass(UIElement):
    def __init__(self, screen, file_name, main) -> None:
        self.screen = screen
        self.file_name = file_name
        self.main = main

        self.offset = 0
        self.image_str = "large_thumb"
        self.rect = pygame.Rect(-1000, -1000, 240, 240)

    def load_images(self):
        self.loader = Loader(self.screen, self.file_name);
        self.loader.start()

    def go_to_large_picture(self):
        self.image = self.images["full"]

    def set_pos(self, pos):
        #if hasattr(self, "image"):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_offset(self, offset):
        self.offset = offset

    def get_rect(self) -> pygame.Rect:
        if hasattr(self, "images"):
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.images[self.image_str].get_width(), self.images[self.image_str].get_height()) 
            self.updated_rect = pygame.Rect(self.rect.x, self.rect.y - self.offset, 240, 240)
        
        return self.rect

    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if hasattr(self, "images") and hasattr(self, "updated_rect") and + \
                    (self.updated_rect.collidepoint(event.pos) or self.updated_rect.collidepoint(pygame.mouse.get_pos())):
                    self.image_str = "small_thumb"
                elif hasattr(self, "images") and self.image_str == "small_thumb":
                    self.image_str = "large_thumb"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hasattr(self, "updated_rect") and self.updated_rect.collidepoint(event.pos):
                    if not self.main.fade_out and not self.main.fade_in:
                        self.main.change_to_picture_view(self)

    def draw(self) -> None:
        """Empty draw needed because all screens need this method
        """
        if hasattr(self, "loader"):
            if not hasattr(self, "images") and hasattr(self.loader, "images"):
                self.images = self.loader.images

                self.loader.dispose()
                del self.loader
                gc.collect()

            if hasattr(self, "updated_rect") and hasattr(self, "images"):
                rect = self.updated_rect
                self.screen.blit(self.images[self.image_str], pygame.Rect(rect.x + ((240 - self.get_rect().width) / 2), rect.y + ((240 - self.get_rect().height) / 2), self.images[self.image_str].get_width(), self.images[self.image_str].get_height()))
        else:
            self.load_images();
