import pygame
import PIL.ExifTags

from PIL import Image
from helpers.UIElement import UIElement

class ImageClass(UIElement):
    def __init__(self, screen, file_name) -> None:
        self.screen = screen
        self.file_name = file_name

        self.offset = 0

        try:
            self.image = pygame.image.load("images\\" + self.file_name)
            
            x, y = self.image.get_size()
            rx = 240 / x
            ry = 240 / y
            ratio = rx if rx < ry else ry

            self.rect = pygame.Rect((-1000, -1000, int(x*ratio), int(y*ratio)))
            self.image = pygame.transform.scale(self.image, (int(x*ratio), int(y*ratio)))

            im = Image.open("images\\" + self.file_name)
            if im._getexif() is not None:
                exif = {
                    PIL.ExifTags.TAGS[k]: v
                    for k, v in im._getexif().items()
                    if k in PIL.ExifTags.TAGS
                }
                #print(exif)
                
                if exif["Orientation"] == 7 or exif["Orientation"] == 8:
                    self.image = pygame.transform.rotate(self.image, 90)
                elif exif["Orientation"] == 3 or exif["Orientation"] == 4:
                    self.image = pygame.transform.rotate(self.image, 180)
                elif exif["Orientation"] == 5 or exif["Orientation"] == 6:
                    self.image = pygame.transform.rotate(self.image, 270)

                if exif["Orientation"] in [2, 4, 5, 7]:
                    self.image = pygame.transform.flip(self.image, True, False)
        except FileNotFoundError or PermissionError:
            print("File Not Found/Permission Error!!")
            exit()

    def set_pos(self, pos):
        if hasattr(self, "image"):
            self.rect.x = pos[0]
            self.rect.y = pos[1]

    def set_offset(self, offset):
        self.offset = offset

    def get_rect(self) -> pygame.Rect:
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height())
        return self.rect
        
    def handle_events(self, events) -> None:
        pass

    def draw(self) -> None:
        """Empty draw needed because all screens need this method
        """
        if hasattr(self, "image"):
            self.screen.blit(self.image, pygame.Rect(self.rect.x + ((240 - self.get_rect().width) / 2), self.rect.y - self.offset + ((240 - self.get_rect().height) / 2), self.rect.width, self.rect.height))
        else:
            pass
