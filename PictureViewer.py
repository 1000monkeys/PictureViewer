
from email.mime import image
from genericpath import isfile
import math
from ntpath import join
from os import listdir
import pygame
from helpers.ImageClass import ImageClass

from helpers.Screen import Screen
from helpers.ScrollBar import ScrollBar

class PictureViewer(Screen):
    def __init__(self):
        pygame.init()

        self.screen_width = 265
        self.screen_height = 786
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("Picture Viewer")

    def handle_events(self, events):
        super().handle_events(events)

    def run(self):
        #mypath = "images"
        #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        #for file in onlyfiles:
        #    super().add_item(ImageClass(self.screen, file))

        #Landscape
        super().add_item(ImageClass(self.screen, "Landscape_0.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_1.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_2.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_3.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_4.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_5.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_6.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_7.jpg"))
        super().add_item(ImageClass(self.screen, "Landscape_8.jpg"))
        
        #Portrait
        super().add_item(ImageClass(self.screen, "Portrait_0.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_1.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_2.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_3.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_4.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_5.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_6.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_7.jpg"))
        super().add_item(ImageClass(self.screen, "Portrait_8.jpg"))

        self.scrollbar = ScrollBar(self.screen, super())

        while True:
            pygame.time.Clock().tick(30)

            self.screen.fill((0, 0, 0))

            #print("Width: " + str(self.amount_width) + " Height: " + str(self.amount_height))

            percentage_scrolled = self.scrollbar.get_percentage_scrolled()
            size = self.scrollbar.get_size()
            offset_height = ((size.height + size.y) / 100 * percentage_scrolled) - (self.screen.get_height() / 100 * percentage_scrolled)

            #print(offset_height)

            super().set_offset(offset_height)
            events = pygame.event.get()
            super().handle_events(events)
            super().draw()
            
            self.scrollbar.calculate_size()
            self.scrollbar.handle_events(events)
            self.scrollbar.draw()

            images = list()
            for item in super().get_items():
                if isinstance(item, ImageClass):
                    images.append(item)

            self.amount_width = 1
            self.amount_height = 18
            for row in range(0, 18):
                for column in range(0, 1):
                    if len(images) > column + row * self.amount_width:
                        #print("id: " + str(column + (row * self.amount_width)) + " Width: " + str(column) + " Height: " + str(row))
                        #print(images[column + row * self.amount_width].get_rect())
                        images[column + row * self.amount_width].set_pos((column * 240, (row * 240)))
                        images[column + row * self.amount_width].set_offset(offset_height)

            pygame.display.flip()


pictureViewer = PictureViewer()
pictureViewer.run()
