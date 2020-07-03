import pygame

class Setting():
    def __init__(self):
        self.screen_widht=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
class Ship():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('ship.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    def blitem(self):
        self.screen.blit(self.image,self.rect)




