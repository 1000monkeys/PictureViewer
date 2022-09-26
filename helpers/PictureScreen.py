import pygame

from helpers.UIElement import UIElement

class PictureScreen(UIElement):
    def __init__(self, screen, main) -> None:
        self.screen = screen
        self.main = main

        pygame.font.init()
        my_font = pygame.font.SysFont('Arial', 24)
        self.text = my_font.render('X', False, (0, 0, 0))

    def set_picture(self, image_class):
        self.image_class = image_class
        self.image = self.image_class.images["full"]

        x, y = self.image.get_size()
        rx = 1024 / x
        ry = 768 / y
        ratio = rx if rx < ry else ry

        self.image = pygame.transform.scale(self.image, (int(x*ratio), int(y*ratio)))
        self.background_rect = pygame.Rect(980, 24, 25, 25);

    def draw(self) -> None:
        self.screen.blit(self.image, pygame.Rect(0, 0, 1024, 768))

        pygame.draw.rect(self.screen, (220, 220, 220), self.background_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), (980, 24, 25, 25), 3)

        self.screen.blit(self.text, (986, 23))

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(0, 0, 1024, 768)

    def handle_events(self, events) -> None:
        self.image_class.handle_events(events)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.background_rect.collidepoint(event.pos):
                    if not self.main.fade_out and not self.main.fade_in:
                        self.main.fade_out = True
                        self.main.next_screen = 0
