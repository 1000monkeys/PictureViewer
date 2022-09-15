from xml.etree import ElementInclude
import pygame
import PIL.ExifTags

from PIL import Image
from helpers.UIElement import UIElement

class ImageClass(UIElement):
    def __init__(self, screen, file_name, main) -> None:
        self.screen = screen
        self.file_name = file_name
        self.main = main

        self.size = 240
        self.offset = 0
        self.smaller = False
        self.rect = pygame.Rect(-1000, -1000, 240, 240)

    def go_to_large_picture(self):
        self.image = self.full_image

    def load_image(self):
        try:
            self.full_image = pygame.image.load("images\\" + self.file_name)
            self.rect = pygame.Rect((-1000, -1000, 0, 0))

            im = Image.open("images\\" + self.file_name)
            if im._getexif() is not None:
                exif = {
                    PIL.ExifTags.TAGS[k]: v
                    for k, v in im._getexif().items()
                    if k in PIL.ExifTags.TAGS
                }
                #print(exif)
                
                if exif["Orientation"] == 7 or exif["Orientation"] == 8:
                    self.full_image = pygame.transform.rotate(self.full_image, 90)
                elif exif["Orientation"] == 3 or exif["Orientation"] == 4:
                    self.full_image = pygame.transform.rotate(self.full_image, 180)
                elif exif["Orientation"] == 5 or exif["Orientation"] == 6:
                    self.full_image = pygame.transform.rotate(self.full_image, 270)

                if exif["Orientation"] in [2, 4, 5, 7]:
                    self.full_image = pygame.transform.flip(self.full_image, True, False)

            x, y = self.full_image.get_size()
            rx = (self.size - 30) / x
            ry = (self.size - 30) / y
            ratio = rx if rx < ry else ry
            self.smaller_thumb = pygame.transform.scale(self.full_image, (int(x*ratio), int(y*ratio)))

            x, y = self.full_image.get_size()
            rx = self.size / x
            ry = self.size / y
            ratio = rx if rx < ry else ry
            self.full_thumb = pygame.transform.scale(self.full_image, (int(x*ratio), int(y*ratio)))

            self.image = self.full_thumb
        except FileNotFoundError or PermissionError:
            print("File Not Found/Permission Error!!")
            exit()

    def set_pos(self, pos):
        #if hasattr(self, "image"):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_offset(self, offset):
        self.offset = offset

    def get_rect(self) -> pygame.Rect:
        if hasattr(self, "image"):
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height())
        else:
            self.rect = pygame.Rect(self.rect.x, self.rect.y, 0, 0)
        self.updated_rect = pygame.Rect(self.rect.x, self.rect.y - self.offset, 240, 240)
        return self.rect
        
    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if hasattr(self, "smaller_thumb") and hasattr(self, "updated_rect") and self.updated_rect.collidepoint(event.pos):
                    self.image = self.smaller_thumb
                    
                    self.smaller = True
                    self.get_rect()
                elif hasattr(self, "full_thumb") and self.smaller:
                    self.image = self.full_thumb
                    
                    self.smaller = False
                    self.size = 240
                    self.get_rect()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.updated_rect.collidepoint(event.pos):
                    self.main.change_to_picture_view(self)

    def draw(self) -> None:
        """Empty draw needed because all screens need this method
        """
        if hasattr(self, "image"):
            if self.smaller:
                self.screen.blit(self.image, pygame.Rect(self.rect.x + ((self.size - self.get_rect().width) / 2), self.rect.y - self.offset + ((self.size - self.get_rect().height) / 2), self.rect.width, self.rect.height))
            else:
                self.screen.blit(self.image, pygame.Rect(self.rect.x + ((self.size - self.get_rect().width) / 2), self.rect.y - self.offset + ((self.size - self.get_rect().height) / 2), self.rect.width, self.rect.height))
        else:
            self.load_image()
