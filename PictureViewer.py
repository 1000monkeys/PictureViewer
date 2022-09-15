
from genericpath import isfile
from ntpath import join
from os import listdir
import sys
from turtle import Screen
import pygame
from helpers.ImageClass import ImageClass

from helpers.GalleryScreen import GalleryScreen
from helpers.PictureScreen import PictureScreen

class Main():
    def __init__(self):
        pygame.init()
        self.super = super()

        self.fade_out = False
        self.fade_in = True
        self.alpha = 255

        self.screen_width = 1024 # 1024
        self.screen_height = 768
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("Picture Viewer")

    def change_to_picture_view(self, image_class):
        self.image_class = image_class
        self.alpha = 0
        self.screen_list[1].set_picture(self.image_class)
        self.fade_in = False
        self.fade_out = True

    def run(self):
        self.gallery_screen = GalleryScreen(self.screen, screen_size=(self.screen_width, self.screen_height))
        self.picture_screen = PictureScreen(self.screen)

        self.screen_list = list()
        self.screen_list.append(self.gallery_screen)
        self.screen_list.append(self.picture_screen)

        self.screen_id = 0

        mypath = "images"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        for file in onlyfiles:
            self.gallery_screen.add_item(ImageClass(self.screen, file, self))

        '''
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
        '''

        while True:
            pygame.time.Clock().tick(30)

            self.screen.fill((0, 0, 0))

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen_list[self.screen_id].handle_events(events)
            self.screen_list[self.screen_id].draw()

            if self.fade_out:
                self.alpha = self.alpha + 18
                if self.alpha > 255:
                    self.alpha = 255

                    self.fade_out = False
                    self.fade_in = True

                    self.screen_list[1].set_picture(self.image_class)
                    self.screen_id = 1
                s = pygame.Surface((1024, 768))
                s.set_alpha(self.alpha)
                s.fill((0, 0, 0))
                self.screen.blit(s, (0,0))
            if self.fade_in:
                self.alpha = self.alpha - 18
                if self.alpha < 0:
                    self.alpha = 0
                    self.fade_out = False
                    self.fade_in = False
                s = pygame.Surface((1024, 768))
                s.set_alpha(self.alpha)
                s.fill((0, 0, 0))
                self.screen.blit(s, (0,0))
            pygame.display.flip()


main = Main()
main.run()
