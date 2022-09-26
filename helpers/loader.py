import os
import pygame
from threading import Thread
from PIL import Image
import PIL.ExifTags
from urllib.parse import urlparse


class Loader(Thread):
    def __init__(self, screen, file_url) -> None:
        super().__init__()
        self.screen = screen
        self.file_url = file_url

        self.file_name = os.path.basename(urlparse(self.file_url).path)
        self.size = 240

        if not os.path.isdir("images"):
            os.mkdir(os.getcwd() + "/images")

    def dispose(self):
        del self.full_image
        del self.info_image
        del self.small_thumb
        del self.large_thumb

        del self.images

        del self.file_name
        del self.size
        del self.file_url

    def run(self):
        full_image = pygame.image.load("images\\" + self.file_name)
        info_image = Image.open("images\\" + self.file_name)

        try:
            self.full_image = pygame.image.load("images\\" + self.file_name)

            self.info_image = Image.open("images\\" + self.file_name)
            if self.info_image._getexif() is not None:
                exif = {
                    PIL.ExifTags.TAGS[k]: v
                    for k, v in self.info_image._getexif().items()
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
            self.small_thumb = pygame.transform.scale(self.full_image, (int(x*ratio), int(y*ratio)))

            x, y = self.full_image.get_size()
            rx = self.size / x
            ry = self.size / y
            ratio = rx if rx < ry else ry
            self.large_thumb = pygame.transform.scale(self.full_image, (int(x*ratio), int(y*ratio)))

            self.image = self.large_thumb
 
            self.images = {"info": info_image, "full": full_image, "small_thumb": self.small_thumb, "large_thumb": self.large_thumb}
        except FileNotFoundError or PermissionError:
            print("File Not Found/Permission Error!!")
            exit()