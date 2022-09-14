import sys

import pygame

class Screen:
    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        
    def add_item(self, item):
        if not hasattr(self, 'items'):
            self.items = list()
        self.items.append(item)

    def get_item(self, pos):
        if not hasattr(self, 'items'):
            self.items = list()
        return self.items[pos]

    def get_items(self):
        if not hasattr(self, 'items'):
            self.items = list()
        return self.items

    def set_offset(self, offset):
        self.offset = offset

    def draw(self) -> None:
        """Empty draw needed because all screens need this method
        """
        events = pygame.event.get()

        window_size = pygame.display.get_window_size()
        
        if not hasattr(self, 'items'):
            self.items = list()

        for item in self.items:
            rect = item.get_rect()
            if rect.x < window_size[0] + self.offset and rect.x + rect.height > -1 and rect.y + rect.width > -1 and rect.y < window_size[1] + self.offset:
                item.handle_events(events)
                item.draw()
