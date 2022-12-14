import math
import gc
import pygame

from helpers.ImageClass import ImageClass
from helpers.ScrollBar import ScrollBar
from helpers.UIElement import UIElement

class GalleryScreen(UIElement):
    def __init__(self, screen, screen_size) -> None:
        self.screen = screen
        self.screen_size = screen_size

        self.scrollbar = ScrollBar(self.screen, self)
        self.images = list()
        self.del_count = 0

    def handle_events(self, events) -> None:
        self.scrollbar.handle_events(events)
        for image in self.images:
            image.handle_events(events)

    def get_rect(self) -> pygame.Rect:
        return super().get_rect()

    def add_item(self, item):
        if not hasattr(self, 'items'):
            self.items = list()
        self.items.append(item)

        if isinstance(item, ImageClass):
            self.images.append(item)

    def get_item(self, pos):
        if not hasattr(self, 'items'):
            self.items = list()
        if len(self.items) > pos:
            return self.items[pos]
        else:
            print("Index non existant!!")
            exit()

    def get_items(self):
        if not hasattr(self, 'items'):
            self.items = list()
        return self.items

    def draw(self) -> None:
        """Empty draw needed because all screens need this method
        """
        gc.collect()

        offset = self.scrollbar.get_offset();
        self.amount_width = math.floor(self.screen_size[0] / 240)
        for column in range(0, self.amount_width):
            for row in range(0, math.ceil(len(self.images) / self.amount_width)):
                if len(self.images) > column + row * self.amount_width:
                    #print("id: " + str(column + (row * self.amount_width)) + " Width: " + str(column) + " Height: " + str(row))
                    #print(images[column + row * self.amount_width].get_rect())
                    pos = (column * 240, row * 240)
                    #print(pos)
                    self.images[column + row * self.amount_width].set_pos(pos)
                    self.images[column + row * self.amount_width].set_offset(offset)

        count = 0
        events = pygame.event.get()
        for image in self.images:
            rect = image.get_rect()
            #print("Rectx" + str(rect.x + offset) + " out " + str(self.screen_size[0] + offset))
            if rect.x < self.screen_size[0] + offset and rect.x + rect.height > -1 and rect.y + rect.width > offset - 240 and rect.y < self.screen_size[1] + offset:
                #print("Drawing: " + str(count))
                count = count + 1
                image.handle_events(events)
                image.draw()
            else:
                if hasattr(image, "images"):
                    print("deleting: " + str(self.del_count) + "!")
                    del image.images
                    gc.collect()
                    self.del_count = self.del_count + 1

        self.scrollbar.calculate_size()
        self.scrollbar.draw()