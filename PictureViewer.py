
from genericpath import isfile
from ntpath import join
from os import listdir
import sys
import pygame
from helpers.ImageClass import ImageClass

from helpers.GalleryScreen import GalleryScreen
from helpers.PictureScreen import PictureScreen

class Main():
    def __init__(self):
        pygame.init()
        self.super = super()

        self.screen_width = 745 # 1024
        self.screen_height = 768
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("Picture Viewer")

    def run(self):
        self.gallery_screen = GalleryScreen(self.screen, screen_size=(self.screen_width, self.screen_height))
        self.picture_screen = PictureScreen()

        mypath = "images"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        for file in onlyfiles:
            self.gallery_screen.add_item(ImageClass(self.screen, file))

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

            self.gallery_screen.handle_events(events)
            self.gallery_screen.draw()

            pygame.display.flip()


main = Main()
main.run()
